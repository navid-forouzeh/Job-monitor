# 🎯 Job Monitor für Navid Forouzeh

Automatisches Job-Monitoring-System, das täglich nach relevanten Teilzeitstellen in Zürich sucht (Finance/Banking/Consulting) und dich via Telegram benachrichtigt.

## ✨ Features

- 🔍 **Automatische Suche** auf Indeed, jobs.ch und LinkedIn
- 📱 **Telegram-Benachrichtigungen** bei neuen Jobs
- 🎯 **Smart Filtering** nach deinem Profil (Teilzeit, Zürich, Finance/Banking/Consulting)
- ⏰ **Läuft 2x täglich** (08:00 und 18:00 Uhr Schweizer Zeit)
- 💾 **Duplikat-Erkennung** (keine doppelten Jobs)
- ☁️ **Komplett kostenlos** (läuft auf GitHub Actions)

## 🚀 Setup-Anleitung (15 Minuten)

### Schritt 1: Telegram Bot erstellen

1. Öffne Telegram und suche nach **@BotFather**
2. Starte einen Chat und schicke: `/newbot`
3. Folge den Anweisungen:
   - Bot-Name: `Navid Job Monitor`
   - Bot-Username: `navid_job_monitor_bot` (muss mit `_bot` enden)
4. BotFather gibt dir einen **Token** (sieht aus wie `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`)
5. **WICHTIG:** Speichere diesen Token irgendwo ab!

### Schritt 2: Chat ID herausfinden

1. Suche in Telegram nach deinem neuen Bot (`@navid_job_monitor_bot`)
2. Klicke auf **Start** und schicke eine beliebige Nachricht (z.B. "Hallo")
3. Öffne im Browser: `https://api.telegram.org/bot<DEIN_BOT_TOKEN>/getUpdates`
   - Ersetze `<DEIN_BOT_TOKEN>` mit dem Token aus Schritt 1
4. Du siehst ein JSON-Objekt. Suche nach `"chat":{"id":123456789`
5. Die Zahl ist deine **Chat ID** (z.B. `123456789`)
6. **WICHTIG:** Speichere diese Chat ID!

### Schritt 3: GitHub Repository erstellen

1. Gehe zu [GitHub](https://github.com) und melde dich an
2. Klicke auf **New Repository** (grüner Button oben rechts)
3. Repository-Name: `job-monitor`
4. Wähle **Public** (kostenlos) oder **Private** (braucht GitHub Pro)
5. Klicke auf **Create Repository**

### Schritt 4: Code hochladen

**Option A: Via GitHub Web-Interface (einfacher)**

1. In deinem neuen Repository, klicke auf **uploading an existing file**
2. Ziehe alle Dateien aus diesem Ordner rein:
   - `job_monitor.py`
   - `requirements.txt`
   - `.github/workflows/job_monitor.yml`
   - `README.md`
3. Klicke auf **Commit changes**

**Option B: Via Git (fortgeschritten)**

```bash
cd /pfad/zu/diesem/ordner
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/DEIN_USERNAME/job-monitor.git
git push -u origin main
```

### Schritt 5: GitHub Secrets einrichten

1. Gehe zu deinem Repository auf GitHub
2. Klicke auf **Settings** (oben rechts)
3. Klicke links auf **Secrets and variables** → **Actions**
4. Klicke auf **New repository secret**
5. Erstelle 2 Secrets:

**Secret 1:**
- Name: `TELEGRAM_BOT_TOKEN`
- Value: Dein Bot-Token aus Schritt 1 (z.B. `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`)
- Klicke auf **Add secret**

**Secret 2:**
- Name: `TELEGRAM_CHAT_ID`
- Value: Deine Chat ID aus Schritt 2 (z.B. `123456789`)
- Klicke auf **Add secret**

### Schritt 6: GitHub Actions aktivieren

1. Gehe zu deinem Repository
2. Klicke auf **Actions** (obere Navigation)
3. Klicke auf **I understand my workflows, go ahead and enable them**
4. Du siehst jetzt den Workflow "Job Monitor"

### Schritt 7: Test ausführen

1. In **Actions**, klicke auf den Workflow "Job Monitor"
2. Klicke rechts auf **Run workflow** → **Run workflow**
3. Warte ca. 1-2 Minuten
4. Du solltest eine Telegram-Nachricht bekommen! 🎉

## 📊 Wie es funktioniert

- **Automatische Ausführung:** Jeden Tag um 08:00 und 18:00 Uhr (Schweizer Zeit)
- **Manuelle Ausführung:** Jederzeit via GitHub Actions
- **Suchkriterien:**
  - Keywords: finance, banking, consulting, analyst, controller, etc.
  - Location: Zürich (10km Radius)
  - Job Type: Teilzeit
  - Ausschluss: Senior, Lead, Director, etc.

## 🔧 Anpassungen

### Suchzeiten ändern

Bearbeite `.github/workflows/job_monitor.yml`:

```yaml
schedule:
  - cron: '0 7,17 * * *'  # 08:00 und 18:00 Uhr
```

Beispiele:
- `'0 8 * * *'` = Einmal täglich um 09:00 Uhr
- `'0 6,12,18 * * *'` = 3x täglich (07:00, 13:00, 19:00 Uhr)
- `'0 9 * * 1-5'` = Nur Mo-Fr um 10:00 Uhr

### Suchbegriffe anpassen

Bearbeite `job_monitor.py`, Zeile 17-24:

```python
KEYWORDS = [
    "deine", "eigenen", "keywords"
]
```

### Weitere Jobportale hinzufügen

Füge in `job_monitor.py` eine neue Funktion hinzu (z.B. `search_linkedin()`).

## 📱 Telegram-Befehle

Schicke deinem Bot folgende Nachrichten:

- Beliebiger Text → Der Bot antwortet nicht (er sendet nur neue Jobs)
- Du bekommst nur Nachrichten, wenn neue Jobs gefunden werden

## 🐛 Troubleshooting

**Keine Telegram-Nachrichten?**
1. Prüfe, ob du dem Bot eine Nachricht geschickt hast (Schritt 2.2)
2. Prüfe die GitHub Secrets (Schritt 5)
3. Gehe zu Actions → Klicke auf den letzten Run → Prüfe die Logs

**GitHub Actions läuft nicht?**
1. Prüfe ob Actions aktiviert ist (Schritt 6)
2. Bei Private Repos: Du brauchst GitHub Free (2000 min/Monat kostenlos)

**Jobs sind nicht relevant?**
1. Passe die `KEYWORDS` in `job_monitor.py` an
2. Passe die `EXCLUDE_KEYWORDS` an

## 💡 Kosten

**Komplett kostenlos!**
- GitHub Actions: 2000 Minuten/Monat kostenlos
- Dein Script braucht ~2 Minuten pro Run
- 2x täglich = 4 Minuten/Tag = 120 Minuten/Monat
- **Fazit:** Völlig ausreichend!

## 📝 Lizenz

MIT License - Du kannst alles damit machen was du willst!

---

**Viel Erfolg bei der Jobsuche! 🚀**

Bei Fragen: Schreib mir einfach im Chat!
