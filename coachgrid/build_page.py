#!/usr/bin/env python3
"""
Baut aus den CSVs in coachgrid/data/ eine durchsuchbare HTML-Seite.

    python3 coachgrid/build_page.py            -> coachgrid/vereine.html

Die Seite ist eine einzelne Datei ohne externe Abhängigkeiten: Telefonnummern
sind anrufbar, Mailadressen anklickbar, jeder Eintrag hat einen Kartenlink.
"""

import csv
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "data")

# Datei -> (Sportart, Geld-Tier gemäss marktanalyse-vereine.md)
SOURCES = [
    ("golf.csv", "Golf", "A"),
    ("tennis.csv", "Tennis", "B"),
    ("schwimmen.csv", "Schwimmen", "B"),
    ("reiten_eishockey.csv", "Reiten & Eishockey", "A/B"),
]

# HTTP-Status des Link-Checks -> was das für uns heisst
LINK_LABEL = {
    "200": ("ok", "Link geprüft"),
    "301": ("ok", "Link geprüft (Weiterleitung)"),
    "403": ("warn", "Seite blockt automatische Prüfung – im Browser prüfen"),
    "406": ("warn", "Seite blockt automatische Prüfung – im Browser prüfen"),
    "429": ("warn", "Seite blockt automatische Prüfung – im Browser prüfen"),
    "000": ("warn", "Zeitüberschreitung beim Prüfen – im Browser prüfen"),
    "404": ("bad", "Link tot (404)"),
    "500": ("bad", "Serverfehler (500)"),
    "334": ("warn", "Unklare Antwort – im Browser prüfen"),
    "-": ("none", "keine Website hinterlegt"),
    "": ("none", "keine Website hinterlegt"),
}


def load():
    clubs = []
    for filename, sport, tier in SOURCES:
        path = os.path.join(DATA, filename)
        with open(path, encoding="utf-8") as handle:
            for row in csv.DictReader(handle, delimiter=";"):
                if not row.get("name"):
                    continue
                status = (row.get("link_status") or "").strip()
                state, hint = LINK_LABEL.get(status, ("warn", f"HTTP {status}"))
                coords = (row.get("koordinaten") or "").strip()
                ort = (row.get("ort") or "").strip()
                if coords:
                    maps = f"https://www.openstreetmap.org/?mlat={coords.split(',')[0]}&mlon={coords.split(',')[1]}&zoom=16"
                elif ort:
                    maps = "https://www.openstreetmap.org/search?query=" + (
                        row["name"] + " " + ort
                    ).replace(" ", "+")
                else:
                    maps = ""
                clubs.append(
                    {
                        "sport": sport,
                        "tier": tier,
                        "name": row["name"].strip(),
                        "tel": (row.get("telefon") or "").strip(),
                        "mail": (row.get("email") or "").strip(),
                        "web": (row.get("website") or "").strip(),
                        "state": state,
                        "hint": hint,
                        "plz": (row.get("plz") or "").strip(),
                        "ort": ort,
                        "strasse": (row.get("strasse") or "").strip(),
                        "angebot": (row.get("angebot") or "").strip(),
                        "maps": maps,
                    }
                )
    clubs.sort(key=lambda c: (c["sport"], c["name"]))
    return clubs


PAGE = """<title>Schweizer Sportvereine – Kontaktliste für Coach Grid</title>
<style>
:root {
  color-scheme: light dark;
  --paper: #f4f6f4;
  --card: #ffffff;
  --ink: #10221d;
  --ink-soft: #4c605a;
  --line: #dae0dc;
  --accent: #0f6f5c;
  --accent-soft: #e3efeb;
  --ok: #2f7a4f;
  --warn: #9a6b12;
  --bad: #a8382f;
  --shadow: 0 1px 2px rgba(16, 34, 29, .06), 0 8px 24px -18px rgba(16, 34, 29, .5);
}
@media (prefers-color-scheme: dark) {
  :root {
    --paper: #0d1512;
    --card: #141d1a;
    --ink: #e6ece9;
    --ink-soft: #93a49e;
    --line: #24322d;
    --accent: #4fbfa4;
    --accent-soft: #16322b;
    --ok: #63b380;
    --warn: #d3a44c;
    --bad: #e08279;
    --shadow: 0 1px 2px rgba(0, 0, 0, .4);
  }
}
:root[data-theme="dark"] {
  --paper: #0d1512; --card: #141d1a; --ink: #e6ece9; --ink-soft: #93a49e;
  --line: #24322d; --accent: #4fbfa4; --accent-soft: #16322b;
  --ok: #63b380; --warn: #d3a44c; --bad: #e08279;
  --shadow: 0 1px 2px rgba(0, 0, 0, .4);
}
:root[data-theme="light"] {
  --paper: #f4f6f4; --card: #ffffff; --ink: #10221d; --ink-soft: #4c605a;
  --line: #dae0dc; --accent: #0f6f5c; --accent-soft: #e3efeb;
  --ok: #2f7a4f; --warn: #9a6b12; --bad: #a8382f;
  --shadow: 0 1px 2px rgba(16, 34, 29, .06), 0 8px 24px -18px rgba(16, 34, 29, .5);
}
body {
  margin: 0;
  background: var(--paper);
  color: var(--ink);
  font: 16px/1.55 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
  -webkit-text-size-adjust: 100%;
}
.wrap { max-width: 1080px; margin: 0 auto; padding: 0 20px 72px; }
header { padding: 40px 0 24px; }
h1 {
  font-family: "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
  font-size: clamp(28px, 4.4vw, 40px);
  line-height: 1.12; margin: 0 0 10px; text-wrap: balance; letter-spacing: -.01em;
}
.lede { margin: 0; max-width: 62ch; color: var(--ink-soft); }
.stats { display: flex; flex-wrap: wrap; gap: 10px; margin: 22px 0 0; }
.stat {
  background: var(--card); border: 1px solid var(--line); border-radius: 10px;
  padding: 10px 14px; box-shadow: var(--shadow);
}
.stat b { display: block; font-size: 22px; font-variant-numeric: tabular-nums; }
.stat span { font-size: 12px; letter-spacing: .06em; text-transform: uppercase; color: var(--ink-soft); }
.toolbar {
  position: sticky; top: 0; z-index: 5; background: var(--paper);
  padding: 14px 0; border-bottom: 1px solid var(--line); margin-bottom: 20px;
  display: flex; flex-wrap: wrap; gap: 10px; align-items: center;
}
input[type="search"] {
  flex: 1 1 240px; min-width: 0; padding: 10px 13px; font-size: 15px;
  border: 1px solid var(--line); border-radius: 9px; background: var(--card); color: inherit;
}
input[type="search"]:focus-visible, .chip:focus-visible, a:focus-visible {
  outline: 2px solid var(--accent); outline-offset: 2px;
}
.chip {
  border: 1px solid var(--line); background: var(--card); color: var(--ink-soft);
  padding: 8px 13px; border-radius: 999px; font-size: 14px; cursor: pointer;
  font-family: inherit; white-space: nowrap;
}
.chip[aria-pressed="true"] { background: var(--accent-soft); border-color: var(--accent); color: var(--accent); font-weight: 600; }
.list { display: grid; gap: 10px; }
.club {
  background: var(--card); border: 1px solid var(--line); border-left: 3px solid var(--accent);
  border-radius: 10px; padding: 14px 16px; box-shadow: var(--shadow);
  display: grid; grid-template-columns: 1fr auto; gap: 6px 18px; align-items: start;
}
.club h2 { grid-column: 1; margin: 0; font-size: 17px; line-height: 1.3; font-weight: 650; }
.meta { grid-column: 1; margin: 0; color: var(--ink-soft); font-size: 14px; }
.meta em { font-style: normal; color: var(--accent); }
.actions { grid-column: 2; grid-row: 1 / span 2; display: flex; flex-wrap: wrap; gap: 6px; justify-content: flex-end; }
.actions a {
  font-size: 13px; text-decoration: none; color: var(--ink); border: 1px solid var(--line);
  border-radius: 8px; padding: 6px 10px; background: var(--paper); white-space: nowrap;
}
.actions a:hover { border-color: var(--accent); color: var(--accent); }
.actions a.dead { color: var(--bad); border-color: var(--bad); text-decoration: line-through; }
.actions a.shaky { color: var(--warn); border-color: var(--warn); }
.empty { padding: 40px 0; color: var(--ink-soft); }
footer { margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line); color: var(--ink-soft); font-size: 14px; }
footer a { color: var(--accent); }
@media (max-width: 620px) {
  .club { grid-template-columns: 1fr; }
  .actions { grid-column: 1; grid-row: auto; justify-content: flex-start; }
}
</style>

<div class="wrap">
<header>
  <h1>Schweizer Sportvereine – wer erreichbar ist</h1>
  <p class="lede">Golf-, Tennis-, Schwimm-, Reit- und Eishockey-Anbieter mit Telefon, Mail und Standort.
  Jede hinterlegte Website wurde am 28.07.2026 automatisch angesteuert; das Ergebnis steht am Eintrag.</p>
  <div class="stats" id="stats"></div>
</header>

<div class="toolbar">
  <input type="search" id="q" placeholder="Suchen: Name, Ort, PLZ, Angebot …" autocomplete="off">
  <button class="chip" data-sport="alle" aria-pressed="true">Alle</button>
  <button class="chip" data-sport="Golf" aria-pressed="false">Golf</button>
  <button class="chip" data-sport="Tennis" aria-pressed="false">Tennis</button>
  <button class="chip" data-sport="Schwimmen" aria-pressed="false">Schwimmen</button>
  <button class="chip" data-sport="Reiten &amp; Eishockey" aria-pressed="false">Reiten &amp; Eishockey</button>
  <button class="chip" id="onlyContact" aria-pressed="false">Nur mit Telefon/Mail</button>
</div>

<div class="list" id="list"></div>
<p class="empty" id="empty" hidden>Kein Treffer.</p>

<footer>
  <p>Quellen: OpenStreetMap-Mitwirkende (ODbL 1.0) für Golf, Tennis, Reiten und Eishockey;
  <a href="https://www.swiss-aquatics.ch/verband/mitglieder/alle-mitgliedvereine/">Swiss Aquatics Mitgliedvereine</a> für Schwimmen.
  Kontaktdaten sind der jeweiligen Quelle entnommen und nicht einzeln nachtelefoniert.</p>
</footer>
</div>

<script>
const CLUBS = __DATA__;
const list = document.getElementById('list');
const empty = document.getElementById('empty');
const q = document.getElementById('q');
const onlyContact = document.getElementById('onlyContact');
let sport = 'alle';

function stats() {
  const n = CLUBS.length;
  const tel = CLUBS.filter(c => c.tel).length;
  const mail = CLUBS.filter(c => c.mail).length;
  const ok = CLUBS.filter(c => c.state === 'ok').length;
  document.getElementById('stats').innerHTML = [
    [n, 'Einträge'], [tel, 'mit Telefon'], [mail, 'mit E-Mail'], [ok, 'Links geprüft ok']
  ].map(([v, l]) => `<div class="stat"><b>${v}</b><span>${l}</span></div>`).join('');
}

function esc(s) {
  return String(s).replace(/[&<>"]/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[ch]));
}

function card(c) {
  const ort = [c.plz, c.ort].filter(Boolean).join(' ');
  const where = [c.strasse, ort].filter(Boolean).join(', ');
  const actions = [];
  if (c.tel) actions.push(`<a href="tel:${esc(c.tel.replace(/\\s/g, ''))}">${esc(c.tel)}</a>`);
  if (c.mail) actions.push(`<a href="mailto:${esc(c.mail)}">E-Mail</a>`);
  if (c.web) {
    const cls = c.state === 'bad' ? ' class="dead"' : (c.state === 'warn' ? ' class="shaky"' : '');
    actions.push(`<a href="${esc(c.web)}"${cls} target="_blank" rel="noopener" title="${esc(c.hint)}">Website</a>`);
  }
  if (c.maps) actions.push(`<a href="${esc(c.maps)}" target="_blank" rel="noopener">Karte</a>`);
  return `<article class="club">
    <h2>${esc(c.name)}</h2>
    <p class="meta"><em>${esc(c.sport)}</em>${where ? ' · ' + esc(where) : ''}${c.angebot ? ' · ' + esc(c.angebot) : ''}</p>
    <div class="actions">${actions.join('')}</div>
  </article>`;
}

function render() {
  const term = q.value.trim().toLowerCase();
  const contactOnly = onlyContact.getAttribute('aria-pressed') === 'true';
  const hits = CLUBS.filter(c => {
    if (sport !== 'alle' && c.sport !== sport) return false;
    if (contactOnly && !c.tel && !c.mail) return false;
    if (!term) return true;
    return [c.name, c.ort, c.plz, c.angebot, c.strasse].join(' ').toLowerCase().includes(term);
  });
  list.innerHTML = hits.map(card).join('');
  empty.hidden = hits.length > 0;
}

document.querySelectorAll('.chip[data-sport]').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.chip[data-sport]').forEach(b => b.setAttribute('aria-pressed', String(b === btn)));
    sport = btn.dataset.sport;
    render();
  });
});
onlyContact.addEventListener('click', () => {
  onlyContact.setAttribute('aria-pressed', onlyContact.getAttribute('aria-pressed') === 'true' ? 'false' : 'true');
  render();
});
q.addEventListener('input', render);
stats();
render();
</script>
"""


def main():
    clubs = load()
    html = PAGE.replace("__DATA__", json.dumps(clubs, ensure_ascii=False))
    out = os.path.join(BASE, "vereine.html")
    with open(out, "w", encoding="utf-8") as handle:
        handle.write(html)

    per_sport = {}
    for c in clubs:
        per_sport[c["sport"]] = per_sport.get(c["sport"], 0) + 1
    print(f"{len(clubs)} Einträge -> {out}")
    for sport, count in sorted(per_sport.items()):
        rows = [c for c in clubs if c["sport"] == sport]
        tel = sum(1 for c in rows if c["tel"])
        mail = sum(1 for c in rows if c["mail"])
        print(f"  {sport:<20}{count:>4}  Telefon {tel:>3}  Mail {mail:>3}")


if __name__ == "__main__":
    main()
