# ⚡ Schnell-Setup (5 Minuten)

## 1️⃣ Telegram Bot erstellen (2 Min)

```
1. Öffne Telegram → Suche @BotFather
2. Schreibe: /newbot
3. Name: Navid Job Monitor
4. Username: navid_job_monitor_bot
5. Speichere den TOKEN
```

**Beispiel-Token:** `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`

---

## 2️⃣ Chat ID herausfinden (1 Min)

```
1. Suche deinen Bot in Telegram (@navid_job_monitor_bot)
2. Klicke Start und schreibe "Hallo"
3. Öffne im Browser:
   https://api.telegram.org/bot<DEIN_TOKEN>/getUpdates
4. Suche nach "chat":{"id":123456789
5. Speichere die Chat ID
```

**Beispiel-Chat-ID:** `123456789`

---

## 3️⃣ GitHub Repository (1 Min)

```
1. Gehe zu github.com
2. Klicke "New Repository"
3. Name: job-monitor
4. Public ✅
5. Create Repository
```

---

## 4️⃣ Dateien hochladen (1 Min)

```
1. Klicke "uploading an existing file"
2. Ziehe alle Dateien rein
3. Commit changes
```

---

## 5️⃣ Secrets einrichten (2 Min)

```
1. Settings → Secrets and variables → Actions
2. New repository secret:
   
   Name: TELEGRAM_BOT_TOKEN
   Value: [Dein Token aus Schritt 1]
   
3. New repository secret:
   
   Name: TELEGRAM_CHAT_ID
   Value: [Deine ID aus Schritt 2]
```

---

## 6️⃣ Aktivieren & Testen (1 Min)

```
1. Actions → Enable workflows
2. Job Monitor → Run workflow
3. Warte 1 Minute
4. Checke Telegram! 🎉
```

---

## ✅ Fertig!

Ab jetzt bekommst du **2x täglich** (08:00 + 18:00 Uhr) automatisch neue Jobs via Telegram!

---

## 🔧 Wichtige Befehle

**Manuell ausführen:**
```
Actions → Job Monitor → Run workflow
```

**Logs ansehen:**
```
Actions → Letzter Run → Klicke drauf
```

**Suchzeiten ändern:**
```
Bearbeite: .github/workflows/job_monitor.yml
Zeile 5: - cron: '0 7,17 * * *'
```

---

## 💡 Tipps

- **Keine Duplikate:** Das System merkt sich alle gesendeten Jobs
- **Kostenlos:** 2000 Min/Monat gratis (du brauchst ~120 Min/Monat)
- **Private Repo?** Geht auch, braucht aber GitHub Free Account
- **Funktioniert nicht?** Checke die Logs unter Actions

---

**Support:** Schreib mir einfach im Chat! 🚀
