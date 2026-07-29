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

    s["A4"] = "Worum es geht"
    s["A4"].font = F_H2
    cell(s, 5, 1,
         "Heute meldet sich jeder Coach einzeln an. Ein Verein bringt 10 bis 40 Coaches auf einmal. "
         "Statt vieler Einzelverträge ein Vertrag mit dem Verein — eine Rechnung, ein Ansprechpartner.",
         align=Alignment(wrap_text=True, vertical="center"), height=34)
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
        ("Ein Preis für alle geht nicht",
         "CHF 10'000 im Jahr entsprechen 25 Coaches zum Einzelpreis. Ein Verein mit 15 Coaches zahlt "
         "damit mehr, als wenn sich seine Coaches einzeln anmelden. Lösung: Staffelpreise (Blatt 2)."),
        ("Wenige grosse statt viele kleine",
         "20 grosse Vereine zu CHF 9'900 bringen gleich viel Umsatz wie 200 kleine zu CHF 1'000 — "
         "bei einem Zehntel des Aufwands für Verkauf und Betreuung (Blatt 3)."),
        ("Die Anfrage bleibt beim Coach",
         "Der Verein zahlt für Sichtbarkeit und erhält jede Anfrage in Kopie. Die Anfrage selbst geht an "
         "den Coach. So bleibt die Plattform eine Coach-Plattform (Blatt 6)."),
    ]
    for offset, (claim, why) in enumerate(points):
        line = 15 + offset
        cell(s, line, 1, claim, font=F_BOLD, align=WRAP)
        cell(s, line, 2, why, align=WRAP, height=52)
        s.merge_cells(start_row=line, start_column=2, end_row=line, end_column=5)

    fazit(s, 19, 5,
          "Das Modell trägt — aber nur mit gestaffelten Preisen und mit Fokus auf grosse Vereine. "
          "Im realistischen Fall sind rund CHF 450'000 über drei Jahre erreichbar. Nächster Schritt: "
          "50 Vereine aus der bestehenden Liste anschreiben und drei Pilotkunden gewinnen (Blatt 7).")
    return s


# ------------------------------------------------------------------ Blatt 2
def blatt_preise(book):
    s = setup(book, "2 Preise", "Preise",
              "Der Vereinspreis muss unter der Summe der Einzelanmeldungen liegen.",
              (26, 20, 20, 20, 20, 26))

    cell(s, 4, 1, "Preis pro Coach und Jahr (heute)", font=F_BOLD)
    cell(s, 4, 2, 399, font=F_INPUT, fmt=CHF, fill=FILL_INPUT, align=CENTER)
    cell(s, 4, 3, "Eingabe", font=F_SMALL, align=CENTER)

    s["A6"] = "Staffelpreise"
    s["A6"].font = F_H2
    header(s, 7, ["Stufe", "Coaches", "Preis pro Jahr", "Preis pro Monat",
                  "Ersparnis pro Jahr", "Preis pro Coach"])
    tiers = [("S", "1 – 10", 2490, 249, 10), ("M", "11 – 25", 4900, 490, 18),
             ("L", "26 – 40", 9900, 990, 33), ("XL", "ab 41", 14900, 1490, 50)]
    for offset, (name, span, year, month, mid) in enumerate(tiers):
        line = 8 + offset
        cell(s, line, 1, name, font=F_BOLD, align=CENTER)
        cell(s, line, 2, span, align=CENTER)
        cell(s, line, 3, year, font=F_INPUT, fmt=CHF, fill=FILL_INPUT, align=CENTER)
        cell(s, line, 4, month, font=F_INPUT, fmt=CHF, fill=FILL_INPUT, align=CENTER)
        cell(s, line, 5, f"=D{line}*12-C{line}", fmt=CHF, font=F_BOLD, align=CENTER)
        cell(s, line, 6, f"=C{line}/{mid}", fmt=CHF, align=CENTER)
        s.row_dimensions[line].height = 22

    cell(s, 12, 1,
         "Wer jährlich zahlt, spart sichtbar. Beim grossen Verein sind das CHF 1'980.",
         font=F_SMALL, align=MID)
    s.merge_cells("A12:F12")

    s["A14"] = "Gegenprobe: ein Einheitspreis von CHF 10'000"
    s["A14"].font = F_H2
    header(s, 15, ["Coaches im Verein", "Einzeln angemeldet", "Einheitspreis",
                   "Differenz", "Verhältnis", "Ergebnis"])
    for offset, count in enumerate([5, 10, 15, 20, 25, 30, 40, 50]):
        line = 16 + offset
        cell(s, line, 1, count, fmt=NUM, align=CENTER, font=F_BOLD)
        cell(s, line, 2, f"=A{line}*$B$4", fmt=CHF, align=CENTER)
        cell(s, line, 3, 10000, fmt=CHF, align=CENTER)
        cell(s, line, 4, f"=C{line}-B{line}", fmt=CHF, align=CENTER)
        cell(s, line, 5, f"=C{line}/B{line}", fmt="0.00", align=CENTER)
        if count == 25:
            text, fill = "gleich teuer", FILL_WARN
        elif count * 399 < 10000:
            text, fill = "Verein zahlt mehr", FILL_BAD
        else:
            text, fill = "Verein spart", FILL_GOOD
        cell(s, line, 6, text, fill=fill, font=F_BOLD, align=CENTER)
        s.row_dimensions[line].height = 20

    chart = BarChart()
    chart.type = "col"
    chart.title = "Einheitspreis gegen Summe der Einzelanmeldungen"
    chart.y_axis.title = "CHF pro Jahr"
    chart.x_axis.title = "Coaches im Verein"
    chart.height, chart.width = 8, 18
    chart.add_data(Reference(s, min_col=2, max_col=3, min_row=15, max_row=23), titles_from_data=True)
    chart.set_categories(Reference(s, min_col=1, min_row=16, max_row=23))
    s.add_chart(chart, "A26")

    fazit(s, 25, 6,
          "CHF 10'000 geteilt durch CHF 399 ergibt 25 Coaches. Alles darunter ist für den Verein ein "
          "schlechtes Geschäft und im Gespräch nicht zu halten. Mit der Staffel bleibt jede Stufe unter "
          "der Summe der Einzelanmeldungen — der Verein spart auf jeder Stufe.")
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
        ("Preis pro Verein und Jahr", 2490, 4900, 6900, CHF),
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
          "Der Unterschied zwischen den Szenarien liegt fast vollständig im Preis pro Verein, nicht in "
          "der Anzahl Kunden. 20 Vereine zu CHF 9'900 bringen gleich viel wie 200 zu CHF 1'000. "
          "Darum zählt, wen man anspricht — nicht wie viele.")
    return s


# ------------------------------------------------------------------ Blatt 4
def blatt_markt(book):
    s = setup(book, "4 Markt", "Markt",
              "Grundlage ist die eigene Kontaktliste vom 28.07.2026 mit 414 Vereinen.",
              (26, 16, 18, 30, 10, 20, 36))

    header(s, 4, ["Sportart", "In unserer Liste", "Clubs in der Schweiz", "Saison",
                  "Stufe", "Umsatz bei 100 %", "Warum in dieser Reihenfolge"])
    market = [
        ("Golf", 103, 100, "April bis Oktober", "S", "='2 Preise'!C8",
         "Höchste Zahlungskraft: eigener Platz, Geschäftsführung, Marketingbudget. Im Winter ruht der Betrieb."),
        ("Tennis", 99, 900, "Aussenplätze April bis Oktober, Halle ganzjährig", "M", "='2 Preise'!C9",
         "Grösste Zahl an Clubs mit eigener Anlage und eigenen Trainern."),
        ("Schwimmen", 180, 175, "ganzjährig (Hallenbad)", "M", "='2 Preise'!C9",
         "Laufendes Kursgeschäft ohne Saisonlücke; dort wird ohnehin nach Angeboten gesucht."),
        ("Reiten und Eishockey", 32, 450, "Eishockey September bis April, Reiten ganzjährig", "M", "='2 Preise'!C9",
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
          "414 Vereine sind mit Name, Telefon und Mailadresse direkt ansprechbar. Golf zuerst, weil dort "
          "Budget und feste Ansprechpartner vorhanden sind — aber Golf steht von November bis März still. "
          "Eishockey läuft genau dann. Wer beide Sportarten im Kundenstamm hat, hat ganzjährig Anfragen "
          "statt einer toten Wintersaison. Risiken und Gegenmassnahmen auf Blatt 5.")
    return s


# ------------------------------------------------------------------ Blatt 5
def blatt_risiken(book):
    s = setup(book, "5 Risiken", "Was schiefgehen kann",
              "Zehn Probleme, die im Vereinsgeschäft auftreten — und was dagegen hilft.",
              (30, 38, 62, 20))

    header(s, 4, ["Problem", "Warum es weh tut", "Was man dagegen tun kann", "Wann es akut wird"])
    risks = [
        ("Golf ist ein Saisongeschäft",
         "Die Plätze sind etwa von April bis Oktober offen, in den Bergen kürzer. Von November bis März "
         "kommen kaum Anfragen — der Club sieht keinen Gegenwert und stellt das Abo infrage.",
         "1. Jahresvertrag statt Monatsabo: der Nutzen wird über die Saison gemessen, nicht über den Monat.\n"
         "2. Eishockey als Gegengewicht aufnehmen — dessen Saison läuft September bis April.\n"
         "3. Die Wintermonate im Vertrag als Vorbereitungszeit ausweisen: Profile, Fotos, Kursangebote für die neue Saison.\n"
         "4. Reporting pro Saison statt pro Monat verschicken.\n"
         "5. Im Winter verkaufen, im Frühling starten — dann fallen Budgetbeschluss und Saisonstart zusammen.",
         "ab dem ersten Winter"),
        ("Vereine entscheiden langsam",
         "Der Vorstand arbeitet ehrenamtlich und tagt oft nur quartalsweise. Grössere Ausgaben brauchen die "
         "Generalversammlung. Aus einem Gespräch werden schnell sechs Monate bis zur Unterschrift.",
         "1. Direkt beim Geschäftsführer oder Sekretariat ansetzen statt beim Gesamtvorstand.\n"
         "2. Den Preis so wählen, dass er unter der Genehmigungsschwelle des Vorstands liegt.\n"
         "3. Eine kostenlose Testphase bis zur nächsten Generalversammlung anbieten.\n"
         "4. Vertragsbeginn auf den Start des Vereinsjahrs legen.\n"
         "5. Den Verkauf ins Budgetfenster im Herbst legen, nicht ins Frühjahr.",
         "sofort, im ersten Gespräch"),
        ("Den meisten Vereinen fehlt schlicht das Geld",
         "82 Prozent der Schweizer Sportvereine haben keine bezahlte Person, die durchschnittlichen "
         "Jahreseinnahmen liegen bei CHF 69'000. Ein Abo über CHF 10'000 wäre dort ein Siebtel des Budgets.",
         "1. Nur Vereine mit eigener Anlage ansprechen — dort gibt es Fixkosten und damit eine Buchhaltung.\n"
         "2. Kleinere Vereine gar nicht als Verein verkaufen, sondern deren Coaches einzeln zu CHF 399.\n"
         "3. Zahlung aus dem Sponsoring- oder Marketingtopf statt aus der Vereinskasse vorschlagen.\n"
         "4. Abrechnung pro Coach statt Pauschale, damit der Betrag mitwächst.\n"
         "5. Rahmenvertrag über einen Verband prüfen statt Einzelverträge.",
         "bei jedem zweiten Kontakt"),
        ("Coaches fühlen sich übergangen",
         "Wenn der Verein den Zugang bezahlt, entsteht schnell der Eindruck, das Profil gehöre dem Verein. "
         "Genau die Coaches, wegen denen die Plattform existiert, verlieren dann das Interesse.",
         "1. Die Anfrage geht an den Coach, der Verein bekommt sie in Kopie (Blatt 6).\n"
         "2. Das Profil bleibt beim Coach, auch wenn er den Verein verlässt.\n"
         "3. Bewertungen und Referenzen gehören dem Coach, nicht dem Vereinskonto.\n"
         "4. Coaches vor der Unterschrift des Vereins informieren, nicht danach.\n"
         "5. Den Vereinsnamen als Zusatz im Profil führen, nicht als Absender.",
         "sobald der erste Verein aktiv ist"),
        ("Der Coach arbeitet privat weiter",
         "Der Verein zahlt, die Anfragen laufen aber an ihm vorbei in private Stunden. Dann bezahlt der "
         "Verein die Sichtbarkeit für ein Geschäft, an dem er nichts verdient.",
         "1. Preisuntergrenze im Vertrag: Privatstunden eines Vereinscoaches liegen mindestens auf Vereinsniveau.\n"
         "2. Ein zweites, privates Profil nur mit schriftlicher Freigabe des Vereins.\n"
         "3. Der Zugangscode erlischt beim Vereinsaustritt.\n"
         "4. Das Dashboard zeigt dem Verein alle Anfragen an seine Coaches.\n"
         "5. Verstoss führt zum Entzug des Zugangs, nicht zu einer Diskussion.",
         "nach den ersten Monaten"),
        ("Zu wenig Rücklauf, keine Verlängerung",
         "Wir können keine neuen Mitglieder garantieren. Bleiben die Anfragen aus, verlängert der Verein "
         "nach einem Jahr nicht — und erzählt es den Nachbarvereinen.",
         "1. Erfolgskriterien vor der Unterschrift schriftlich festhalten.\n"
         "2. Monatliches Reporting ab dem ersten Tag, auch wenn die Zahlen klein sind.\n"
         "3. Erstes Jahr zum halben Preis gegen das Recht, den Verein als Referenz zu nennen.\n"
         "4. Ausstiegsmöglichkeit nach zwölf Monaten statt Streit um die Restlaufzeit.\n"
         "5. Bei schwachen Zahlen nachbessern (mehr Sichtbarkeit) statt Geld zurückzahlen.",
         "nach zwölf Monaten"),
        ("Wenige Kunden tragen den ganzen Umsatz",
         "Zwanzig grosse Vereine bringen den Umsatz von zweihundert kleinen — kündigen drei davon, "
         "bricht ein Sechstel des Geschäfts weg.",
         "1. Kein Verein darf mehr als 15 Prozent des Vereinsumsatzes ausmachen.\n"
         "2. Das Einzelcoach-Geschäft bewusst weiterführen, nicht ersetzen.\n"
         "3. Vertragsenden über das Jahr verteilen statt alle per 31. Dezember.\n"
         "4. Nutzung des Dashboards als Frühwarnsignal beobachten.\n"
         "5. Mindestens zwei Sportarten im Kundenstamm halten.",
         "ab dem zehnten Kunden"),
        ("Onboarding von 40 Coaches kostet Zeit",
         "Ein Grossverein bedeutet vierzig Profile mit Foto, Text und Qualifikationen. Ohne Prozess "
         "verbrennt das mehr Zeit, als das Abo einbringt.",
         "1. Selbstregistrierung der Coaches über einen Vereinscode.\n"
         "2. Einmalige Einrichtungsgebühr, die den Aufwand deckt.\n"
         "3. Ein Ansprechpartner im Verein, der die Coaches sammelt und nachfasst.\n"
         "4. Profile per Liste importieren statt einzeln erfassen.\n"
         "5. Den Zeitaufwand im Pilot messen und in den Preis der nächsten Stufe einrechnen.",
         "beim ersten Grossverein"),
        ("Der Verband baut es selbst",
         "Swiss Tennis, Swiss Golf oder Swiss Aquatics haben die Vereine bereits als Mitglieder. Bauen sie "
         "ein eigenes Verzeichnis, verlieren wir den Zugang zu genau dieser Gruppe.",
         "1. Den Verband als Partner ansprechen, bevor er es selbst versucht.\n"
         "2. Auf Buchung und Lektion setzen — eine reine Auflistung kann jeder Verband selbst.\n"
         "3. Die ersten Clubs mit einer Exklusivität in ihrer Region binden.\n"
         "4. Schnell sein: ein Verbandsprojekt braucht Jahre, wir brauchen Monate.\n"
         "5. Die Marke bei den Coaches aufbauen — die bleiben, auch wenn der Verein wechselt.",
         "im zweiten Jahr"),
        ("Kaltakquise per Mail",
         "Wir schreiben Vereine an, die uns nicht kennen. Ohne Sorgfalt landet das im Spam und schadet "
         "der Absenderadresse für alle künftigen Mails.",
         "1. Nur allgemeine Vereinsadressen verwenden, keine privaten Adressen von Vorstandsmitgliedern.\n"
         "2. Abmeldemöglichkeit in jeder Mail, Absender und Kontakt klar erkennbar.\n"
         "3. Nach einem Widerspruch die Adresse dauerhaft aus der Liste nehmen.\n"
         "4. Höchstens zweimal schreiben, danach telefonisch nachfassen.\n"
         "5. In Wellen von 50 Adressen versenden statt 414 auf einmal.",
         "ab der ersten Welle"),
    ]
    for offset, (problem, hurt, options, when) in enumerate(risks):
        line = 5 + offset
        cell(s, line, 1, problem, font=F_BOLD, align=WRAP)
        cell(s, line, 2, hurt, align=WRAP)
        cell(s, line, 3, options, align=Alignment(wrap_text=True, vertical="top"))
        cell(s, line, 4, when, align=WRAP, height=104)

    fazit(s, 16, 4,
          "Kein Problem auf dieser Liste kippt das Modell — aber vier davon treffen schon im ersten Jahr: "
          "die Winterlücke bei Golf, die langsamen Vereinsentscheide, das fehlende Budget bei kleinen "
          "Vereinen und die Sorge der Coaches. Alle vier lassen sich mit Vertragsgestaltung und der Wahl "
          "der Zielgruppe entschärfen, nicht mit Entwicklung. Genau das ist im Fahrplan auf Blatt 7 abgebildet.")
    return s


# ------------------------------------------------------------------ Blatt 6
def blatt_konflikt(book):
    s = setup(book, "6 Coach oder Verein", "Coach oder Verein",
              "Der Verein zahlt nur, wenn er den Nutzen sieht. Die Plattform lebt davon, dass es um den Coach geht.",
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
         "Nein. Wir erhöhen die Wahrscheinlichkeit, gefunden zu werden — eine Zusage auf Kundenzahlen "
         "gibt niemand seriös ab.",
         "Keine Erfolgsgarantie. Stattdessen monatliches Reporting und Ausstieg nach 24 Monaten."),
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

    s["A12"] = "Wann wir das Modell wieder einpacken"
    s["A12"].font = F_H2
    header(s, 13, ["Kennzahl", "Grenze", "", "", ""])
    stops = [
        ("Antworten auf 50 Anschreiben", "unter 4 Antworten"),
        ("Abschlüsse nach 10 Gesprächen", "keiner"),
        ("Anfragen pro Pilotverein und Monat", "unter 2"),
    ]
    for offset, (kpi, limit) in enumerate(stops):
        line = 14 + offset
        cell(s, line, 1, kpi)
        cell(s, line, 2, limit, font=F_BOLD, fill=FILL_BAD, align=CENTER)
        s.merge_cells(start_row=line, start_column=2, end_row=line, end_column=5)

    fazit(s, 18, 5,
          "Der Pilot kostet drei Monate und keine Entwicklung. Er liefert genau die vier Zahlen, die "
          "heute noch Annahme sind: Antwortquote, Abschlussquote, Anfragen pro Verein und "
          "Zahlungsbereitschaft. Erst danach lohnt sich das Dashboard.")
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
