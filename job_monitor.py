#!/usr/bin/env python3
"""
Automatischer Job-Monitor für Navid Forouzeh
VEREINFACHTE VERSION - funktioniert ohne Datenbank
"""

import requests
import os
from datetime import datetime

# Telegram Config
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

def send_telegram(message):
    """Sendet Telegram-Nachricht"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }
    try:
        response = requests.post(url, json=payload, timeout=10)
        if response.status_code == 200:
            print("✅ Telegram-Nachricht gesendet")
            return True
        else:
            print(f"❌ Telegram-Fehler: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Fehler: {e}")
        return False

def main():
    print(f"🔍 Job-Suche gestartet ({datetime.now().strftime('%d.%m.%Y %H:%M')})")
    
    # Test-Nachricht
    message = f"""🎯 *Job Monitor aktiv!*

Dein automatischer Job-Monitor läuft jetzt!

✅ Sucht 2x täglich nach Jobs
✅ Filtert nach: Teilzeit, Zürich, Finance/Banking/Consulting
✅ Sendet dir nur neue, relevante Jobs

_Erste echte Suche erfolgt in Kürze..._

Test um {datetime.now().strftime('%d.%m.%Y %H:%M')} Uhr"""
    
    success = send_telegram(message)
    
    if success:
        print("✅ Setup erfolgreich!")
    else:
        print("❌ Setup fehlgeschlagen - prüfe deine Secrets!")

if __name__ == "__main__":
    main()
