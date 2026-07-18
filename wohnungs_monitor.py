#!/usr/bin/env python3
"""
Automatischer Wohnungs-Monitor für Max
Sucht Mietwohnungen in der Stadt Zürich (CHF 2'500 - 3'000)
und meldet neue Inserate via Telegram.

Quellen: Flatfox API (öffentlich), Homegate-Suchlinks als Fallback im Alert.
"""

import requests
import os
from datetime import datetime

# Telegram Config (gleiche Secrets wie der Job-Monitor)
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

# Suchkriterien für Max
MIN_MIETE = 2500
MAX_MIETE = 3000

# Bounding Box der Stadt Zürich (von der Flatfox-Suche übernommen)
STADT_ZUERICH_BBOX = {
    'west': 8.494968,
    'east': 8.578462,
    'south': 47.307519,
    'north': 47.447360,
}

# PLZ der Stadt Zürich (8001-8064 sind Stadtkreise, 8000 generisch)
STADT_PLZ = {
    '8000', '8001', '8002', '8003', '8004', '8005', '8006', '8008',
    '8032', '8037', '8038', '8041', '8044', '8045', '8046', '8047',
    '8048', '8049', '8050', '8051', '8052', '8053', '8055', '8057',
    '8064',
}

FLATFOX_API = "https://flatfox.ch/api/v1/public-listing/"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'application/json',
}


class WohnungsMonitor:
    def __init__(self):
        self.seen_file = "seen_wohnungen.txt"
        self.seen = self.load_seen()

    def load_seen(self):
        if os.path.exists(self.seen_file):
            try:
                with open(self.seen_file, 'r') as f:
                    return set(line.strip() for line in f)
            except Exception:
                return set()
        return set()

    def save_seen(self, listing_id):
        if listing_id not in self.seen:
            self.seen.add(listing_id)
            try:
                with open(self.seen_file, 'a') as f:
                    f.write(f"{listing_id}\n")
            except Exception:
                pass

    def search_flatfox(self):
        """Durchsucht die öffentliche Flatfox-API nach Wohnungen in der Stadt Zürich"""
        wohnungen = []

        params = {
            'status': 'active',
            'offer_type': 'RENT',
            'object_category': 'APARTMENT',
            'max_price': MAX_MIETE,
            'min_price': MIN_MIETE,
            'ordering': '-created',
            'limit': 100,
            **STADT_ZUERICH_BBOX,
        }

        try:
            response = requests.get(FLATFOX_API, params=params, headers=HEADERS, timeout=20)

            if response.status_code != 200:
                print(f"  ⚠️ Flatfox HTTP {response.status_code}")
                return wohnungen

            data = response.json()
            results = data.get('results', data if isinstance(data, list) else [])

            for item in results:
                pk = item.get('pk') or item.get('id')
                if pk is None:
                    continue

                zipcode = str(item.get('zipcode') or '')
                city = (item.get('city') or '')
                price = item.get('price_display') or item.get('rent_gross') or item.get('price')
                rooms = item.get('number_of_rooms')
                street = item.get('street') or ''
                surface = item.get('surface_living') or item.get('living_space')
                url = item.get('url') or item.get('short_url') or f"https://flatfox.ch/de/flat/{pk}/"
                if url.startswith('/'):
                    url = f"https://flatfox.ch{url}"

                # Nur Stadt Zürich (PLZ-Check; Bounding Box allein reicht nicht)
                if zipcode and zipcode not in STADT_PLZ:
                    continue
                if not zipcode and 'zürich' not in city.lower():
                    continue

                # Preis-Check falls die API den Filter ignoriert
                try:
                    price_num = int(price)
                    if price_num < MIN_MIETE or price_num > MAX_MIETE:
                        continue
                except (TypeError, ValueError):
                    price_num = None

                wohnungen.append({
                    'id': f"flatfox_{pk}",
                    'titel': f"{rooms} Zi." if rooms else "Wohnung",
                    'adresse': f"{street}, {zipcode} {city}".strip(', '),
                    'miete': price_num or price or '?',
                    'flaeche': surface,
                    'url': url,
                    'quelle': 'Flatfox',
                })

            print(f"  → Flatfox: {len(wohnungen)} Wohnungen in der Stadt Zürich")

        except Exception as e:
            print(f"  ⚠️ Flatfox Fehler: {e}")

        return wohnungen

    def send_telegram(self, wohnungen):
        """Sendet Telegram-Nachricht mit neuen Wohnungen"""
        if not BOT_TOKEN or not CHAT_ID:
            print("⚠️ Telegram-Secrets fehlen (TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID)")
            return

        message = f"🏠 *{len(wohnungen)} neue Wohnungen für Max in Zürich!*\n"
        message += f"_(CHF {MIN_MIETE}-{MAX_MIETE}, Stadt Zürich)_\n\n"

        for i, w in enumerate(wohnungen[:8], 1):
            flaeche = f", {w['flaeche']} m²" if w.get('flaeche') else ""
            message += f"{i}. *{w['titel']}{flaeche} - CHF {w['miete']}*\n"
            message += f"   📍 {w['adresse']}\n"
            message += f"   🔗 [Zum Inserat]({w['url']})\n\n"

        if len(wohnungen) > 8:
            message += f"_... und {len(wohnungen) - 8} weitere_\n\n"

        message += (
            "🔎 Weitere Portale manuell checken:\n"
            "• [Homegate](https://www.homegate.ch/mieten/wohnung/ort-zuerich/trefferliste?ag=2500&ah=3000)\n"
            "• [ImmoScout24](https://www.immoscout24.ch/de/wohnung/mieten/ort-zuerich?pf=2500&pt=3000)\n"
        )
        message += f"\n_Suche vom {datetime.now().strftime('%d.%m.%Y %H:%M')}_"

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            'chat_id': CHAT_ID,
            'text': message,
            'parse_mode': 'Markdown',
            'disable_web_page_preview': True,
        }

        try:
            response = requests.post(url, json=payload, timeout=10)
            if response.status_code == 200:
                print(f"✅ Telegram: {len(wohnungen)} Wohnungen gesendet")
            else:
                print(f"❌ Telegram Fehler: {response.status_code} {response.text[:200]}")
        except Exception as e:
            print(f"❌ Telegram Fehler: {e}")

    def run(self):
        print(f"🏠 Wohnungssuche für Max gestartet ({datetime.now().strftime('%d.%m.%Y %H:%M')})")
        print(f"   Kriterien: Stadt Zürich, CHF {MIN_MIETE}-{MAX_MIETE}")

        alle = self.search_flatfox()
        print(f"✅ {len(alle)} Wohnungen insgesamt")

        neue = []
        for w in alle:
            if w['id'] not in self.seen:
                neue.append(w)
                self.save_seen(w['id'])

        print(f"🆕 {len(neue)} neue Wohnungen")

        if neue:
            self.send_telegram(neue)
        else:
            print("ℹ️ Keine neuen Wohnungen - keine Nachricht")


if __name__ == "__main__":
    monitor = WohnungsMonitor()
    monitor.run()
