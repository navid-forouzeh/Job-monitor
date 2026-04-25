#!/usr/bin/env python3
"""
Lokaler Test des Job-Monitors
Setzt Umgebungsvariablen und führt das Script aus
"""

import os
import sys

# Test-Modus: Setze diese Werte für lokalen Test
# WICHTIG: Ersetze diese mit deinen echten Werten!
os.environ['TELEGRAM_BOT_TOKEN'] = 'DEIN_BOT_TOKEN_HIER'
os.environ['TELEGRAM_CHAT_ID'] = 'DEINE_CHAT_ID_HIER'

# Importiere und starte den Job Monitor
from job_monitor import JobMonitor

if __name__ == "__main__":
    print("🧪 Test-Modus")
    print("=" * 50)
    
    if os.environ['TELEGRAM_BOT_TOKEN'] == 'DEIN_BOT_TOKEN_HIER':
        print("❌ FEHLER: Bitte setze TELEGRAM_BOT_TOKEN in test_local.py")
        sys.exit(1)
    
    if os.environ['TELEGRAM_CHAT_ID'] == 'DEINE_CHAT_ID_HIER':
        print("❌ FEHLER: Bitte setze TELEGRAM_CHAT_ID in test_local.py")
        sys.exit(1)
    
    print("✅ Umgebungsvariablen gesetzt")
    print("🔍 Starte Job-Suche...\n")
    
    monitor = JobMonitor()
    monitor.run()
    
    print("\n✅ Test abgeschlossen!")
