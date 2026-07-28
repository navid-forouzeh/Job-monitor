#!/usr/bin/env python3
"""
Vereins-Finder für Coach Grid.

Findet Schweizer Sportvereine und -anlagen (Tennis, Golf, Schwimmen, Reiten,
Eishockey, Fussball, ...) über die Overpass-API von OpenStreetMap und
exportiert sie als CSV/JSON — inklusive Kontaktdaten und einem
Zahlungsfähigkeits-Score pro Verein.

Beispiele:
    python3 coachgrid/club_finder.py --sports tennis,golf,swimming
    python3 coachgrid/club_finder.py --sports all --out out/vereine
    python3 coachgrid/club_finder.py --sports tennis --area "Kanton Zürich"
    python3 coachgrid/club_finder.py --sports tennis --dry-run
    python3 coachgrid/club_finder.py --from-file cache/tennis.json --sports tennis

Datenquelle: OpenStreetMap (ODbL 1.0). Bei Weiterverwendung auf der Website
muss "© OpenStreetMap-Mitwirkende" genannt werden.
"""

import argparse
import csv
import json
import os
import re
import sys
import time
from dataclasses import dataclass, field, asdict

import requests

OVERPASS_ENDPOINTS = [
    "https://overpass-api.de/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter",
]

USER_AGENT = "coachgrid-club-finder/1.0 (+https://www.thecoachgrid.com)"


@dataclass(frozen=True)
class Segment:
    """Eine Sportart inkl. OSM-Filter und wirtschaftlicher Einordnung."""

    key: str
    label: str
    # Overpass-Filter. Jeder Eintrag wird zu `nwr<filter>(area.search);`
    filters: tuple
    # A = eigene Anlage + Personal, B = eigene Anlage/Halle, C = ehrenamtlich, ohne Infrastruktur
    budget_tier: str
    # Grobe Bandbreite Jahresbeitrag Erwachsene in CHF (Recherche, siehe marktanalyse-vereine.md)
    fee_chf: tuple
    note: str = ""


# Reihenfolge = empfohlene Akquise-Reihenfolge (siehe marktanalyse-vereine.md).
SEGMENTS = {
    s.key: s
    for s in [
        Segment(
            key="golf",
            label="Golf",
            filters=(
                '["club"="sport"]["sport"="golf"]',
                '["leisure"="golf_course"]',
            ),
            budget_tier="A",
            fee_chf=(790, 3500),
            note="Betrieb wie ein KMU, angestellte Pros und Geschäftsführung.",
        ),
        Segment(
            key="tennis",
            label="Tennis",
            filters=(
                '["club"="sport"]["sport"="tennis"]',
                '["leisure"="sports_centre"]["sport"="tennis"]',
                '["leisure"="pitch"]["sport"="tennis"]["name"]',
            ),
            budget_tier="B",
            fee_chf=(250, 900),
            note="Eigene Plätze = Fixkosten = Budget; ca. 900 Clubs in der CH.",
        ),
        Segment(
            key="swimming",
            label="Schwimmen",
            filters=(
                '["club"="sport"]["sport"="swimming"]',
                '["leisure"="sports_centre"]["sport"="swimming"]',
            ),
            budget_tier="B",
            fee_chf=(200, 800),
            note="Kursgeschäft (Schwimmkurse) hat die höchste Suchnachfrage.",
        ),
        Segment(
            key="equestrian",
            label="Reitsport",
            filters=(
                '["club"="sport"]["sport"="equestrian"]',
                '["leisure"="horse_riding"]',
            ),
            budget_tier="A",
            fee_chf=(300, 1200),
            note="Reitställe sind meist kommerziell geführt, nicht ehrenamtlich.",
        ),
        Segment(
            key="ice_hockey",
            label="Eishockey",
            filters=(
                '["club"="sport"]["sport"="ice_hockey"]',
                '["leisure"="sports_centre"]["sport"="ice_hockey"]',
            ),
            budget_tier="B",
            fee_chf=(400, 1500),
            note="Hohe Nachwuchskosten, bezahlte Trainer verbreitet.",
        ),
        Segment(
            key="fitness",
            label="Fitness / Kraftsport",
            filters=(
                '["leisure"="fitness_centre"]',
                '["club"="sport"]["sport"="fitness"]',
            ),
            budget_tier="A",
            fee_chf=(600, 1400),
            note="Kommerzielle Betriebe — zahlungsfähigste Gruppe, aber keine Vereine.",
        ),
        Segment(
            key="martial_arts",
            label="Kampfsport",
            filters=(
                '["club"="sport"]["sport"~"martial_arts|judo|karate|taekwondo|boxing|wrestling"]',
                '["leisure"="sports_centre"]["sport"~"martial_arts|judo|karate|taekwondo|boxing"]',
            ),
            budget_tier="B",
            fee_chf=(400, 1200),
            note="Oft als Schule/GmbH geführt, entscheidet schnell.",
        ),
        Segment(
            key="dance",
            label="Tanz",
            filters=(
                '["club"="sport"]["sport"="dance"]',
                '["leisure"="dance"]',
            ),
            budget_tier="B",
            fee_chf=(400, 1200),
        ),
        Segment(
            key="climbing",
            label="Klettern",
            filters=(
                '["club"="sport"]["sport"="climbing"]',
                '["leisure"="sports_centre"]["sport"="climbing"]',
            ),
            budget_tier="B",
            fee_chf=(300, 900),
        ),
        Segment(
            key="football",
            label="Fussball",
            filters=('["club"="sport"]["sport"="soccer"]',),
            budget_tier="C",
            fee_chf=(150, 500),
            note="1'345 Vereine, Anlage meist von der Gemeinde — wenig Fixkosten, wenig Budget.",
        ),
        Segment(
            key="gymnastics",
            label="Turnen",
            filters=('["club"="sport"]["sport"~"gymnastics|athletics"]',),
            budget_tier="C",
            fee_chf=(80, 250),
            note="2'650 Vereine (STV), fast durchwegs ehrenamtlich.",
        ),
        Segment(
            key="volleyball",
            label="Volleyball",
            filters=('["club"="sport"]["sport"="volleyball"]',),
            budget_tier="C",
            fee_chf=(100, 400),
        ),
        Segment(
            key="basketball",
            label="Basketball",
            filters=('["club"="sport"]["sport"="basketball"]',),
            budget_tier="C",
            fee_chf=(150, 500),
        ),
        Segment(
            key="rowing",
            label="Rudern / Segeln",
            filters=('["club"="sport"]["sport"~"rowing|sailing|canoe"]',),
            budget_tier="B",
            fee_chf=(300, 1200),
        ),
        Segment(
            key="shooting",
            label="Schiesssport",
            filters=('["club"="sport"]["sport"="shooting"]',),
            budget_tier="C",
            fee_chf=(80, 300),
        ),
        Segment(
            key="winter",
            label="Ski / Snowboard",
            filters=('["club"="sport"]["sport"~"skiing|ski|snowboard"]',),
            budget_tier="C",
            fee_chf=(80, 400),
        ),
    ]
}

TIER_SCORE = {"A": 4, "B": 3, "C": 1}


@dataclass
class Club:
    osm_type: str
    osm_id: int
    name: str
    sport: str
    sport_label: str
    website: str = ""
    email: str = ""
    phone: str = ""
    street: str = ""
    postcode: str = ""
    city: str = ""
    lat: float = 0.0
    lon: float = 0.0
    budget_tier: str = ""
    budget_score: int = 0
    signals: list = field(default_factory=list)

    @property
    def osm_url(self):
        return f"https://www.openstreetmap.org/{self.osm_type}/{self.osm_id}"


def build_query(segment, area_name=None, timeout=180):
    """Baut die Overpass-QL-Abfrage für eine Sportart."""
    if area_name:
        area = f'area["name"="{area_name}"]->.search;'
    else:
        area = 'area["ISO3166-1"="CH"][admin_level=2]->.search;'

    body = "\n".join(f"  nwr{f}(area.search);" for f in segment.filters)
    return f"[out:json][timeout:{timeout}];\n{area}\n(\n{body}\n);\nout center tags;"


def fetch(query, sleep=2.0, retries=3):
    """Fragt Overpass ab und wechselt bei Überlast den Endpunkt."""
    last_error = None
    for attempt in range(retries):
        endpoint = OVERPASS_ENDPOINTS[attempt % len(OVERPASS_ENDPOINTS)]
        try:
            response = requests.post(
                endpoint,
                data={"data": query},
                headers={"User-Agent": USER_AGENT},
                timeout=240,
            )
            if response.status_code == 200:
                return response.json()
            # 429 = rate limit, 504 = Overpass überlastet: beides ist wiederholbar
            last_error = f"HTTP {response.status_code} von {endpoint}"
        except requests.RequestException as exc:
            last_error = f"{type(exc).__name__}: {exc}"

        wait = sleep * (2**attempt)
        print(f"  ⚠️  {last_error} — neuer Versuch in {wait:.0f}s", file=sys.stderr)
        time.sleep(wait)

    raise RuntimeError(f"Overpass nicht erreichbar: {last_error}")


def score(tags, segment):
    """Bewertet, wie wahrscheinlich der Verein ein zahlender Kunde sein kann."""
    points = TIER_SCORE[segment.budget_tier]
    signals = []

    if tags.get("website") or tags.get("contact:website"):
        points += 1
        signals.append("website")
    if tags.get("email") or tags.get("contact:email"):
        points += 1
        signals.append("email")
    if tags.get("phone") or tags.get("contact:phone"):
        signals.append("phone")
    # Eigene Infrastruktur ist der beste Proxy für ein echtes Budget.
    if tags.get("leisure") in {"golf_course", "sports_centre", "fitness_centre", "horse_riding"}:
        points += 1
        signals.append("eigene_anlage")
    if tags.get("golf:holes") or tags.get("holes"):
        points += 1
        signals.append(f"golf_{tags.get('golf:holes') or tags.get('holes')}_loecher")
    if tags.get("operator:type") in {"private", "company"} or tags.get("office"):
        signals.append("kommerziell")

    return min(points, 10), signals


def parse(payload, segment):
    """Wandelt eine Overpass-Antwort in Club-Objekte um."""
    clubs = []
    for element in payload.get("elements", []):
        tags = element.get("tags", {})
        name = tags.get("name", "").strip()
        if not name:
            continue

        center = element.get("center", {})
        points, signals = score(tags, segment)

        clubs.append(
            Club(
                osm_type=element.get("type", ""),
                osm_id=element.get("id", 0),
                name=name,
                sport=segment.key,
                sport_label=segment.label,
                website=tags.get("website") or tags.get("contact:website", ""),
                email=tags.get("email") or tags.get("contact:email", ""),
                phone=tags.get("phone") or tags.get("contact:phone", ""),
                street=" ".join(
                    x for x in (tags.get("addr:street", ""), tags.get("addr:housenumber", "")) if x
                ),
                postcode=tags.get("addr:postcode", ""),
                city=tags.get("addr:city", ""),
                lat=element.get("lat") or center.get("lat") or 0.0,
                lon=element.get("lon") or center.get("lon") or 0.0,
                budget_tier=segment.budget_tier,
                budget_score=points,
                signals=signals,
            )
        )
    return clubs


# "Tennisclub Musterhausen", "TC Musterhausen" und "Tennis-Club Musterhausen"
# sind derselbe Verein — Sportart- und Rechtsformwörter fliegen darum raus.
_SPORT_WORD = r"(?:tennis|golf|schwimm|swim|nataton|fussball|football|turn|sport|hockey|reit|volley|basket|kletter|tanz|judo|karate|boxing|ski|rugby|unihockey)?"
_CLUB_WORD = r"(?:club|klub|verein|cercle|societ[ée]|association)"
_ABBREVIATIONS = r"\b(?:tc|tv|fc|sc|gc|hc|stv|sv|cs|ct)\b"


def normalize_name(name):
    original = name.lower()
    shortened = re.sub(_SPORT_WORD + _CLUB_WORD, " ", original)
    shortened = re.sub(_ABBREVIATIONS, " ", shortened)
    # Bleibt nichts übrig (z.B. "Tennisclub"), zählt der Originalname.
    return re.sub(r"[^a-z0-9]+", "", shortened) or re.sub(r"[^a-z0-9]+", "", original)


def domain_of(url):
    match = re.search(r"https?://(?:www\.)?([^/]+)", url or "")
    return match.group(1).lower() if match else ""


def dedupe(clubs):
    """Entfernt Duplikate (Anlage + Verein sind in OSM oft zwei Objekte)."""
    best = {}
    for club in clubs:
        keys = [f"n:{club.sport}:{normalize_name(club.name)}:{club.postcode}"]
        if club.website:
            keys.append(f"w:{domain_of(club.website)}")

        existing = next((best[k] for k in keys if k in best), None)
        if existing is None:
            for key in keys:
                best[key] = club
            continue

        # Der Eintrag mit mehr Information gewinnt, fehlende Felder werden ergänzt.
        for attr in ("website", "email", "phone", "street", "postcode", "city"):
            if not getattr(existing, attr) and getattr(club, attr):
                setattr(existing, attr, getattr(club, attr))
        if club.budget_score > existing.budget_score:
            existing.budget_score = club.budget_score
            existing.signals = club.signals
        for key in keys:
            best.setdefault(key, existing)

    seen, unique = set(), []
    for club in best.values():
        marker = (club.osm_type, club.osm_id)
        if marker not in seen:
            seen.add(marker)
            unique.append(club)
    return unique


CSV_COLUMNS = [
    "name",
    "sport_label",
    "budget_tier",
    "budget_score",
    "website",
    "email",
    "phone",
    "street",
    "postcode",
    "city",
    "lat",
    "lon",
    "signals",
    "osm_url",
]


def write_output(clubs, out_prefix):
    directory = os.path.dirname(out_prefix)
    if directory:
        os.makedirs(directory, exist_ok=True)

    clubs = sorted(clubs, key=lambda c: (-c.budget_score, c.sport, c.name))

    with open(f"{out_prefix}.csv", "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        for club in clubs:
            row = asdict(club)
            row["signals"] = "|".join(club.signals)
            row["osm_url"] = club.osm_url
            writer.writerow({k: row[k] for k in CSV_COLUMNS})

    with open(f"{out_prefix}.json", "w", encoding="utf-8") as handle:
        payload = []
        for club in clubs:
            row = asdict(club)
            row["osm_url"] = club.osm_url
            payload.append(row)
        json.dump(payload, handle, ensure_ascii=False, indent=2)

    return f"{out_prefix}.csv", f"{out_prefix}.json"


def summarize(clubs):
    """Kurzstatistik pro Sportart — was davon ist überhaupt kontaktierbar."""
    stats = {}
    for club in clubs:
        entry = stats.setdefault(club.sport_label, {"total": 0, "web": 0, "mail": 0, "hot": 0})
        entry["total"] += 1
        entry["web"] += bool(club.website)
        entry["mail"] += bool(club.email)
        entry["hot"] += club.budget_score >= 6
    return stats


def resolve_sports(value):
    if value in ("all", "alle"):
        return list(SEGMENTS.values())

    segments = []
    for key in (k.strip() for k in value.split(",")):
        if key not in SEGMENTS:
            raise SystemExit(
                f"Unbekannte Sportart '{key}'. Verfügbar: {', '.join(SEGMENTS)}"
            )
        segments.append(SEGMENTS[key])
    return segments


def main():
    parser = argparse.ArgumentParser(description="Findet Sportvereine für Coach Grid.")
    parser.add_argument(
        "--sports",
        default="tennis,golf,swimming",
        help=f"Kommaliste oder 'all'. Verfügbar: {', '.join(SEGMENTS)}",
    )
    parser.add_argument(
        "--area",
        default=None,
        help="OSM-Gebietsname, z.B. 'Kanton Zürich'. Standard: ganze Schweiz.",
    )
    parser.add_argument("--out", default="out/vereine", help="Pfad-Präfix für CSV/JSON.")
    parser.add_argument("--sleep", type=float, default=3.0, help="Pause zwischen Abfragen.")
    parser.add_argument("--min-score", type=int, default=0, help="Nur Vereine ab diesem Score.")
    parser.add_argument("--dry-run", action="store_true", help="Nur die Abfragen ausgeben.")
    parser.add_argument(
        "--from-file",
        default=None,
        help="Overpass-JSON von der Platte lesen statt abzufragen (Test/Offline).",
    )
    parser.add_argument("--cache-dir", default=None, help="Rohantworten hier ablegen.")
    args = parser.parse_args()

    segments = resolve_sports(args.sports)

    if args.dry_run:
        for segment in segments:
            print(f"# {segment.label}\n{build_query(segment, args.area)}\n")
        return 0

    all_clubs = []
    for index, segment in enumerate(segments):
        query = build_query(segment, args.area)
        print(f"🔎 {segment.label} …")

        if args.from_file:
            with open(args.from_file, encoding="utf-8") as handle:
                payload = json.load(handle)
        else:
            if index:
                time.sleep(args.sleep)
            payload = fetch(query, sleep=args.sleep)
            if args.cache_dir:
                os.makedirs(args.cache_dir, exist_ok=True)
                path = os.path.join(args.cache_dir, f"{segment.key}.json")
                with open(path, "w", encoding="utf-8") as handle:
                    json.dump(payload, handle, ensure_ascii=False)

        clubs = parse(payload, segment)
        print(f"   → {len(clubs)} Treffer")
        all_clubs.extend(clubs)

    unique = [c for c in dedupe(all_clubs) if c.budget_score >= args.min_score]
    csv_path, json_path = write_output(unique, args.out)

    print(f"\n✅ {len(unique)} Vereine (von {len(all_clubs)} Rohtreffern)")
    print(f"{'Sportart':<22}{'Total':>7}{'Website':>9}{'E-Mail':>8}{'Score≥6':>9}")
    for label, stat in sorted(summarize(unique).items(), key=lambda x: -x[1]["total"]):
        print(
            f"{label:<22}{stat['total']:>7}{stat['web']:>9}{stat['mail']:>8}{stat['hot']:>9}"
        )
    print(f"\n📄 {csv_path}\n📄 {json_path}")
    print("Datenquelle: OpenStreetMap-Mitwirkende (ODbL 1.0)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
