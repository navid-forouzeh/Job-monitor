# Coach Grid — Vereine finden

| Datei | Was |
|---|---|
| `Coach_Grid_Vereinsmodell.xlsx` | **Entscheidungsmodell «Vereine als B2B-Kunden»** — Staffelpreise, Szenarien über 3 Jahre, Sensitivität, Zielkonflikt Coach/Verein, 90-Tage-Fahrplan. Gebaut mit `build_vereinsmodell.py` |
| **[`data/`](data/)** | **414 Schweizer Vereine und Anlagen mit Telefon, Mail, Adresse und Angebot** — Golf 103, Tennis 99, Schwimmen 180, Reiten & Eishockey 32 |
| `vereine.html` | Dieselbe Liste als durchsuchbare Seite (Telefon anrufbar, Mail anklickbar, Kartenlink pro Eintrag) |
| [`quellen.md`](quellen.md) | Jede Zahl mit ihrer Quelle, jeder Link mit Prüfstatus vom 28.07.2026 |
| [`marktanalyse-vereine.md`](marktanalyse-vereine.md) | Wie viele Leute suchen einen Verein, wie viele Mitglieder ein Verein zum Rendieren braucht, welche Vereinstypen zahlen können |
| `club_finder.py` | Script, das weitere Sportarten aus OpenStreetMap nachzieht |
| `build_page.py` | Baut `vereine.html` aus den CSVs neu |

## Die Liste

```bash
python3 coachgrid/build_page.py   # CSVs -> coachgrid/vereine.html
```

Die CSVs sind semikolongetrennt (Excel-tauglich) mit den Spalten
`name; telefon; email; website; link_status; plz; ort; strasse; angebot; koordinaten`.

`link_status` ist der HTTP-Code vom Link-Check am 28.07.2026:
`200`/`301` = erreichbar, `403`/`406`/`429`/`000` = Server blockt die automatische
Prüfung oder antwortet zu langsam (im Browser meist normal erreichbar),
`404`/`500` = Link tot, `-` = keine Website hinterlegt.
Jede hinterlegte Website wurde angesteuert (rund 400 Checks über alle Sportarten);
im Durchgang Golf + Schwimmen antworteten 248 von 277 Adressen sauber.

Zwei Mehrsport-Anlagen (Centre Sportif de la Vigne Blanche, Sportzentrum Prau la Selva)
stehen bewusst in zwei Dateien, weil sie beide Sportarten anbieten.

## Schnellstart

```bash
pip install requests

# Die drei interessantesten Sportarten, ganze Schweiz
python3 coachgrid/club_finder.py --sports tennis,golf,swimming --out out/vereine

# Alle 16 Sportarten
python3 coachgrid/club_finder.py --sports all --out out/vereine --cache-dir cache

# Nur ein Kanton
python3 coachgrid/club_finder.py --sports tennis --area "Kanton Zürich"

# Nur die zahlungsfähigen (Score >= 6)
python3 coachgrid/club_finder.py --sports all --min-score 6

# Abfragen anschauen, ohne etwas zu laden
python3 coachgrid/club_finder.py --sports golf --dry-run
```

Ausgabe: `out/vereine.csv` und `out/vereine.json` mit Name, Sportart, Website,
E-Mail, Telefon, Adresse, Koordinaten, OSM-Link und einem Score.

## Der Score (0–10)

Schätzt, ob ein Verein überhaupt Geld ausgeben kann — die Herleitung steht in
Kapitel 4/5 der Marktanalyse.

| Punkte | Woher |
|---|---|
| 4 / 3 / 1 | Tier A (Golf, Reiten, Fitness) / Tier B (Tennis, Schwimmen, Eishockey, …) / Tier C (Fussball, Turnen, …) |
| +1 | Website hinterlegt |
| +1 | E-Mail hinterlegt |
| +1 | eigene Anlage (`sports_centre`, `golf_course`, `fitness_centre`, `horse_riding`) |
| +1 | Golfplatz mit Lochangabe |

**Ab 6 lohnt sich die Ansprache**, darunter ist es ein Gratis-Listing für SEO.

## Sportarten

`golf`, `tennis`, `swimming`, `equestrian`, `ice_hockey`, `fitness`, `martial_arts`,
`dance`, `climbing`, `football`, `gymnastics`, `volleyball`, `basketball`, `rowing`,
`shooting`, `winter` — die Reihenfolge in `SEGMENTS` ist gleichzeitig die empfohlene
Akquise-Reihenfolge.

Neue Sportart = ein `Segment(...)`-Eintrag in `club_finder.py`; die
[OSM-Werte für `sport=*`](https://wiki.openstreetmap.org/wiki/Key:sport) sind die Referenz.

## Datenquelle und Grenzen

Daten kommen aus **OpenStreetMap** über die Overpass-API — gratis, keine API-Keys,
aber:

- **Lizenz ODbL 1.0**: bei Nutzung auf der Website muss "© OpenStreetMap-Mitwirkende"
  stehen. Für ein Verzeichnis ist das unproblematisch.
- **Abdeckung ist nicht vollständig.** OSM kennt Anlagen besser als Vereine. Ein
  Turnverein ohne eigene Halle taucht oft gar nicht auf, ein Tennisplatz fast immer.
- **Fair Use:** Overpass ist ein Gratisdienst. Das Script macht eine Abfrage pro
  Sportart mit 3 s Pause und schaltet bei Überlast auf einen zweiten Endpunkt um.
  Ergebnisse mit `--cache-dir` ablegen statt neu abfragen.
- **Kein Scraping der Verbandsseiten.** Das Script liest nur OSM.

### Zweitquellen für die Lücken

Wenn die OSM-Abdeckung für eine Sportart zu dünn ist, sind das die offiziellen
Verzeichnisse (jeweils vorher Nutzungsbedingungen prüfen):

| Sportart | Verband |
|---|---|
| Tennis (~900 Clubs) | swisstennis.ch |
| Golf (>90 Clubs) | swissgolf.ch |
| Schwimmen (~175 Vereine) | swiss-aquatics.ch — publiziert zusätzlich die gemeldeten Mitgliederzahlen pro Verein, damit lässt sich die Vereinsgrösse direkt validieren |
| Fussball (1'345 Vereine) | football.ch |
| Turnen (2'650 Vereine) | stv-fsg.ch |
| Eishockey | sihf.ch |
| alle übrigen | swissolympic.ch → Mitgliedverbände |

## Tests

```bash
python3 coachgrid/test_club_finder.py
```

11 Tests, laufen ohne Netzwerk (Fixture statt Overpass). Geprüft sind
Query-Bau, Parsing, Scoring, Duplikat-Zusammenführung und der Export.

> Die Overpass-Abfragen selbst konnten in der Entwicklungsumgebung nicht live
> getestet werden (kein ausgehender Netzzugriff). Vor dem ersten grossen Lauf
> einmal `--sports golf` als Stichprobe fahren — Golf ist klein und in OSM gut erfasst.
