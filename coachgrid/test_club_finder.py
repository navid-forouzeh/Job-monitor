#!/usr/bin/env python3
"""Offline-Tests für den Vereins-Finder (keine Netzwerkabfragen)."""

import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from club_finder import (  # noqa: E402
    SEGMENTS,
    build_query,
    dedupe,
    normalize_name,
    parse,
    resolve_sports,
    summarize,
    write_output,
)

FIXTURE = {
    "elements": [
        {
            "type": "way",
            "id": 1,
            "center": {"lat": 47.37, "lon": 8.54},
            "tags": {
                "name": "Tennisclub Musterhausen",
                "club": "sport",
                "sport": "tennis",
                "leisure": "sports_centre",
                "website": "https://www.tc-musterhausen.ch",
                "contact:email": "info@tc-musterhausen.ch",
                "addr:street": "Sportweg",
                "addr:housenumber": "5",
                "addr:postcode": "8000",
                "addr:city": "Zürich",
            },
        },
        {
            # Gleicher Club, in OSM zusätzlich als Platz erfasst → Duplikat
            "type": "way",
            "id": 2,
            "center": {"lat": 47.3701, "lon": 8.5401},
            "tags": {
                "name": "TC Musterhausen",
                "leisure": "pitch",
                "sport": "tennis",
                "addr:postcode": "8000",
                "phone": "+41 44 000 00 00",
            },
        },
        {
            "type": "node",
            "id": 3,
            "lat": 46.5,
            "lon": 6.6,
            "tags": {"name": "Tennisclub Ohne Kontakt", "club": "sport", "sport": "tennis"},
        },
        {
            # Ohne Namen → wird ignoriert
            "type": "node",
            "id": 4,
            "lat": 46.0,
            "lon": 7.0,
            "tags": {"club": "sport", "sport": "tennis"},
        },
    ]
}


class TestQuery(unittest.TestCase):
    def test_schweiz_query_nutzt_landesgrenze(self):
        query = build_query(SEGMENTS["golf"])
        self.assertIn('area["ISO3166-1"="CH"][admin_level=2]->.search;', query)
        self.assertIn('nwr["leisure"="golf_course"](area.search);', query)

    def test_gebiets_query(self):
        query = build_query(SEGMENTS["tennis"], area_name="Kanton Zürich")
        self.assertIn('area["name"="Kanton Zürich"]->.search;', query)

    def test_alle_sportarten_aufloesbar(self):
        self.assertEqual(len(resolve_sports("all")), len(SEGMENTS))
        self.assertEqual([s.key for s in resolve_sports("tennis,golf")], ["tennis", "golf"])
        with self.assertRaises(SystemExit):
            resolve_sports("quidditch")


class TestParse(unittest.TestCase):
    def setUp(self):
        self.clubs = parse(FIXTURE, SEGMENTS["tennis"])

    def test_namenlose_eintraege_fallen_raus(self):
        self.assertEqual(len(self.clubs), 3)

    def test_kontaktfelder(self):
        club = self.clubs[0]
        self.assertEqual(club.website, "https://www.tc-musterhausen.ch")
        self.assertEqual(club.email, "info@tc-musterhausen.ch")
        self.assertEqual(club.street, "Sportweg 5")
        self.assertEqual(club.city, "Zürich")

    def test_score_belohnt_kontakt_und_anlage(self):
        mit_kontakt, ohne_kontakt = self.clubs[0], self.clubs[2]
        self.assertGreater(mit_kontakt.budget_score, ohne_kontakt.budget_score)
        self.assertIn("eigene_anlage", mit_kontakt.signals)

    def test_golf_loecher_zaehlen(self):
        payload = {
            "elements": [
                {
                    "type": "way",
                    "id": 9,
                    "center": {"lat": 47.0, "lon": 8.0},
                    "tags": {
                        "name": "Golfclub Beispiel",
                        "leisure": "golf_course",
                        "golf:holes": "18",
                        "website": "https://gc-beispiel.ch",
                    },
                }
            ]
        }
        club = parse(payload, SEGMENTS["golf"])[0]
        self.assertIn("golf_18_loecher", club.signals)
        self.assertGreaterEqual(club.budget_score, 7)


class TestDedupe(unittest.TestCase):
    def test_namensnormalisierung(self):
        self.assertEqual(
            normalize_name("Tennisclub Musterhausen"), normalize_name("TC  Musterhausen!")
        )

    def test_duplikat_wird_zusammengefuehrt(self):
        unique = dedupe(parse(FIXTURE, SEGMENTS["tennis"]))
        self.assertEqual(len(unique), 2)
        merged = next(c for c in unique if "Musterhausen" in c.name)
        # Telefonnummer stammt aus dem Duplikat-Eintrag
        self.assertEqual(merged.phone, "+41 44 000 00 00")
        self.assertEqual(merged.email, "info@tc-musterhausen.ch")


class TestOutput(unittest.TestCase):
    def test_csv_und_json_werden_geschrieben(self):
        clubs = dedupe(parse(FIXTURE, SEGMENTS["tennis"]))
        with tempfile.TemporaryDirectory() as tmp:
            csv_path, json_path = write_output(clubs, os.path.join(tmp, "sub", "vereine"))
            self.assertTrue(os.path.exists(csv_path))
            with open(csv_path, encoding="utf-8") as handle:
                header = handle.readline()
            self.assertIn("budget_score", header)
            with open(json_path, encoding="utf-8") as handle:
                data = json.load(handle)
            self.assertEqual(len(data), len(clubs))
            self.assertTrue(data[0]["osm_url"].startswith("https://www.openstreetmap.org/"))

    def test_statistik(self):
        stats = summarize(dedupe(parse(FIXTURE, SEGMENTS["tennis"])))
        self.assertEqual(stats["Tennis"]["total"], 2)
        self.assertEqual(stats["Tennis"]["web"], 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
