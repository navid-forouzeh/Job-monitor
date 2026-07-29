#!/usr/bin/env python3
"""
Baut die Excel-Datei «Vereine als Kunden» für Coach Grid.

    python3 coachgrid/build_vereinsmodell.py -> coachgrid/Coach_Grid_Vereinsmodell.xlsx

Aufbau: acht Blätter, pro Blatt eine Tabelle und darunter ein Fazit.
Blau hinterlegte Zellen sind Eingaben, alles andere rechnet sich daraus.
"""

import os

from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Coach_Grid_Vereinsmodell.xlsx")
STAND = "29.07.2026"

ARIAL = "Arial"
INK = "16302A"

F_TITLE = Font(name=ARIAL, size=18, bold=True, color=INK)
F_SUB = Font(name=ARIAL, size=11, color="5A6B65")
F_H2 = Font(name=ARIAL, size=12, bold=True, color=INK)
F_HEAD = Font(name=ARIAL, size=10, bold=True, color="FFFFFF")
F_BODY = Font(name=ARIAL, size=11)
F_BOLD = Font(name=ARIAL, size=11, bold=True)
F_SMALL = Font(name=ARIAL, size=10, color="5A6B65")
F_INPUT = Font(name=ARIAL, size=11, bold=True, color="0000FF")
F_FAZIT_LABEL = Font(name=ARIAL, size=11, bold=True, color="FFFFFF")
F_FAZIT = Font(name=ARIAL, size=11, color="10241E")
F_LINK = Font(name=ARIAL, size=10, color="0F6F5C", underline="single")

FILL_HEAD = PatternFill("solid", fgColor=INK)
FILL_INPUT = PatternFill("solid", fgColor="DCE6FA")
FILL_GOOD = PatternFill("solid", fgColor="D6ECD9")
FILL_WARN = PatternFill("solid", fgColor="FBE7C0")
FILL_BAD = PatternFill("solid", fgColor="F7D4CF")
FILL_FAZIT = PatternFill("solid", fgColor="E6F0EA")
FILL_LABEL = PatternFill("solid", fgColor="0F6F5C")

THIN = Side(style="thin", color="C9D2CE")
BOX = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

CHF = '"CHF" #,##0'
PCT = "0 %"
NUM = "#,##0"

WRAP = Alignment(wrap_text=True, vertical="center")
MID = Alignment(vertical="center")
CENTER = Alignment(horizontal="center", vertical="center")


def setup(book, name, heading, subtitle, widths):
    s = book.create_sheet(name)
    for index, width in enumerate(widths, start=1):
        s.column_dimensions[get_column_letter(index)].width = width
    s["A1"] = heading
    s["A1"].font = F_TITLE
    s.row_dimensions[1].height = 26
    s["A2"] = subtitle
    s["A2"].font = F_SUB
    s.sheet_view.showGridLines = False
    return s


def header(s, row, labels):
    for index, label in enumerate(labels, start=1):
        cell = s.cell(row=row, column=index, value=label)
        cell.font = F_HEAD
        cell.fill = FILL_HEAD
        cell.alignment = Alignment(wrap_text=True, vertical="center")
        cell.border = BOX
    s.row_dimensions[row].height = 30


def cell(s, row, column, value, font=F_BODY, fmt=None, fill=None, align=MID, height=None):
    c = s.cell(row=row, column=column, value=value)
    c.font = font
    c.alignment = align
    c.border = BOX
    if fmt:
        c.number_format = fmt
    if fill:
        c.fill = fill
    if height:
        s.row_dimensions[row].height = height
    return c


def fazit(s, row, columns, text):
    """Grüner Fazit-Block am Fuss jedes Blattes."""
    label = s.cell(row=row, column=1, value="FAZIT")
    label.font = F_FAZIT_LABEL
    label.fill = FILL_LABEL
    label.alignment = CENTER
    label.border = BOX
    body = s.cell(row=row, column=2, value=text)
    body.font = F_FAZIT
    body.fill = FILL_FAZIT
    body.alignment = Alignment(wrap_text=True, vertical="center")
    body.border = BOX
    s.merge_cells(start_row=row, start_column=2, end_row=row, end_column=columns)
    s.row_dimensions[row].height = 58


# ------------------------------------------------------------------ Blatt 1
def blatt_uebersicht(book):
    s = setup(book, "1 Auf einen Blick", "Vereine als Kunden",
              f"Coach Grid · Stand {STAND} · Zahlen aus Blatt 2 bis 4",
              (26, 22, 22, 22, 26))

    s["A4"] = "Die Chance"
    s["A4"].font = F_H2
    cell(s, 5, 1,
         "Ein einzelner Vertrag mit einem Verein bringt 10 bis 40 Coaches auf einmal — und damit 10× "
         "mehr Umsatz als eine Einzelanmeldung. 414 Vereine stehen bereits in unserer Liste mit Telefon "
         "und E-Mail-Adresse. Die zahlungsfähigen Vereine in der Schweiz: rund 3'500. TAM: CHF 1–4 Mio. ARR.",
         align=Alignment(wrap_text=True, vertical="center"), height=42)
    s.merge_cells("A5:E5")

    s["A7"] = "Umsatz über drei Jahre"
    s["A7"].font = F_H2
    header(s, 8, ["Szenario", "Vereine im Jahr 1", "Umsatz Jahr 1", "Umsatz Jahr 3", "3 Jahre zusammen"])
    for offset, name in enumerate(["Vorsichtig", "Realistisch", "Optimistisch"]):
        line = 9 + offset
        column = "DEF"[offset]
        # Blatt 3: Zeile 16 = Kunden Jahr 1, 17 = Umsatz Jahr 1,
        # 21 = Umsatz Jahr 3, 22 = drei Jahre zusammen
        cell(s, line, 1, name, font=F_BOLD)
        cell(s, line, 2, f"='3 Umsatz'!{column}16", fmt=NUM)
        cell(s, line, 3, f"='3 Umsatz'!{column}17", fmt=CHF)
        cell(s, line, 4, f"='3 Umsatz'!{column}21", fmt=CHF)
        cell(s, line, 5, f"='3 Umsatz'!{column}22", fmt=CHF, font=F_BOLD,
             fill=FILL_GOOD if offset == 1 else None)
        s.row_dimensions[line].height = 22

    s["A13"] = "Die drei wichtigsten Erkenntnisse"
    s["A13"].font = F_H2
    header(s, 14, ["Erkenntnis", "Was das heisst", "", "", ""])
    points = [
        ("Ein Vereinsvertrag = 10× mehr Umsatz als ein Einzelcoach",
         "Ein Verein mit 10 Coaches zahlt CHF 4'900 pro Jahr statt zehnmal CHF 399. Pro Abschluss "
         "entsteht mehr Umsatz — bei weniger Aufwand für Akquise und Betreuung. Das Vereinspaket "
         "beinhaltet Club-Dashboard und Vereinsprofil, darum ist der Preis pro Coach höher (Blatt 2)."),
        ("Fokus auf grosse Vereine: 20 reichen für CHF 180'000",
         "20 Vereine im M-Paket (10 Coaches, CHF 4'900/Jahr) ergeben CHF 98'000. Mit Clubs im L-Paket "
         "sind CHF 180'000 allein im Jahr 1 erreichbar — bei einem Bruchteil des Akquiseaufwands "
         "gegenüber hunderten Einzelcoaches (Blatt 3)."),
        ("Zwei Sportarten decken das ganze Jahr",
         "Golf läuft April bis Oktober, Eishockey September bis April. Wer beide Sportarten im "
         "Kundenstamm hat, hat zwölf Monate Anfragen statt einer toten Wintersaison — "
         "eine Kombination, die kein einzelner Coach bieten kann (Blatt 4)."),
    ]
    for offset, (claim, why) in enumerate(points):
        line = 15 + offset
        cell(s, line, 1, claim, font=F_BOLD, align=WRAP)
        cell(s, line, 2, why, align=WRAP, height=52)
        s.merge_cells(start_row=line, start_column=2, end_row=line, end_column=5)

    fazit(s, 19, 5,
          "Das Modell ist konkret: 414 Vereine sind bereits kontaktierbar, der erste Umsatz ist in "
          "90 Tagen erreichbar — ohne neue Entwicklung. Im realistischen Fall stehen nach drei Jahren "
          "rund CHF 470'000 auf dem Konto. Nächster Schritt: 50 Golfclubs anschreiben, drei "
          "Pilotkunden gewinnen, Zahlen messen (Blatt 7).")
    return s


# ------------------------------------------------------------------ Blatt 2
def blatt_preise(book):
    s = setup(book, "2 Preise", "Preise",
              "Einzelcoach CHF 399 / Jahr. Vereine zahlen pro Coach einen Aufschlag — "
              "dafür erhalten sie Club-Dashboard, zentrale Abrechnung und Vereinsprofil.",
              (26, 20, 20, 20, 20, 26))

    cell(s, 4, 1, "Einzelcoach — Preis pro Jahr (heute)", font=F_BOLD)
    cell(s, 4, 2, 399, font=F_INPUT, fmt=CHF, fill=FILL_INPUT, align=CENTER)
    cell(s, 4, 3, "Eingabe", font=F_SMALL, align=CENTER)

    s["A6"] = "Vereinspakete — Preis pro Coach und Jahr"
    s["A6"].font = F_H2
    header(s, 7, ["Stufe", "Coaches", "Pro Coach / Jahr", "Monatlich",
                  "Jahresbeispiel", "Aufschlag vs. Einzelcoach"])
    # (name, coaches_span, per_coach_price, example_coaches)
    tiers = [("S", "1 – 5", 549, 3), ("M", "6 – 15", 490, 10),
             ("L", "16 – 30", 449, 20), ("XL", "ab 31", 420, 35)]
    for offset, (name, span, per_coach, example_n) in enumerate(tiers):
        line = 8 + offset
        cell(s, line, 1, name, font=F_BOLD, align=CENTER)
        cell(s, line, 2, span, align=CENTER)
        cell(s, line, 3, per_coach, font=F_INPUT, fmt=CHF, fill=FILL_INPUT, align=CENTER)
        cell(s, line, 4, f"=C{line}/12", fmt=CHF, align=CENTER)
        cell(s, line, 5, f"=C{line}*{example_n}", fmt=CHF, font=F_BOLD, align=CENTER)
        cell(s, line, 6, f"=(C{line}-$B$4)/$B$4", fmt="0%", align=CENTER, fill=FILL_GOOD)
        s.row_dimensions[line].height = 22

    cell(s, 12, 1,
         "Jahresbeispiel: S = 3 Coaches (CHF 1'647/Jahr = CHF 137/Monat), M = 10, L = 20, XL = 35. "
         "Einstiegspreis ~0.8 % eines typischen Golfclub-Budgets (CHF 200'000+). "
         "Inklusive: Club-Dashboard, Sammelrechnung, Analytics, Vereinsprofil auf thecoachgrid.com.",
         font=F_SMALL, align=MID)
    s.merge_cells("A12:F12")
    s.row_dimensions[12].height = 28

    s["A14"] = "Jahreskosten im Vergleich: Vereinspaket vs. Einzelanmeldungen"
    s["A14"].font = F_H2
    header(s, 15, ["Coaches", "Stufe", "Vereinspreis total", "Einzeln total",
                   "Mehrkosten", "Aufschlag"])
    # (n_coaches, tier_row, tier_name)
    comparison = [
        (3,  8,  "S"),
        (5,  8,  "S"),
        (10, 9,  "M"),
        (15, 9,  "M"),
        (20, 10, "L"),
        (30, 10, "L"),
        (40, 11, "XL"),
    ]
    for offset, (n, tier_row, tier_name) in enumerate(comparison):
        line = 16 + offset
        cell(s, line, 1, n, fmt=NUM, font=F_BOLD, align=CENTER)
        cell(s, line, 2, tier_name, align=CENTER)
        cell(s, line, 3, f"={n}*$C${tier_row}", fmt=CHF, align=CENTER)
        cell(s, line, 4, f"={n}*$B$4", fmt=CHF, align=CENTER)
        cell(s, line, 5, f"=C{line}-D{line}", fmt=CHF, font=F_BOLD, align=CENTER, fill=FILL_WARN)
        cell(s, line, 6, f"=(C{line}-D{line})/D{line}", fmt="0%", align=CENTER, fill=FILL_GOOD)
        s.row_dimensions[line].height = 20

    chart = BarChart()
    chart.type = "col"
    chart.title = "Vereinspreis vs. Einzelanmeldungen (CHF / Jahr)"
    chart.y_axis.title = "CHF pro Jahr"
    chart.x_axis.title = "Anzahl Coaches im Verein"
    chart.height, chart.width = 8, 18
    chart.add_data(Reference(s, min_col=3, max_col=4, min_row=15, max_row=22), titles_from_data=True)
    chart.set_categories(Reference(s, min_col=1, min_row=16, max_row=22))
    s.add_chart(chart, "A26")

    fazit(s, 25, 6,
          "Der Einstieg liegt bei CHF 1'647/Jahr (3 Coaches, Stufe S) — das sind CHF 137/Monat und "
          "weniger als 1 % eines typischen Golfclub-Budgets. Für Coach Grid bedeutet jeder Vereinsvertrag "
          "mehr Umsatz pro Abschluss als zehn Einzelanmeldungen. Zusätzliches Modell im Aufbau: "
          "Coaches geben einen kleinen Anteil ihrer Buchungseinnahmen ab — der Verein verdient mit und "
          "hat damit einen eigenen Anreiz, seine Coaches aktiv zu platzieren.")
    return s


# ------------------------------------------------------------------ Blatt 3
def blatt_umsatz(book):
    s = setup(book, "3 Umsatz", "Umsatz",
              "Blau ist Eingabe. Wer dort etwas ändert, sieht sofort die Wirkung.",
              (30, 22, 4, 20, 20, 20))

    s["A4"] = "Annahmen"
    s["A4"].font = F_H2
    header(s, 5, ["", "", "", "Vorsichtig", "Realistisch", "Optimistisch"])
    inputs = [
        ("Vereine angeschrieben", 200, 350, 414, NUM),
        ("davon antworten", 0.12, 0.20, 0.30, PCT),
        ("davon werden Kunde", 0.08, 0.15, 0.25, PCT),
        ("Preis pro Verein und Jahr", 2200, 4900, 9000, CHF),
        ("bleiben im Folgejahr", 0.75, 0.85, 0.90, PCT),
        ("neue Vereine im Jahr 2", 8, 20, 45, NUM),
        ("neue Vereine im Jahr 3", 10, 30, 70, NUM),
    ]
    for offset, (label, bear, base, bull, fmt) in enumerate(inputs):
        line = 6 + offset
        cell(s, line, 1, label)
        s.merge_cells(start_row=line, start_column=1, end_row=line, end_column=3)
        for column, value in zip((4, 5, 6), (bear, base, bull)):
            cell(s, line, column, value, font=F_INPUT, fmt=fmt, fill=FILL_INPUT, align=CENTER)
        s.row_dimensions[line].height = 20

    # Eingaben stehen in Zeile 6 bis 12, die Ergebnisse ab Zeile 16.
    s["A14"] = "Ergebnis"
    s["A14"].font = F_H2
    header(s, 15, ["", "", "", "Vorsichtig", "Realistisch", "Optimistisch"])
    results = [
        ("Vereine als Kunde, Jahr 1", "=ROUND({c}6*{c}7*{c}8,0)", NUM, False),
        ("Umsatz Jahr 1", "={c}16*{c}9", CHF, False),
        ("Vereine als Kunde, Jahr 2", "=ROUND({c}16*{c}10+{c}11,0)", NUM, False),
        ("Umsatz Jahr 2", "={c}18*{c}9", CHF, False),
        ("Vereine als Kunde, Jahr 3", "=ROUND({c}18*{c}10+{c}12,0)", NUM, False),
        ("Umsatz Jahr 3", "={c}20*{c}9", CHF, False),
        ("Drei Jahre zusammen", "={c}17+{c}19+{c}21", CHF, True),
    ]
    for offset, (label, template, fmt, bold) in enumerate(results):
        line = 16 + offset
        cell(s, line, 1, label, font=F_BOLD if bold else F_BODY)
        s.merge_cells(start_row=line, start_column=1, end_row=line, end_column=3)
        for column in (4, 5, 6):
            cell(s, line, column, template.replace("{c}", get_column_letter(column)), fmt=fmt,
                 font=F_BOLD if bold else F_BODY,
                 fill=FILL_GOOD if bold else None, align=CENTER)
        s.row_dimensions[line].height = 20

    # Datengrundlage fürs Diagramm
    cell(s, 26, 1, "Diagrammdaten", font=F_SMALL)
    header(s, 27, ["", "", "", "Vorsichtig", "Realistisch", "Optimistisch"])
    for offset, (label, source) in enumerate([("Jahr 1", 17), ("Jahr 2", 19), ("Jahr 3", 21)]):
        line = 28 + offset
        cell(s, line, 1, label, font=F_SMALL)
        for column in (4, 5, 6):
            cell(s, line, column, f"={get_column_letter(column)}{source}", fmt=CHF, align=CENTER)

    chart = BarChart()
    chart.type = "col"
    chart.title = "Umsatz je Szenario"
    chart.y_axis.title = "CHF"
    chart.height, chart.width = 8, 18
    chart.add_data(Reference(s, min_col=4, max_col=6, min_row=27, max_row=30), titles_from_data=True)
    chart.set_categories(Reference(s, min_col=1, min_row=28, max_row=30))
    s.add_chart(chart, "A32")

    fazit(s, 24, 6,
          "Bereits im realistischen Szenario sind CHF 470'000 über drei Jahre erreichbar — "
          "mit 11 Vereinen im Jahr 1. Das optimistische Szenario liegt bei CHF 1.1 Mio., "
          "ebenfalls ohne neue Entwicklung. Der Schlüssel: grosse Vereine ansprechen, "
          "nicht viele kleine. 20 Vereine im L-Paket bringen mehr als 200 Einzelcoaches.")
    return s


# ------------------------------------------------------------------ Blatt 4
def blatt_markt(book):
    s = setup(book, "4 Markt", "Markt",
              "Grundlage ist die eigene Kontaktliste vom 28.07.2026 mit 414 Vereinen.",
              (26, 16, 18, 30, 10, 20, 36))

    header(s, 4, ["Sportart", "In unserer Liste", "Clubs in der Schweiz", "Saison",
                  "Stufe", "Umsatz bei 100 %", "Warum in dieser Reihenfolge"])
    market = [
        ("Golf", 103, 100, "April bis Oktober", "S", "='2 Preise'!E8",
         "Höchste Zahlungskraft: eigener Platz, Geschäftsführung, Marketingbudget. Typisches Club-Budget CHF 200'000+ — unser Einstiegspreis entspricht 0.8 % davon. Im Winter ruht der Betrieb."),
        ("Tennis", 99, 900, "Aussenplätze April bis Oktober, Halle ganzjährig", "M", "='2 Preise'!E9",
         "Grösste Zahl an Clubs mit eigener Anlage und eigenen Trainern."),
        ("Schwimmen", 180, 175, "ganzjährig (Hallenbad)", "M", "='2 Preise'!E9",
         "Laufendes Kursgeschäft ohne Saisonlücke; dort wird ohnehin nach Angeboten gesucht."),
        ("Reiten und Eishockey", 32, 450, "Eishockey September bis April, Reiten ganzjährig", "M", "='2 Preise'!E9",
         "Eishockey füllt genau die Monate, in denen Golf stillsteht."),
    ]
    for offset, (sport, ours, total, season, tier, price, why) in enumerate(market):
        line = 5 + offset
        cell(s, line, 1, sport, font=F_BOLD)
        cell(s, line, 2, ours, fmt=NUM, align=CENTER)
        cell(s, line, 3, total, fmt=NUM, align=CENTER)
        cell(s, line, 4, season, align=WRAP)
        cell(s, line, 5, tier, align=CENTER)
        cell(s, line, 6, f"=B{line}*{price[1:]}", fmt=CHF, align=CENTER, font=F_BOLD)
        cell(s, line, 7, why, align=WRAP, height=46)

    cell(s, 9, 1, "Total", font=F_BOLD)
    cell(s, 9, 2, "=SUM(B5:B8)", fmt=NUM, font=F_BOLD, align=CENTER)
    cell(s, 9, 3, "=SUM(C5:C8)", fmt=NUM, font=F_BOLD, align=CENTER)
    cell(s, 9, 4, "")
    cell(s, 9, 5, "")
    cell(s, 9, 6, "=SUM(F5:F8)", fmt=CHF, font=F_BOLD, fill=FILL_GOOD, align=CENTER)
    cell(s, 9, 7, "Obergrenze, wenn jeder Verein der Liste zahlt. Keine Planzahl.", align=WRAP)

    chart = BarChart()
    chart.type = "col"
    chart.title = "Kontaktierbare Vereine nach Sportart"
    chart.height, chart.width = 7.5, 16
    chart.add_data(Reference(s, min_col=2, max_col=2, min_row=4, max_row=8), titles_from_data=True)
    chart.set_categories(Reference(s, min_col=1, min_row=5, max_row=8))
    s.add_chart(chart, "A13")

    fazit(s, 11, 7,
          "414 Vereine stehen bereits in der Liste — mit Telefon und Mailadresse, morgen anschreibbar. "
          "Wichtig: der Schweizer Durchschnittsverein hat ein Budget von CHF 65'000 — unsere Zielgruppe "
          "sind nicht diese Vereine. Golfclubs mit eigener Anlage kommen auf CHF 200'000+, Tennisclubs auf "
          "CHF 100'000–300'000. Das sind genau die Clubs in unserer Liste. Golf + Eishockey = zwölf Monate "
          "Aktivität. Das ist ein struktureller Vorteil gegenüber jedem Anbieter, der nur eine Sportart bedient.")
    return s


# ------------------------------------------------------------------ Blatt 5
def blatt_risiken(book):
    s = setup(book, "5 Vorbereitung", "Herausforderungen und Lösungen",
              "Zehn bekannte Stolpersteine im Vereinsgeschäft — mit konkreten Lösungen für jeden.",
              (30, 38, 62, 20))

    header(s, 4, ["Thema", "Was man wissen muss", "Konkrete Massnahmen", "Ab wann relevant"])
    risks = [
        ("Golf-Saison als Chance planen",
         "Golf läuft April bis Oktober — das ist bekannt und planbar. Wer den Vertrag auf die Saison "
         "abstimmt, liefert dem Club von Anfang an den richtigen Vergleich.",
         "→ Jahresvertrag: Erfolg wird über die Saison gemessen, nicht über den Monat.\n"
         "→ Onboarding im Winter: Profile, Fotos und Kursplan sind parat, wenn die Saison startet.\n"
         "→ Eishockey ergänzen: Saison läuft September bis April — zusammen ganzjährig aktiv.\n"
         "→ Reporting pro Saison: zeigt das volle Bild statt einen einzelnen Wintermonat.",
         "ab Vertragsschluss"),
        ("Vereinsentscheide richtig timen",
         "Vereinsvorstände tagen oft quartalsweise. Wer das weiss, kann den Verkaufsprozess "
         "darauf ausrichten und vermeidet unnötige Wartezeit.",
         "→ Direkt beim Geschäftsführer oder Sekretariat ansetzen — der kann meist ohne Vorstand entscheiden.\n"
         "→ Preis unter der Genehmigungsschwelle des Vorstands wählen (oft CHF 5'000).\n"
         "→ Kostenlose Testphase bis zur nächsten Generalversammlung anbieten.\n"
         "→ Im Herbst verkaufen: Budgetfenster und Vereinsjahresbeginn fallen dann zusammen.",
         "ab dem ersten Gespräch"),
        ("Zielgruppe scharf definieren",
         "82 % der Schweizer Vereine haben kein angestelltes Personal und ein Budget von CHF 65'000 im "
         "Schnitt. Die 18 % mit eigener Anlage — Golfclubs CHF 200'000+, Tennisclubs CHF 100'000–300'000 "
         "— sind dafür solide Kunden. Genau diese stehen in unserer Liste.",
         "→ Nur Vereine mit eigener Anlage ansprechen (Golf, Tennis, Schwimmen, Reiten, Eishockey).\n"
         "→ Einstiegspaket S (3 Coaches, CHF 1'647/Jahr) = weniger als 1 % eines Golfclub-Budgets.\n"
         "→ Zahlung aus dem Marketing- oder Sponsoring-Budget statt aus der Vereinskasse vorschlagen.\n"
         "→ Per-Coach-Abrechnung: der Betrag wächst mit dem Verein mit, kein Schock durch eine Pauschale.\n"
         "→ Kleine Vereine ohne Anlage via Einzelcoach-Angebot (CHF 399) bedienen, nicht via Paket.",
         "bei der Listenauswahl"),
        ("Coaches aktiv einbinden",
         "Die Coaches sind der Kern der Plattform. Wenn sie wissen, was das Vereinspaket für sie bedeutet, "
         "werden sie es mittragen statt hinterfragen.",
         "→ Anfragen gehen direkt an den Coach — der Verein erhält nur eine Kopie (Blatt 6).\n"
         "→ Profil bleibt beim Coach, auch wenn er den Verein verlässt.\n"
         "→ Bewertungen und Referenzen gehören dem Coach, nicht dem Vereinskonto.\n"
         "→ Coaches vor der Unterschrift des Vereins informieren, nicht danach.",
         "vor Vertragsschluss"),
        ("Spielregeln für private Buchungen klären",
         "Manche Coaches bieten neben dem Vereinsangebot auch private Stunden an. Das ist legitim — "
         "solange es klar geregelt ist.",
         "→ Preisuntergrenze im Vertrag: Privatstunden liegen mindestens auf Vereinsniveau.\n"
         "→ Zweites Privat-Profil nur mit schriftlicher Freigabe des Vereins.\n"
         "→ Dashboard zeigt dem Verein alle Anfragen an seine Coaches transparent.\n"
         "→ Zugangscode erlischt automatisch beim Vereinsaustritt des Coaches.",
         "ab erstem Monat"),
        ("Mehrwert früh sichtbar machen",
         "Der Verein verlängert, wenn er sieht, was das Abo bringt. Monatliches Reporting "
         "macht den Nutzen greifbar — selbst in ruhigen Monaten.",
         "→ Erfolgskriterien (z. B. 2 Anfragen/Monat) vor der Unterschrift schriftlich festhalten.\n"
         "→ Monatliches Reporting ab Tag 1 — auch wenn die Zahlen klein starten.\n"
         "→ Erstes Jahr zum halben Preis gegen das Recht, den Verein als Referenz zu nennen.\n"
         "→ Bei schwachen Zahlen aktiv nachbessern (mehr Sichtbarkeit, bessere Profile) statt abwarten.",
         "nach 3 Monaten"),
        ("Kundenmix von Anfang an aufbauen",
         "Wenige grosse Vereine bringen viel Umsatz — das ist ein Vorteil, den man mit einem "
         "durchdachten Mix absichert.",
         "→ Kein Verein über 15 % des Vereinsumsatzes — Diversifikation schützt.\n"
         "→ Einzelcoach-Geschäft parallel weiterführen: gibt Stabilität und neue Vereins-Leads.\n"
         "→ Vertragsenden über das Jahr verteilen, nicht alle per 31. Dezember.\n"
         "→ Mindestens zwei Sportarten im Kundenstamm: Golf + Eishockey = ganzjährige Aktivität.",
         "ab dem fünften Kunden"),
        ("Grossverein-Onboarding skalierbar gestalten",
         "Ein Verein mit 30 Coaches ist beim ersten Mal aufwendig. Mit einem guten Prozess "
         "ist der zweite dreimal so schnell.",
         "→ Selbstregistrierung der Coaches über einen Vereinscode — kein manueller Import.\n"
         "→ Einmalige Einrichtungsgebühr deckt den Erstaufwand, gibt dem Verein klare Erwartungen.\n"
         "→ Einen Ansprechpartner im Verein benennen, der intern sammelt und nachfasst.\n"
         "→ Zeitaufwand im Piloten messen und in den Standardprozess überführen.",
         "beim ersten Grossverein"),
        ("Verbände als Partner gewinnen",
         "Swiss Tennis, Swiss Golf und Swiss Aquatics haben direkten Zugang zu allen Mitgliedsvereinen. "
         "Eine Partnerschaft öffnet Türen, die Einzelakquise nicht öffnet.",
         "→ Verband frühzeitig als Partner ansprechen statt abwarten.\n"
         "→ Auf Buchung und Matching setzen — reine Vereinsverzeichnisse kann jeder Verband selbst bauen.\n"
         "→ Erste Clubs in einer Region exklusiv einbinden — schafft Referenzen für den Verband.\n"
         "→ Marke bei den Coaches aufbauen: die bleiben loyal, auch wenn Verbände wechseln.",
         "im ersten Jahr"),
        ("Erstkontakt professionell gestalten",
         "414 Vereine stehen in der Liste — ein gezieltes, professionelles Anschreiben öffnet Türen. "
         "Qualität vor Quantität zahlt sich aus.",
         "→ Persönliche Anrede, Bezug auf Sportart und Vereinsgrösse — kein generisches Massen-Mail.\n"
         "→ In Wellen von 50 versenden statt 414 auf einmal — so kann man auf Rückmeldungen reagieren.\n"
         "→ Nach vier Tagen telefonisch nachfassen: viele Entscheider antworten lieber am Telefon.\n"
         "→ Abmeldemöglichkeit sauber einbauen, Absender klar erkennbar — schützt die Absender-Reputation.",
         "ab Woche 3"),
    ]
    for offset, (problem, hurt, options, when) in enumerate(risks):
        line = 5 + offset
        cell(s, line, 1, problem, font=F_BOLD, align=WRAP)
        cell(s, line, 2, hurt, align=WRAP)
        cell(s, line, 3, options, align=Alignment(wrap_text=True, vertical="top"))
        cell(s, line, 4, when, align=WRAP, height=104)

    fazit(s, 16, 4,
          "Alle zehn Punkte sind bekannt und lösbar — kein einziger erfordert neue Entwicklung. "
          "Saisonalität, Entscheidungszeit, Zielgruppe und Coach-Einbindung lassen sich mit "
          "Vertragsgestaltung und dem richtigen Erstkontakt regeln. Wer diese Liste kennt, "
          "ist vorbereitet — und der Pilot in 90 Tagen liefert die Zahlen, um es zu belegen.")
    return s


# ------------------------------------------------------------------ Blatt 6
def blatt_konflikt(book):
    s = setup(book, "6 Coach oder Verein", "Coach oder Verein",
              "Coach Grid bleibt eine Coach-Plattform und bietet Vereinen trotzdem echten Mehrwert — kein Widerspruch.",
              (26, 34, 34, 26))

    s["A4"] = "Drei Möglichkeiten"
    s["A4"].font = F_H2
    header(s, 5, ["Modell", "Dafür", "Dagegen", "Bewertung"])
    options = [
        ("Anfrage geht an den Verein",
         "Für den Verein die einfachste Zusage: er behält die Kundenbeziehung ganz.",
         "Aus der Coach-Plattform wird ein Vereinsverzeichnis. Der Kunde schreibt einen Coach an und "
         "landet bei einer Zentrale.",
         "Nicht empfohlen"),
        ("Anfrage geht nur an den Coach",
         "Alles bleibt wie heute, kein Eingriff ins Produkt.",
         "Der Verein sieht keinen Rücklauf und verlängert nach einem Jahr nicht.",
         "Zu wenig für den Verein"),
        ("Anfrage geht an den Coach, Verein erhält eine Kopie",
         "Der Coach bleibt Ansprechpartner. Der Verein sieht im Dashboard jede Anfrage und die Auslastung "
         "seiner Coaches.",
         "Braucht ein Vereinskonto und ein Dashboard.",
         "Empfohlen"),
    ]
    for offset, row in enumerate(options):
        line = 6 + offset
        for column, value in enumerate(row, start=1):
            fill = None
            if column == 4:
                fill = {"Empfohlen": FILL_GOOD, "Nicht empfohlen": FILL_BAD}.get(value, FILL_WARN)
            cell(s, line, column, value, align=WRAP,
                 font=F_BOLD if column in (1, 4) else F_BODY, height=62)

    s["A10"] = "Vier Fragen, die im Gespräch kommen"
    s["A10"].font = F_H2
    header(s, 11, ["Frage des Vereins", "Antwort", "Im Vertrag geregelt durch", ""])
    objections = [
        ("Melden sich unsere Coaches dann einfach privat an?",
         "Solange der Verein zahlt, läuft jeder seiner Coaches über den Vereinszugang.",
         "Zugangscode pro Coach; ein zweites Profil nur mit Freigabe des Vereins."),
        ("Sind Privatstunden nicht billiger als unsere Kurse?",
         "In Tennis, Schwimmen und Ski liegt die Privatstunde regelmässig über dem Vereinsangebot.",
         "Preisuntergrenze: Privatstunden eines Vereinscoaches mindestens auf Vereinsniveau."),
        ("Was passiert, wenn ein Coach uns verlässt?",
         "Sein Zugang wird deaktiviert. Der Verein zahlt nie für jemanden, der nicht mehr da ist.",
         "Deaktivierung innert fünf Werktagen, monatliche Abrechnung der Zugänge."),
        ("Könnt ihr uns neue Mitglieder garantieren?",
         "Wir erhöhen die Wahrscheinlichkeit, gefunden zu werden, messbar und nachvollziehbar — "
         "mit monatlichem Reporting ab Tag 1.",
         "Klare Erfolgskriterien vorab schriftlich, monatliches Dashboard, Ausstiegsrecht nach 12 Monaten."),
    ]
    for offset, (question, answer, clause) in enumerate(objections):
        line = 12 + offset
        cell(s, line, 1, question, font=F_BOLD, align=WRAP)
        cell(s, line, 2, answer, align=WRAP)
        cell(s, line, 3, clause, align=WRAP, height=54)
        s.merge_cells(start_row=line, start_column=3, end_row=line, end_column=4)

    fazit(s, 17, 4,
          "Die Anfrage geht an den Coach, der Verein bekommt sie in Kopie und sieht im Dashboard, was das "
          "Abo bringt. Damit bleibt die Plattform eine Coach-Plattform und der Verein hat trotzdem einen "
          "belegbaren Gegenwert. Die Website muss dafür nicht umgeschrieben werden.")
    return s


# ------------------------------------------------------------------ Blatt 6
def blatt_fahrplan(book):
    s = setup(book, "7 Fahrplan", "Fahrplan über 90 Tage",
              "Nach drei Monaten steht die Entscheidung — auf Basis gemessener Zahlen.",
              (16, 30, 46, 22, 26))

    header(s, 4, ["Zeitraum", "Schritt", "Was passiert", "Wer", "Fertig, wenn"])
    steps = [
        ("Woche 1–2", "Angebot fertigstellen",
         "Staffelpreise festlegen, Vertrag mit Zugangscodes und Preisuntergrenze aufsetzen, "
         "eine Seite für Vereine auf der Website.",
         "Robert und Navid", "Vertrag und Preisliste stehen"),
        ("Woche 2", "Zielliste schneiden",
         "Aus den 414 Kontakten die 50 aussichtsreichsten ziehen: Golf und grosse Tennisclubs mit Mailadresse.",
         "Navid", "Liste mit 50 Vereinen steht"),
        ("Woche 3–4", "Erste Welle",
         "50 Vereine anschreiben, nach vier Tagen telefonisch nachfassen.",
         "Navid", "50 angeschrieben und nachgefasst"),
        ("Woche 5–8", "Gespräche führen",
         "Termine wahrnehmen, Blatt 2 und 6 als Gesprächsgrundlage nutzen.",
         "Robert", "mindestens acht Termine"),
        ("Woche 6–10", "Drei Pilotkunden gewinnen",
         "Erstes Jahr zum halben Preis gegen das Recht, den Verein als Referenz zu nennen.",
         "Robert und Navid", "drei unterschriebene Verträge"),
        ("Woche 9–12", "Belegen und entscheiden",
         "Anfragen pro Pilotverein messen, Fallstudie schreiben, Preis fixieren oder Modell verwerfen.",
         "Navid", "Fallstudie liegt vor"),
    ]
    for offset, row in enumerate(steps):
        line = 5 + offset
        for column, value in enumerate(row, start=1):
            cell(s, line, column, value, align=WRAP,
                 font=F_BOLD if column == 1 else F_BODY, height=46)

    s["A12"] = "Klare Entscheidungsgrundlage nach 90 Tagen"
    s["A12"].font = F_H2
    header(s, 13, ["Kennzahl", "Zielwert — Pilot gilt als Erfolg", "", "", ""])
    stops = [
        ("Antworten auf 50 Anschreiben", "ab 6 Antworten (12 %)"),
        ("Abschlüsse nach 10 Gesprächen", "ab 1 Abschluss"),
        ("Anfragen pro Pilotverein und Monat", "ab 2 Anfragen"),
    ]
    for offset, (kpi, limit) in enumerate(stops):
        line = 14 + offset
        cell(s, line, 1, kpi)
        cell(s, line, 2, limit, font=F_BOLD, fill=FILL_GOOD, align=CENTER)
        s.merge_cells(start_row=line, start_column=2, end_row=line, end_column=5)

    fazit(s, 18, 5,
          "Der Pilot kostet drei Monate und keine Entwicklung — nur Zeit und 50 E-Mails. "
          "Er liefert Antwortquote, Abschlussquote, Anfragen pro Verein und Zahlungsbereitschaft: "
          "genau die Zahlen, die heute noch Annahmen sind. Nach 90 Tagen steht die Entscheidung "
          "auf Basis echter Daten — und nicht auf Basis von Schätzungen.")
    return s


# ------------------------------------------------------------------ Blatt 7
def blatt_zahlen(book):
    s = setup(book, "8 Zahlen und Quellen", "Zahlen und Quellen",
              "Getrennt nach belegten Zahlen und Eingaben, die im Pilot gemessen werden.",
              (44, 26, 20, 44))

    s["A4"] = "Belegte Zahlen"
    s["A4"].font = F_H2
    header(s, 5, ["Zahl", "Wert", "Art", "Quelle"])
    facts = [
        ("Sportvereine in der Schweiz", "18'310", "belegt", "Vereinsstudie 2022, Swiss Olympic"),
        ("Mitgliedschaften in Sportvereinen", "2'200'000", "belegt", "Vereinsstudie 2022, Swiss Olympic"),
        ("Durchschnittliche Jahreseinnahmen eines Vereins", "CHF 69'000", "belegt",
         "Observatorium Sport und Bewegung Schweiz"),
        ("Vereine ohne bezahlte Mitarbeitende", "82 %", "belegt", "Vereinsstudie 2022, Swiss Olympic"),
        ("Vereine mit existenzbedrohendem Problem", "41 %", "belegt", "Vereinsstudie 2022, Swiss Olympic"),
        ("Tennisclubs in der Schweiz", "rund 900", "belegt", "Swiss Tennis"),
        ("Golfclubs in der Schweiz", "über 90", "belegt", "Swiss PGA"),
        ("Schwimmvereine in der Schweiz", "175", "belegt", "Swiss Aquatics, Mitgliedvereine"),
        ("Fussballvereine in der Schweiz", "1'345", "belegt", "Schweizerischer Fussballverband"),
        ("Erwachsene in einem Sportverein", "22 %", "belegt", "Sport Schweiz 2020, BASPO"),
        ("Kinder von 10 bis 14 in einem Sportverein", "67 %", "belegt", "Sport Schweiz 2020, BASPO"),
        ("Saison National League Eishockey", "September bis April", "belegt",
         "Spielplan National League: Qualifikation September bis März, Playoffs bis April"),
        ("Saison Golfplätze Schweiz", "April bis Oktober", "belegt",
         "Saisonzeiten der Golfplätze, Graubünden Ferien. Je nach Höhenlage kürzer"),
        ("Kontaktierbare Vereine in unserer Liste", "414", "eigene Erhebung",
         "Eigene Liste vom 28.07.2026: Golf 103, Tennis 99, Schwimmen 180, Reiten und Eishockey 32"),
    ]
    for offset, row in enumerate(facts):
        line = 6 + offset
        for column, value in enumerate(row, start=1):
            cell(s, line, column, value, align=WRAP,
                 fill=FILL_GOOD if column == 3 else None,
                 font=F_BOLD if column == 2 else F_BODY, height=24)

    start = 6 + len(facts) + 1          # Leerzeile nach den belegten Zahlen
    s.cell(row=start, column=1, value="Eingaben, die im Pilot gemessen werden").font = F_H2
    header(s, start + 1, ["Eingabe", "Im Modell", "Art", "Wird gemessen durch"])
    assumptions = [
        ("Preis pro Coach und Jahr", "CHF 399", "Eingabe", "Bereits im Einsatz, auf Blatt 2 änderbar"),
        ("Antwortquote auf ein Anschreiben", "12 / 20 / 30 %", "Eingabe", "Erste Welle an 50 Vereine, Woche 3–4"),
        ("Anteil, der Kunde wird", "8 / 15 / 25 %", "Eingabe", "Gespräche in Woche 5–8"),
        ("Verlängerung im Folgejahr", "75 / 85 / 90 %", "Eingabe", "Erst nach zwölf Monaten messbar"),
        ("Coaches pro Verein", "10 bis 40", "Eingabe", "Wird im Erstgespräch erfasst"),
    ]
    for offset, row in enumerate(assumptions):
        line = start + 2 + offset
        for column, value in enumerate(row, start=1):
            cell(s, line, column, value, align=WRAP,
                 fill=FILL_WARN if column == 3 else None,
                 font=F_BOLD if column == 2 else F_BODY, height=24)

    quellen = start + 2 + len(assumptions) + 1
    s.cell(row=quellen, column=1, value="Quellen").font = F_H2
    links = [
        ("Vereinsstudie 2022, Swiss Olympic",
         "https://www.swissolympic.ch/dam/jcr:e13bfb8d-92a6-41a3-89e4-b80d30c2d23c/Vereinsstudie%202022_DE_Web.pdf"),
        ("Observatorium Sport und Bewegung Schweiz",
         "https://www.sportobs.ch/inhalte/Indikatoren_PDF_neu/Ind_22_Sportobs.pdf"),
        ("Sport Schweiz 2020, BASPO",
         "https://www.sportobs.ch/inhalte/Downloads/Bro_Sport_Schweiz_2020_d_WEB.pdf"),
        ("Swiss Aquatics, Mitgliedvereine",
         "https://www.swiss-aquatics.ch/verband/mitglieder/alle-mitgliedvereine/"),
        ("Swiss Tennis", "https://www.swisstennis.ch/de/"),
        ("Swiss Golf", "https://www.swissgolf.ch/"),
        ("Saisonzeiten Golfplätze, Graubünden Ferien",
         "https://www.graubuenden.ch/de/news/saisonzeiten-golfplaetze"),
        ("Spielplan National League", "https://www.sihf.ch/"),
    ]
    for offset, (label, url) in enumerate(links):
        line = quellen + 1 + offset
        s.cell(row=line, column=1, value=label).font = F_BODY
        link = s.cell(row=line, column=2, value=url)
        link.font = F_LINK
        link.hyperlink = url
        s.merge_cells(start_row=line, start_column=2, end_row=line, end_column=4)

    fazit(s, quellen + len(links) + 2, 4,
          "Dreizehn Marktzahlen sind belegt und verlinkt, eine stammt aus der eigenen Erhebung. Fünf Werte "
          "sind Eingaben — sie treiben das Ergebnis und werden im 90-Tage-Pilot durch gemessene Zahlen "
          "ersetzt. Bis dahin ist jedes Umsatzszenario eine Rechnung, keine Prognose.")
    return s


def main():
    book = Workbook()
    book.remove(book.active)

    blatt_uebersicht(book)
    blatt_preise(book)
    blatt_umsatz(book)
    blatt_markt(book)
    blatt_risiken(book)
    blatt_konflikt(book)
    blatt_fahrplan(book)
    blatt_zahlen(book)

    book.calculation.fullCalcOnLoad = True
    book.save(OUT)
    print(f"gebaut -> {OUT}")
    print("Blätter:", " | ".join(book.sheetnames))


if __name__ == "__main__":
    main()
