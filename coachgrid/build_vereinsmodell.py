#!/usr/bin/env python3
"""
Baut das Entscheidungsmodell «Vereine als B2B-Kunden» als Excel-Datei.

    python3 coachgrid/build_vereinsmodell.py -> coachgrid/Coach_Grid_Vereinsmodell.xlsx

Alle Zahlen im Modell hängen an den blau markierten Eingabezellen. Wer dort
etwas ändert, sieht sofort, was mit dem Umsatz passiert.
"""

import os

from openpyxl import Workbook
from openpyxl.chart import BarChart, LineChart, Reference
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Coach_Grid_Vereinsmodell.xlsx")
STAND = "29.07.2026"
COACH_PREIS = 399  # heutiger Einzelpreis pro Coach und Jahr

ARIAL = "Arial"
INK = "16302A"
ACCENT = "0F6F5C"

F_TITLE = Font(name=ARIAL, size=16, bold=True, color=INK)
F_H2 = Font(name=ARIAL, size=12, bold=True, color=INK)
F_HEAD = Font(name=ARIAL, size=10, bold=True, color="FFFFFF")
F_BODY = Font(name=ARIAL, size=10)
F_BOLD = Font(name=ARIAL, size=10, bold=True)
F_ITAL = Font(name=ARIAL, size=10, italic=True, color="55635E")
F_INPUT = Font(name=ARIAL, size=10, color="0000FF")  # Eingabe
F_LINK = Font(name=ARIAL, size=10, color=ACCENT, underline="single")

FILL_HEAD = PatternFill("solid", fgColor=INK)
FILL_INPUT = PatternFill("solid", fgColor="FFF2A8")  # Annahme, darf geändert werden
FILL_GOOD = PatternFill("solid", fgColor="D6ECD9")
FILL_WARN = PatternFill("solid", fgColor="FBE7C0")
FILL_BAD = PatternFill("solid", fgColor="F7D4CF")
FILL_BAND = PatternFill("solid", fgColor="EFF3F1")

THIN = Side(style="thin", color="C9D2CE")
BOX = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

CHF = '"CHF" #,##0'
CHF0 = '"CHF" #,##0;("CHF" #,##0);-'
PCT = "0%"
NUM = "#,##0"

WRAP = Alignment(wrap_text=True, vertical="top")
TOP = Alignment(vertical="top")


def head(sheet, row, labels, widths=None):
    for index, label in enumerate(labels, start=1):
        cell = sheet.cell(row=row, column=index, value=label)
        cell.font = F_HEAD
        cell.fill = FILL_HEAD
        cell.alignment = Alignment(wrap_text=True, vertical="center")
        cell.border = BOX
    sheet.row_dimensions[row].height = 28
    if widths:
        for index, width in enumerate(widths, start=1):
            sheet.column_dimensions[get_column_letter(index)].width = width


def put(sheet, row, column, value, font=F_BODY, fmt=None, fill=None, align=TOP, border=True):
    cell = sheet.cell(row=row, column=column, value=value)
    cell.font = font
    cell.alignment = align
    if fmt:
        cell.number_format = fmt
    if fill:
        cell.fill = fill
    if border:
        cell.border = BOX
    return cell


def title(sheet, text, subtitle=None):
    cell = sheet.cell(row=1, column=1, value=text)
    cell.font = F_TITLE
    if subtitle:
        sub = sheet.cell(row=2, column=1, value=subtitle)
        sub.font = F_ITAL


# ---------------------------------------------------------------- Blatt 1
def sheet_summary(book):
    s = book.create_sheet("1 Zusammenfassung")
    for column, width in zip("ABCDEF", (42, 17, 17, 17, 17, 46)):
        s.column_dimensions[column].width = width
    title(
        s,
        "Vereine als zweites Standbein",
        f"Coach Grid · Entscheidungsgrundlage · Stand {STAND}. "
        "Blau = Eingabe, alles andere rechnet sich daraus.",
    )

    s["A4"] = "Die Idee in drei Sätzen"
    s["A4"].font = F_H2
    for offset, text in enumerate(
        [
            "Heute verkaufen wir einzeln: ein Coach zahlt CHF 399 im Jahr. Ein Verein hat 10–40 Coaches auf einen Schlag.",
            "Wir verkaufen dem Verein ein Paket für alle seine Coaches — ein Vertrag, eine Rechnung, ein Ansprechpartner.",
            "Der Verein bekommt Sichtbarkeit und ein Dashboard; die Anfrage geht weiterhin an den Coach. Die Plattform bleibt eine Coach-Plattform.",
        ]
    ):
        put(s, 5 + offset, 1, text, align=WRAP, border=False)
        s.merge_cells(start_row=5 + offset, start_column=1, end_row=5 + offset, end_column=6)
        s.row_dimensions[5 + offset].height = 16

    s["A9"] = "Was dabei herausschaut (3 Jahre kumuliert)"
    s["A9"].font = F_H2
    head(s, 10, ["Szenario", "Neukunden J1", "ARR Jahr 1", "ARR Jahr 3", "Kumuliert 3 Jahre", "Was dafür wahr sein muss"])
    # Bezüge auf Blatt 4: Zeile 6 = Abschlüsse Jahr 1, 16 = ARR Jahr 1,
    # 20 = ARR Jahr 3, 21 = Umsatz 3 Jahre kumuliert.
    rows = [
        ("Vorsichtig", "='4 Szenarien'!D6", "='4 Szenarien'!D16", "='4 Szenarien'!D20", "='4 Szenarien'!D21",
         "Wir schreiben die Liste an, wenige antworten, wir landen kleine Vereine."),
        ("Realistisch", "='4 Szenarien'!E6", "='4 Szenarien'!E16", "='4 Szenarien'!E20", "='4 Szenarien'!E21",
         "Warme Ansprache statt Kaltmail, Fokus auf Golf und grosse Tennisclubs, 2 Referenzkunden."),
        ("Optimistisch", "='4 Szenarien'!F6", "='4 Szenarien'!F16", "='4 Szenarien'!F20", "='4 Szenarien'!F21",
         "Ein Verband oder ein Referenzclub öffnet die Tür, Empfehlungen tragen den Rest."),
    ]
    for offset, (name, neu, arr1, arr3, kum, bed) in enumerate(rows):
        line = 11 + offset
        put(s, line, 1, name, font=F_BOLD)
        put(s, line, 2, neu, fmt=NUM)
        put(s, line, 3, arr1, fmt=CHF)
        put(s, line, 4, arr3, fmt=CHF)
        put(s, line, 5, kum, fmt=CHF, font=F_BOLD, fill=FILL_GOOD)
        put(s, line, 6, bed, align=WRAP)
        s.row_dimensions[line].height = 30

    s["A15"] = "Die drei Punkte, die vor dem ersten Anruf entschieden sein müssen"
    s["A15"].font = F_H2
    findings = [
        ("1", "Der 10k-Preis kippt unter 25 Coaches",
         f"CHF 10'000 geteilt durch CHF {COACH_PREIS} sind 25 Coaches. Ein Verein mit 15 Coaches zahlt beim "
         "10k-Deal das 1.7-fache dessen, was seine Coaches einzeln zahlen würden — das rechnet der erste "
         "Vereinspräsident in dreissig Sekunden nach. Darum Staffelpreise nach Coach-Zahl (Blatt 2)."),
        ("2", "Wenige grosse Vereine schlagen viele kleine",
         "20 grosse Vereine à CHF 9'900 bringen gleich viel wie 200 kleine à CHF 1'000 — bei einem Zehntel "
         "Vertriebsaufwand und einem Zehntel Support. Zuerst Golf, grosse Tennisclubs und Eishockey."),
        ("3", "Die Anfrage muss beim Coach landen",
         "Leiten wir Anfragen an die Vereinsadresse um, wird aus einer Coach-Plattform ein Vereinsverzeichnis. "
         "Der Verein bekommt Sichtbarkeit, Dashboard und Kopie jeder Anfrage — die Anfrage selbst geht an den "
         "Coach. Details und Vertragsklauseln auf Blatt 6."),
    ]
    head(s, 16, ["Nr.", "Befund", "", "", "", "Begründung"])
    for offset, (num, claim, why) in enumerate(findings):
        line = 17 + offset
        put(s, line, 1, num, font=F_BOLD, align=Alignment(horizontal="center", vertical="top"))
        cell = put(s, line, 2, claim, font=F_BOLD, align=WRAP)
        s.merge_cells(start_row=line, start_column=2, end_row=line, end_column=5)
        put(s, line, 6, why, align=WRAP)
        s.row_dimensions[line].height = 58

    s["A21"] = "Empfehlung"
    s["A21"].font = F_H2
    put(
        s,
        22,
        1,
        "Pilot mit 50 Vereinen aus der bestehenden Kontaktliste (Golf und grosse Tennisclubs zuerst), "
        "Staffelpreis statt Einheitspreis, drei Referenzkunden zu Sonderkonditionen, Anfrage bleibt beim Coach. "
        "Entscheidung nach 90 Tagen anhand der Abschlussquote — Fahrplan auf Blatt 7.",
        align=WRAP,
        border=False,
    )
    s.merge_cells("A22:F22")
    s.row_dimensions[22].height = 34
    return s


# ---------------------------------------------------------------- Blatt 2
def sheet_pricing(book):
    s = book.create_sheet("2 Preismodell")
    for column, width in zip("ABCDEFGH", (26, 14, 14, 14, 15, 15, 15, 34)):
        s.column_dimensions[column].width = width
    title(
        s,
        "Preismodell",
        "Der Vereinspreis muss unter der Summe der Einzelpreise liegen — sonst ist er nicht verhandelbar.",
    )

    put(s, 4, 1, "Heutiger Einzelpreis pro Coach und Jahr", font=F_BOLD, border=False)
    put(s, 4, 2, COACH_PREIS, font=F_INPUT, fmt=CHF, fill=FILL_INPUT)
    put(s, 4, 3, "← Eingabe", font=F_ITAL, border=False)

    s["A6"] = "Staffelpreise nach Anzahl Coaches"
    s["A6"].font = F_H2
    head(
        s,
        7,
        ["Stufe", "Coaches ab", "Coaches bis", "Jahrespreis", "Preis pro Coach",
         "Rabatt vs. Einzel", "Monatspreis", "Ersparnis bei Jahreszahlung"],
    )
    tiers = [("S – kleiner Verein", 1, 10, 2490, 249), ("M – mittlerer Verein", 11, 25, 4900, 490),
             ("L – grosser Verein", 26, 40, 9900, 990), ("XL – Grossverein", 41, 80, 14900, 1490)]
    for offset, (name, low, high, year, month) in enumerate(tiers):
        line = 8 + offset
        put(s, line, 1, name, font=F_BOLD)
        put(s, line, 2, low, font=F_INPUT, fmt=NUM, fill=FILL_INPUT)
        put(s, line, 3, high, font=F_INPUT, fmt=NUM, fill=FILL_INPUT)
        put(s, line, 4, year, font=F_INPUT, fmt=CHF, fill=FILL_INPUT)
        put(s, line, 5, f"=D{line}/((B{line}+C{line})/2)", fmt=CHF)
        put(s, line, 6, f"=E{line}/$B$4-1", fmt=PCT)
        put(s, line, 7, month, font=F_INPUT, fmt=CHF, fill=FILL_INPUT)
        put(s, line, 8, f"=G{line}*12-D{line}", fmt=CHF, font=F_BOLD)

    put(s, 12, 1,
        "Der Monatspreis ist bewusst höher gerechnet: wer jährlich zahlt, spart sichtbar. "
        "Beim grossen Verein sind das CHF 1'980 — genau die Logik «CHF 990 im Monat oder CHF 9'900 im Jahr».",
        align=WRAP, border=False)
    s.merge_cells("A12:H12")
    s.row_dimensions[12].height = 30

    s["A14"] = "Gegenprobe: Vereinspreis gegen die Summe der Einzelanmeldungen"
    s["A14"].font = F_H2
    head(s, 15, ["Coaches im Verein", "Summe Einzelpreise", "Vereinspreis L (10k-Idee)",
                 "Differenz für den Verein", "Verhältnis", "Urteil", "", ""])
    counts = [5, 10, 15, 20, 25, 30, 40, 50]
    for offset, count in enumerate(counts):
        line = 16 + offset
        put(s, line, 1, count, fmt=NUM, font=F_INPUT, fill=FILL_INPUT)
        put(s, line, 2, f"=A{line}*$B$4", fmt=CHF)
        put(s, line, 3, "=$D$10", fmt=CHF)
        put(s, line, 4, f"=C{line}-B{line}", fmt=CHF0)
        put(s, line, 5, f"=C{line}/B{line}", fmt="0.00x")
        # Exakter Break-even: 10'000 / 399 = 25.06 Coaches
        if count == 25:
            verdict, fill = "Break-even (Differenz CHF 25)", FILL_WARN
        elif count * COACH_PREIS < 10000:
            verdict, fill = "Verein zahlt drauf", FILL_BAD
        else:
            verdict, fill = "Verein spart", FILL_GOOD
        put(s, line, 6, verdict, fill=fill, font=F_BOLD)

    put(s, 25, 1,
        f"Break-even liegt bei CHF 10'000 / CHF {COACH_PREIS} = 25 Coaches. Da die meisten Vereine 10–20 Coaches "
        "haben, ist der Einheitspreis von 10k für die Mehrheit ein Argument gegen uns. Mit der Staffel bleibt "
        "jede Stufe unter der Einzelsumme und der Verein spart sichtbar.",
        align=WRAP, border=False)
    s.merge_cells("A25:H25")
    s.row_dimensions[25].height = 32

    chart = BarChart()
    chart.type = "col"
    chart.title = "Vereinspreis gegen Summe der Einzelanmeldungen"
    chart.y_axis.title = "CHF pro Jahr"
    chart.x_axis.title = "Anzahl Coaches im Verein"
    chart.height, chart.width = 8.5, 20
    data = Reference(s, min_col=2, max_col=3, min_row=15, max_row=23)
    cats = Reference(s, min_col=1, min_row=16, max_row=23)
    chart.add_data(data, titles_from_data=True)
    chart.set_categories(cats)
    s.add_chart(chart, "A27")
    return s


# ---------------------------------------------------------------- Blatt 3
def sheet_market(book):
    s = book.create_sheet("3 Zielmarkt")
    for column, width in zip("ABCDEFGH", (24, 15, 15, 15, 15, 16, 18, 34)):
        s.column_dimensions[column].width = width
    title(
        s,
        "Zielmarkt",
        "Basis ist unsere eigene Kontaktliste (414 Einträge mit Telefon, Mail und Adresse) — nicht der Gesamtmarkt.",
    )

    head(s, 4, ["Sportart", "In unserer Liste", "Markt CH gesamt", "Ø Coaches pro Verein",
                "Passende Stufe", "Preis pro Jahr", "Potenzial bei 100 %", "Warum diese Priorität"])
    market = [
        ("Golf", 103, 100, 6, "S", "=INDEX('2 Preismodell'!$D$8:$D$11,1)",
         "Höchste Zahlungskraft: eigener Platz, Geschäftsführung, Marketingbudget. Wenige Pros, darum Stufe S."),
        ("Tennis", 99, 900, 12, "M", "=INDEX('2 Preismodell'!$D$8:$D$11,2)",
         "Grösste Zahl an Clubs mit eigener Anlage. Herz der Zielgruppe."),
        ("Schwimmen", 180, 175, 20, "M", "=INDEX('2 Preismodell'!$D$8:$D$11,2)",
         "Viele Trainer pro Verein und laufendes Kursgeschäft — dort wird ohnehin gesucht."),
        ("Reiten & Eishockey", 32, 450, 25, "M", "=INDEX('2 Preismodell'!$D$8:$D$11,2)",
         "Eishockey mit grossem Nachwuchsstab; Reitbetriebe meist kommerziell geführt und entscheiden schnell."),
    ]
    for offset, (sport, ours, total, coaches, tier, price, why) in enumerate(market):
        line = 5 + offset
        put(s, line, 1, sport, font=F_BOLD)
        put(s, line, 2, ours, fmt=NUM)
        put(s, line, 3, total, font=F_INPUT, fmt=NUM, fill=FILL_INPUT)
        put(s, line, 4, coaches, font=F_INPUT, fmt=NUM, fill=FILL_INPUT)
        put(s, line, 5, tier)
        put(s, line, 6, price, fmt=CHF)
        put(s, line, 7, f"=B{line}*F{line}", fmt=CHF, font=F_BOLD)
        put(s, line, 8, why, align=WRAP)
        s.row_dimensions[line].height = 42

    put(s, 9, 1, "Total", font=F_BOLD)
    put(s, 9, 2, "=SUM(B5:B8)", fmt=NUM, font=F_BOLD)
    put(s, 9, 3, "=SUM(C5:C8)", fmt=NUM, font=F_BOLD)
    put(s, 9, 7, "=SUM(G5:G8)", fmt=CHF, font=F_BOLD, fill=FILL_GOOD)
    put(s, 9, 8, "Theoretische Obergrenze, wenn jeder Verein der Liste zahlt. Nie die Planzahl.", align=WRAP)

    s["A11"] = "Vom Kontakt zum Kunden"
    s["A11"].font = F_H2
    head(s, 12, ["Stufe", "Vorsichtig", "Realistisch", "Optimistisch", "", "", "", "Bemerkung"])
    funnel = [
        ("Vereine angeschrieben", "='4 Szenarien'!D4", "='4 Szenarien'!E4", "='4 Szenarien'!F4", NUM,
         "Aus der Liste, mit Name des Ansprechpartners."),
        ("davon antworten", "='4 Szenarien'!D4*'4 Szenarien'!D5", "='4 Szenarien'!E4*'4 Szenarien'!E5",
         "='4 Szenarien'!F4*'4 Szenarien'!F5", NUM, "Antwortquote steht auf Blatt 4 und ist änderbar."),
        ("davon schliessen ab", "='4 Szenarien'!D6", "='4 Szenarien'!E6", "='4 Szenarien'!F6", NUM,
         "Kunden im ersten Jahr."),
        # Abschlüsse (Zeile 15) geteilt durch Angeschriebene (Zeile 13), je Spalte
        ("Abschlussquote gesamt", "=B15/B13", "=C15/C13", "=D15/D13", "0.0%",
         "Anteil der angeschriebenen Vereine, der unterschreibt."),
    ]
    for offset, (label, bear, base, bull, fmt, note) in enumerate(funnel):
        line = 13 + offset
        put(s, line, 1, label, font=F_BOLD)
        put(s, line, 2, bear, fmt=fmt)
        put(s, line, 3, base, fmt=fmt)
        put(s, line, 4, bull, fmt=fmt)
        put(s, line, 8, note, align=WRAP)

    chart = BarChart()
    chart.type = "col"
    chart.title = "Kontaktierbare Vereine nach Sportart"
    chart.y_axis.title = "Anzahl Vereine"
    chart.height, chart.width = 8, 16
    data = Reference(s, min_col=2, max_col=2, min_row=4, max_row=8)
    cats = Reference(s, min_col=1, min_row=5, max_row=8)
    chart.add_data(data, titles_from_data=True)
    chart.set_categories(cats)
    s.add_chart(chart, "A19")
    return s


# ---------------------------------------------------------------- Blatt 4
def sheet_scenarios(book):
    s = book.create_sheet("4 Szenarien")
    for column, width in zip("ABCDEFGH", (34, 4, 4, 16, 16, 16, 4, 44)):
        s.column_dimensions[column].width = width
    title(s, "Szenarien über drei Jahre", "Blau ist Eingabe. Alles darunter rechnet sich daraus.")

    head(s, 3, ["Treiber", "", "", "Vorsichtig", "Realistisch", "Optimistisch", "", "Bemerkung"])
    drivers = [
        ("Vereine angeschrieben (Jahr 1)", 200, 350, 414, NUM,
         "Die Liste hat 414 Einträge mit Kontaktdaten."),
        ("Antwortquote", 0.12, 0.20, 0.30, PCT,
         "Kaltmail an Vereine liegt erfahrungsgemäss bei 10–20 %; mit Telefon-Nachfassen höher. Annahme."),
        ("Abschlüsse Jahr 1", "=ROUND(D4*D5*D7,0)", "=ROUND(E4*E5*E7,0)", "=ROUND(F4*F5*F7,0)", NUM,
         "Angeschrieben × Antwortquote × Abschluss aus Antwort, auf ganze Vereine gerundet."),
        ("Abschluss aus Antwort", 0.08, 0.15, 0.25, PCT, "Annahme, im Pilot zu messen."),
        ("Ø Jahrespreis pro Verein", 2490, 4900, 6900, CHF,
         "Vorsichtig = nur Stufe S, realistisch = Stufe M, optimistisch = Mischung M und L."),
        ("Verlängerungsquote pro Jahr", 0.75, 0.85, 0.90, PCT,
         "Vertragslaufzeit 24 Monate, danach jährliche Verlängerung."),
        ("Neue Vereine Jahr 2", 8, 20, 45, NUM, "Empfehlungen und zweite Welle."),
        ("Neue Vereine Jahr 3", 10, 30, 70, NUM, "Ab hier trägt die Referenzliste."),
    ]
    for offset, (label, bear, base, bull, fmt, note) in enumerate(drivers):
        line = 4 + offset
        put(s, line, 1, label, font=F_BOLD)
        for column, value in zip((4, 5, 6), (bear, base, bull)):
            is_input = not (isinstance(value, str) and value.startswith("="))
            put(s, line, column, value, fmt=fmt,
                font=F_INPUT if is_input else F_BODY,
                fill=FILL_INPUT if is_input else None)
        put(s, line, 8, note, align=WRAP)
        s.row_dimensions[line].height = 26

    s["A13"] = "Ergebnis"
    s["A13"].font = F_H2
    head(s, 14, ["Kennzahl", "", "", "Vorsichtig", "Realistisch", "Optimistisch", "", "Bemerkung"])
    results = [
        ("Kunden Ende Jahr 1", "=D6", "=E6", "=F6", NUM, ""),
        ("ARR Jahr 1", "=D15*D8", "=E15*E8", "=F15*F8", CHF, "Wiederkehrender Jahresumsatz."),
        ("Kunden Ende Jahr 2", "=ROUND(D15*D9+D10,0)", "=ROUND(E15*E9+E10,0)", "=ROUND(F15*F9+F10,0)", NUM,
         "Bestand nach Kündigungen plus neue."),
        ("ARR Jahr 2", "=D17*D8", "=E17*E8", "=F17*F8", CHF, ""),
        ("Kunden Ende Jahr 3", "=ROUND(D17*D9+D11,0)", "=ROUND(E17*E9+E11,0)", "=ROUND(F17*F9+F11,0)", NUM, ""),
        ("ARR Jahr 3", "=D19*D8", "=E19*E8", "=F19*F8", CHF, ""),
        ("Umsatz 3 Jahre kumuliert", "=D16+D18+D20", "=E16+E18+E20", "=F16+F18+F20", CHF, "Summe der drei Jahresumsätze."),
    ]
    for offset, (label, bear, base, bull, fmt, note) in enumerate(results):
        line = 15 + offset
        bold = label.startswith("Umsatz 3")
        put(s, line, 1, label, font=F_BOLD if bold else F_BODY)
        for column, value in zip((4, 5, 6), (bear, base, bull)):
            put(s, line, column, value, fmt=fmt, font=F_BOLD if bold else F_BODY,
                fill=FILL_GOOD if bold else None)
        put(s, line, 8, note, align=WRAP)

    s["A23"] = "Gegenprobe zu den Zahlen aus dem Chat"
    s["A23"].font = F_H2
    head(s, 24, ["Behauptung", "", "", "Rechnung", "Nötige Abschlussquote", "Urteil", "", "Kommentar"])
    checks = [
        ("«200 Vereine à CHF 1'000 über 3 Jahre = CHF 600'000»", "=200*1000*3", "=200/F4",
         "Möglich, aber teuer erkauft",
         "Rechnerisch korrekt. Es braucht aber 200 Abschlüsse — knapp die Hälfte unserer ganzen Liste. "
         "Und CHF 1'000 sind 2.5 Coaches zum Einzelpreis: viel Aufwand für wenig Ertrag pro Kunde."),
        ("«10 Vereine à CHF 10'000 = CHF 100'000»", "=10*10000", "=10/F4",
         "Der bessere Weg",
         "Nur 10 Abschlüsse nötig — 2 % der Liste. Aber nur bei Vereinen ab 25 Coaches verhandelbar (Blatt 2). "
         "Realistisch sind das die grössten Eishockey- und Tennisclubs."),
    ]
    for offset, (claim, calc, rate, verdict, note) in enumerate(checks):
        line = 25 + offset
        cell = put(s, line, 1, claim, font=F_BOLD, align=WRAP)
        s.merge_cells(start_row=line, start_column=1, end_row=line, end_column=3)
        put(s, line, 4, calc, fmt=CHF)
        put(s, line, 5, rate, fmt="0.0%")
        put(s, line, 6, verdict, font=F_BOLD, fill=FILL_WARN if offset == 0 else FILL_GOOD)
        put(s, line, 8, note, align=WRAP)
        s.row_dimensions[line].height = 46

    # Eigener Datenblock fürs Diagramm: nur die Franken-Zeilen, sonst wären die
    # Kundenzahlen neben den CHF-Werten als Balken unsichtbar.
    put(s, 29, 1, "Diagrammdaten (verweisen auf die Ergebnisse oben)", font=F_H2, border=False)
    head(s, 30, ["", "", "", "Vorsichtig", "Realistisch", "Optimistisch", "", ""])
    for offset, (label, source) in enumerate(
        [("ARR Jahr 1", 16), ("ARR Jahr 2", 18), ("ARR Jahr 3", 20)]
    ):
        line = 31 + offset
        put(s, line, 1, label, font=F_BOLD)
        for column in (4, 5, 6):
            put(s, line, column, f"={get_column_letter(column)}{source}", fmt=CHF)

    chart = BarChart()
    chart.type = "col"
    chart.title = "Wiederkehrender Umsatz (ARR) je Szenario"
    chart.y_axis.title = "CHF"
    chart.height, chart.width = 9, 20
    data = Reference(s, min_col=4, max_col=6, min_row=30, max_row=33)
    cats = Reference(s, min_col=1, min_row=31, max_row=33)
    chart.add_data(data, titles_from_data=True)
    chart.set_categories(cats)
    s.add_chart(chart, "A35")
    return s


# ---------------------------------------------------------------- Blatt 5
def sheet_sensitivity(book):
    s = book.create_sheet("5 Sensitivität")
    for column, width in zip("ABCDEFGH", (26, 14, 14, 14, 14, 14, 14, 40)):
        s.column_dimensions[column].width = width
    title(s, "Sensitivität", "Wiederkehrender Jahresumsatz je Kombination aus Preis und Anzahl Kunden.")

    prices = [1000, 2490, 4900, 6900, 9900, 14900]
    counts = [5, 10, 20, 30, 50, 80, 120, 200]

    put(s, 4, 1, "Kunden ↓ / Preis →", font=F_HEAD, fill=FILL_HEAD)
    for index, price in enumerate(prices):
        put(s, 4, 2 + index, price, font=F_HEAD, fill=FILL_HEAD, fmt=CHF)
    for row_index, count in enumerate(counts):
        line = 5 + row_index
        put(s, line, 1, count, font=F_HEAD, fill=FILL_HEAD, fmt=NUM)
        for col_index in range(len(prices)):
            column = 2 + col_index
            letter = get_column_letter(column)
            cell = put(s, line, column, f"=$A{line}*{letter}$4", fmt=CHF)
            if count * prices[col_index] >= 200000:
                cell.fill = FILL_GOOD
            elif count * prices[col_index] >= 100000:
                cell.fill = FILL_WARN
            elif count * prices[col_index] < 30000:
                cell.fill = FILL_BAND

    put(s, 14, 1,
        "Grün ab CHF 200'000 wiederkehrend, orange ab CHF 100'000. Die gleiche Zelle erreicht man auf zwei Wegen: "
        "200 kleine Kunden zu CHF 1'000 oder 20 grosse zu CHF 9'900. Beides ergibt rund CHF 200'000 — der zweite "
        "Weg kostet ein Zehntel des Vertriebsaufwands. Das ist das eigentliche Argument für die Staffel.",
        align=WRAP, border=False)
    s.merge_cells("A14:H14")
    s.row_dimensions[14].height = 44
    return s


# ---------------------------------------------------------------- Blatt 6
def sheet_conflict(book):
    s = book.create_sheet("6 Konflikt & Lösung")
    for column, width in zip("ABCDE", (26, 40, 40, 40, 30)):
        s.column_dimensions[column].width = width
    title(
        s,
        "Der Zielkonflikt — und wie wir ihn auflösen",
        "Der Verein zahlt, weil er etwas davon hat. Die Plattform lebt davon, dass es um den Coach geht.",
    )

    s["A4"] = "Das Problem in einem Satz"
    s["A4"].font = F_H2
    put(s, 5, 1,
        "Ein Verein zahlt nur, wenn er den Nutzen sieht — der Nutzen ist die Anfrage. Leiten wir Anfragen an die "
        "Vereinsadresse, wird aus der Coach-Plattform ein Vereinsverzeichnis, und die Coaches verlieren den Grund, "
        "bei uns zu sein.",
        align=WRAP, border=False)
    s.merge_cells("A5:E5")
    s.row_dimensions[5].height = 32

    head(s, 7, ["Modell", "Wie es läuft", "Spricht dafür", "Spricht dagegen", "Urteil"])
    options = [
        ("A — Anfrage an den Verein",
         "Coach-Profile bleiben sichtbar, aber jeder Kontaktbutton führt zur Vereinsadresse.",
         "Für den Verein die einfachste Zusage: er behält die Kundenbeziehung vollständig.",
         "Bricht das Versprechen der Plattform. Coaches werden zu Karteikarten und wandern ab. "
         "Der Kunde erwartet den Coach, den er angeschrieben hat, und bekommt eine Zentrale.",
         "Nicht empfohlen"),
        ("B — Anfrage nur an den Coach",
         "Alles bleibt wie heute, der Verein zahlt für Sichtbarkeit und sein Logo auf den Profilen.",
         "Philosophie bleibt unangetastet, kein Bruch im Produkt.",
         "Der Verein fragt zu Recht: wofür zahle ich? Ohne sichtbaren Rücklauf keine Verlängerung.",
         "Zu wenig für den Verein"),
        ("C — Anfrage an den Coach, Verein in Kopie",
         "Die Anfrage geht an den Coach. Der Verein erhält automatisch eine Kopie und sieht im Dashboard "
         "alle Anfragen, Buchungen und Auslastung seiner Coaches.",
         "Der Coach bleibt der Ansprechpartner — Versprechen gehalten. Der Verein sieht schwarz auf weiss, "
         "was das Abo bringt, und behält die Kontrolle über seine Coaches.",
         "Etwas Entwicklungsaufwand: Vereinskonto, Dashboard, Kopie-Zustellung.",
         "Empfehlung"),
    ]
    for offset, row in enumerate(options):
        line = 8 + offset
        for column, value in enumerate(row, start=1):
            fill = None
            if column == 5:
                fill = {"Empfehlung": FILL_GOOD, "Nicht empfohlen": FILL_BAD}.get(value, FILL_WARN)
            put(s, line, column, value, align=WRAP,
                font=F_BOLD if column in (1, 5) else F_BODY, fill=fill)
        s.row_dimensions[line].height = 76

    s["A12"] = "Die vier Einwände, die im Gespräch garantiert kommen"
    s["A12"].font = F_H2
    head(s, 13, ["Einwand", "Antwort", "Regelung im Vertrag", "", ""])
    objections = [
        ("«Dann melden sich unsere Coaches einfach privat an und wir zahlen umsonst.»",
         "Solange der Verein zahlt, läuft der Coach über den Vereinscode. Ein zweites Privatprofil ist nur mit "
         "Freigabe des Vereins möglich.",
         "Vereinscodes pro Coach; keine Doppellistung ohne Freigabe; Code erlischt beim Vereinsaustritt."),
        ("«Privatlektionen sind billiger, dann bucht niemand mehr über uns.»",
         "In Tennis, Schwimmen und Ski ist die Privatlektion regelmässig teurer als das Vereinsangebot — sie ist "
         "die Zusatzleistung, nicht die günstigere Alternative.",
         "Preisuntergrenze: Privatlektionen eines Vereinscoaches liegen mindestens auf Vereinsniveau."),
        ("«Was, wenn ein Coach den Verein verlässt?»",
         "Sein Zugang wird deaktiviert, das Profil verschwindet aus dem Vereinspaket. Der Verein zahlt nie für "
         "jemanden, der nicht mehr da ist.",
         "Codes monatlich abrechenbar; Deaktivierung innert 5 Werktagen; Meldepflicht des Vereins."),
        ("«Könnt ihr uns Kunden garantieren?»",
         "Nein — und das sagen wir offen. Wir erhöhen die Wahrscheinlichkeit, gefunden zu werden, weil wir "
         "Marketing und Sichtbarkeit übernehmen. Eine Zusage auf Kundenzahlen macht niemand seriös.",
         "Keine Erfolgsgarantie im Vertrag. Stattdessen: Reporting und Ausstieg nach 24 Monaten."),
    ]
    for offset, (obj, answer, clause) in enumerate(objections):
        line = 14 + offset
        put(s, line, 1, obj, font=F_BOLD, align=WRAP)
        put(s, line, 2, answer, align=WRAP)
        cell = put(s, line, 3, clause, align=WRAP)
        s.merge_cells(start_row=line, start_column=3, end_row=line, end_column=5)
        s.row_dimensions[line].height = 62
    return s


# ---------------------------------------------------------------- Blatt 7
def sheet_roadmap(book):
    s = book.create_sheet("7 Fahrplan 90 Tage")
    for column, width in zip("ABCDEF", (14, 34, 44, 18, 26, 26)):
        s.column_dimensions[column].width = width
    title(s, "Fahrplan über 90 Tage", "Ziel: nach drei Monaten wissen wir, ob das Modell trägt — mit Zahlen statt Meinung.")

    head(s, 4, ["Zeitraum", "Schritt", "Was konkret passiert", "Verantwortlich", "Fertig wenn", "Messgrösse"])
    steps = [
        ("Woche 1–2", "Angebot fertig machen",
         "Staffelpreise festlegen, Vertragsentwurf mit Codes und Preisuntergrenze, eine Seite für Vereine auf der Website.",
         "Robert / Navid", "Vertrag und Preisliste stehen", "—"),
        ("Woche 2", "Zielliste schneiden",
         "Aus den 414 Kontakten die 50 aussichtsreichsten ziehen: Golf und grosse Tennisclubs mit Mailadresse.",
         "Navid", "Liste mit 50 Vereinen steht", "50 Kontakte"),
        ("Woche 3–4", "Erste Welle",
         "50 Vereine anschreiben, nach 4 Tagen telefonisch nachfassen. Gleiche Botschaft wie bei Coaches: mehr Sichtbarkeit, keine Garantie.",
         "Navid", "50 angeschrieben, 50 nachgefasst", "Antwortquote"),
        ("Woche 5–8", "Gespräche führen",
         "Termine wahrnehmen, Blatt 2 und 6 als Gesprächsgrundlage nutzen, Einwände sauber beantworten.",
         "Robert", "mindestens 8 Termine", "Termine pro 50 Kontakte"),
        ("Woche 6–10", "Drei Piloten gewinnen",
         "Drei Vereine zu Sonderkonditionen: erstes Jahr halber Preis gegen das Recht, sie als Referenz zu nennen.",
         "Robert / Navid", "3 unterschriebene Verträge", "Abschlussquote"),
        ("Woche 9–12", "Belegen und entscheiden",
         "Anfragen pro Pilotverein messen, eine Fallstudie schreiben, Preis fixieren oder Modell verwerfen.",
         "Navid", "Fallstudie liegt vor", "Anfragen pro Verein und Monat"),
    ]
    for offset, row in enumerate(steps):
        line = 5 + offset
        for column, value in enumerate(row, start=1):
            put(s, line, column, value, align=WRAP, font=F_BOLD if column == 1 else F_BODY)
        s.row_dimensions[line].height = 52

    s["A12"] = "Abbruchkriterien — wann wir das Modell wieder einpacken"
    s["A12"].font = F_H2
    for offset, text in enumerate([
        "Unter 8 % Antwortquote auf 50 saubere Kontakte: die Botschaft stimmt nicht, nicht der Markt.",
        "Null Abschlüsse nach 10 geführten Gesprächen: der Preis oder das Modell trägt nicht.",
        "Weniger als 2 Anfragen pro Pilotverein und Monat: der Verein verlängert nicht, egal wie gut das Gespräch war.",
    ]):
        put(s, 13 + offset, 1, "• " + text, align=WRAP, border=False)
        s.merge_cells(start_row=13 + offset, start_column=1, end_row=13 + offset, end_column=6)
    return s


# ---------------------------------------------------------------- Blatt 8
def sheet_assumptions(book):
    s = book.create_sheet("8 Annahmen & Quellen")
    for column, width in zip("ABCD", (40, 20, 26, 62)):
        s.column_dimensions[column].width = width
    title(s, "Annahmen und Quellen", "Was gemessen ist, was geschätzt ist, und woher es kommt.")

    head(s, 4, ["Annahme", "Wert", "Art", "Herkunft"])
    items = [
        ("Einzelpreis pro Coach und Jahr", "CHF 399", "gesetzt", "Von euch genannt (Chat vom 29.07.2026)."),
        ("Coaches pro Verein", "10–20, teils 40+", "eure Beobachtung",
         "Von euch genannt. Für Golf eher tief (3–8 Pros), für Eishockey und Schwimmen eher hoch — darum auf Blatt 3 pro Sportart änderbar."),
        ("Kontaktierbare Vereine", "414", "gemessen",
         "Eigene Liste vom 28.07.2026: Golf 103, Tennis 99, Schwimmen 180, Reiten und Eishockey 32."),
        ("Vereine im Markt CH", "rund 1'600 mit eigener Anlage", "recherchiert",
         "Swiss Tennis rund 900 Clubs, Swiss Golf über 90, Swiss Aquatics 175, Eishockey und Reitbetriebe geschätzt."),
        ("Sportvereine CH gesamt", "18'310 mit 2.2 Mio. Mitgliedschaften", "recherchiert",
         "Vereinsstudie 2022, Swiss Olympic."),
        ("Ø Einnahmen eines Sportvereins", "CHF 69'000 pro Jahr", "recherchiert",
         "Observatorium Sport und Bewegung Schweiz. Wichtig fürs Preisgespräch: ein 10k-Abo wäre bei einem "
         "Durchschnittsverein 14 % des gesamten Jahresbudgets."),
        ("Vereine ohne bezahlte Mitarbeitende", "82 %", "recherchiert",
         "Vereinsstudie 2022. Deshalb Staffelpreise statt Einheitspreis."),
        ("Antwortquote auf Kaltmail", "12 / 20 / 30 %", "Annahme",
         "Erfahrungswert B2B mit telefonischem Nachfassen. Im Pilot zu messen, nicht belegt."),
        ("Abschluss aus Antwort", "8 / 15 / 25 %", "Annahme", "Erfahrungswert. Im Pilot zu messen, nicht belegt."),
        ("Verlängerungsquote", "75 / 85 / 90 %", "Annahme", "Bei 24 Monaten Laufzeit. Nicht belegt."),
    ]
    for offset, row in enumerate(items):
        line = 5 + offset
        for column, value in enumerate(row, start=1):
            fill = None
            if column == 3:
                fill = {"gemessen": FILL_GOOD, "recherchiert": FILL_BAND, "Annahme": FILL_WARN}.get(value)
            put(s, line, column, value, align=WRAP, font=F_BOLD if column == 1 else F_BODY, fill=fill)
        s.row_dimensions[line].height = 40

    s["A17"] = "Quellen"
    s["A17"].font = F_H2
    links = [
        ("Vereinsstudie 2022, Swiss Olympic",
         "https://www.swissolympic.ch/dam/jcr:e13bfb8d-92a6-41a3-89e4-b80d30c2d23c/Vereinsstudie%202022_DE_Web.pdf"),
        ("Vereinsfinanzen, Sportobservatorium",
         "https://www.sportobs.ch/inhalte/Indikatoren_PDF_neu/Ind_22_Sportobs.pdf"),
        ("Swiss Aquatics, Mitgliedvereine",
         "https://www.swiss-aquatics.ch/verband/mitglieder/alle-mitgliedvereine/"),
        ("Swiss Tennis", "https://www.swisstennis.ch/de/"),
        ("Swiss Golf", "https://www.swissgolf.ch/"),
    ]
    for offset, (label, url) in enumerate(links):
        line = 18 + offset
        put(s, line, 1, label, border=False)
        cell = put(s, line, 2, url, font=F_LINK, border=False)
        cell.hyperlink = url
        s.merge_cells(start_row=line, start_column=2, end_row=line, end_column=4)

    put(s, 24, 1,
        "Alles in der Spalte «Annahme» ist noch nicht belegt. Diese vier Zahlen entscheiden über das ganze Modell — "
        "der 90-Tage-Pilot dient in erster Linie dazu, sie durch gemessene Werte zu ersetzen.",
        align=WRAP, border=False)
    s.merge_cells("A24:D24")
    s.row_dimensions[24].height = 30
    return s


def main():
    book = Workbook()
    book.remove(book.active)

    sheet_summary(book)
    sheet_pricing(book)
    sheet_market(book)
    sheet_scenarios(book)
    sheet_sensitivity(book)
    sheet_conflict(book)
    sheet_roadmap(book)
    sheet_assumptions(book)

    # Excel soll beim Öffnen selbst rechnen — openpyxl legt keine Werte ab.
    book.calculation.fullCalcOnLoad = True
    book.save(OUT)
    print(f"gebaut -> {OUT}")
    print("Blätter:", ", ".join(book.sheetnames))


if __name__ == "__main__":
    main()
