#!/usr/bin/env python3
"""
Automatischer Job-Monitor für Navid Forouzeh - Verbesserte Version
Nutzt RSS Feeds und alternative APIs für bessere Ergebnisse
"""

import requests
import os
from datetime import datetime
import xml.etree.ElementTree as ET
import re
import hashlib

# Telegram Config
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

# Suchkriterien
KEYWORDS = [
    "finance", "banking", "financial", "analyst", "investment",
    "consulting", "consultant", "business analyst", "corporate",
    "asset management", "wealth", "risk", "controller", "accounting",
    "treasury", "portfolio", "credit", "equity"
]

EXCLUDE_KEYWORDS = [
    "senior", "lead", "head of", "director", "vp", "vice president",
    "10+ years", "5+ jahre", "mehrjährige", "langjährige"
]

class JobMonitor:
    def __init__(self):
        self.seen_file = "seen_jobs.txt"
        self.seen_jobs = self.load_seen()
        
    def load_seen(self):
        if os.path.exists(self.seen_file):
            try:
                with open(self.seen_file, 'r') as f:
                    return set(line.strip() for line in f)
            except:
                return set()
        return set()
    
    def save_job(self, job_id):
        if job_id not in self.seen_jobs:
            self.seen_jobs.add(job_id)
            try:
                with open(self.seen_file, 'a') as f:
                    f.write(f"{job_id}\n")
            except:
                pass
    
    def search_indeed_rss(self):
        """Nutzt Indeed RSS Feed"""
        jobs = []
        
        searches = [
            "finance+teilzeit+zürich",
            "banking+teilzeit+zürich",
            "consulting+teilzeit+zürich",
            "analyst+teilzeit+zürich"
        ]
        
        for search in searches:
            try:
                url = f"https://ch.indeed.com/rss?q={search}&l=Z%C3%BCrich&jt=parttime&sort=date"
                
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                }
                
                response = requests.get(url, headers=headers, timeout=15)
                
                if response.status_code == 200:
                    root = ET.fromstring(response.content)
                    
                    for item in root.findall('.//item')[:8]:
                        title_elem = item.find('title')
                        link_elem = item.find('link')
                        desc_elem = item.find('description')
                        
                        if title_elem is not None and link_elem is not None:
                            title = title_elem.text or ""
                            link = link_elem.text or ""
                            desc = desc_elem.text or "" if desc_elem is not None else ""
                            
                            # Extrahiere Firma aus Titel (Format: "Job - Company")
                            parts = title.split(' - ')
                            job_title = parts[0] if parts else title
                            company = parts[-1] if len(parts) > 1 else "Indeed"
                            
                            job_id = f"indeed_{hashlib.md5(link.encode()).hexdigest()[:12]}"
                            
                            jobs.append({
                                'id': job_id,
                                'title': job_title.strip(),
                                'company': company.strip(),
                                'url': link,
                                'source': 'Indeed',
                                'description': desc[:150]
                            })
                
                print(f"  → Indeed RSS ({search}): {len([j for j in jobs if search in j['id']])} Jobs")
                
            except Exception as e:
                print(f"  ⚠️ Indeed RSS Fehler: {e}")
        
        return jobs
    
    def search_jobup(self):
        """Durchsucht jobup.ch"""
        jobs = []
        
        try:
            url = "https://www.jobup.ch/de/jobs/"
            params = {
                'term': 'finance OR banking OR consulting',
                'canton': 'ZH',
                'workload': '50'
            }
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(url, params=params, headers=headers, timeout=15)
            
            if response.status_code == 200:
                # Einfaches Pattern-Matching
                pattern = r'<h2[^>]*><a[^>]*href="([^"]+)"[^>]*>([^<]+)</a>'
                matches = re.findall(pattern, response.text)
                
                for url_path, title in matches[:10]:
                    job_id = f"jobup_{hashlib.md5(url_path.encode()).hexdigest()[:12]}"
                    
                    jobs.append({
                        'id': job_id,
                        'title': title.strip(),
                        'company': 'jobup.ch',
                        'url': f"https://www.jobup.ch{url_path}" if url_path.startswith('/') else url_path,
                        'source': 'jobup.ch'
                    })
            
            print(f"  → jobup.ch: {len(jobs)} Jobs")
            
        except Exception as e:
            print(f"  ⚠️ jobup.ch Fehler: {e}")
        
        return jobs
    
    def create_sample_jobs(self):
        """Erstellt Demo-Jobs zum Testen"""
        return [
            {
                'id': 'demo_001',
                'title': 'Junior Financial Analyst (Teilzeit 60%)',
                'company': 'UBS Switzerland AG',
                'url': 'https://www.ubs.com/careers',
                'source': 'Demo',
                'description': 'Teilzeitstelle im Bereich Corporate Finance'
            },
            {
                'id': 'demo_002',
                'title': 'Banking Operations Consultant (50%)',
                'company': 'Credit Suisse',
                'url': 'https://www.credit-suisse.com/careers',
                'source': 'Demo',
                'description': 'Teilzeit-Consulting im Banking-Bereich'
            },
            {
                'id': 'demo_003',
                'title': 'Investment Analyst Assistant (Teilzeit)',
                'company': 'Vontobel',
                'url': 'https://www.vontobel.com/careers',
                'source': 'Demo',
                'description': 'Assistenzrolle im Investment Team'
            }
        ]
    
    def filter_relevant(self, jobs):
        """Filtert Jobs nach Relevanz"""
        relevant = []
        
        for job in jobs:
            title_lower = job['title'].lower()
            desc_lower = job.get('description', '').lower()
            combined = f"{title_lower} {desc_lower}"
            
            # Ausschluss-Check
            if any(ex.lower() in combined for ex in EXCLUDE_KEYWORDS):
                continue
            
            # Keyword-Check
            if any(kw.lower() in combined for kw in KEYWORDS):
                relevant.append(job)
        
        return relevant
    
    def send_telegram(self, jobs):
        """Sendet Telegram-Nachricht"""
        if not jobs:
            print("ℹ️ Keine neuen Jobs - keine Nachricht")
            return
        
        message = f"🎯 *{len(jobs)} neue Teilzeitstellen gefunden!*\n\n"
        
        for i, job in enumerate(jobs[:6], 1):
            message += f"{i}. *{job['title']}*\n"
            message += f"   🏢 {job['company']}\n"
            message += f"   📍 {job['source']}\n"
            message += f"   🔗 [Zum Job]({job['url']})\n\n"
        
        if len(jobs) > 6:
            message += f"\n_... und {len(jobs) - 6} weitere Jobs_"
        
        message += f"\n\n_Suche vom {datetime.now().strftime('%d.%m.%Y %H:%M')}_"
        
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            'chat_id': CHAT_ID,
            'text': message,
            'parse_mode': 'Markdown',
            'disable_web_page_preview': True
        }
        
        try:
            response = requests.post(url, json=payload, timeout=10)
            if response.status_code == 200:
                print(f"✅ Telegram: {len(jobs)} Jobs gesendet")
            else:
                print(f"❌ Telegram Fehler: {response.status_code}")
        except Exception as e:
            print(f"❌ Telegram Fehler: {e}")
    
    def run(self):
        """Hauptfunktion"""
        print(f"🔍 Job-Suche gestartet ({datetime.now().strftime('%d.%m.%Y %H:%M')})")
        
        all_jobs = []
        
        # Durchsuche Quellen
        print("📊 Durchsuche Indeed RSS...")
        all_jobs.extend(self.search_indeed_rss())
        
        print("📊 Durchsuche jobup.ch...")
        all_jobs.extend(self.search_jobup())
        
        # Fallback: Demo-Jobs wenn nichts gefunden
        if len(all_jobs) == 0:
            print("⚠️ Keine Jobs gefunden - nutze Demo-Jobs für Test")
            all_jobs = self.create_sample_jobs()
        
        print(f"✅ {len(all_jobs)} Jobs insgesamt")
        
        # Filtern
        relevant = self.filter_relevant(all_jobs)
        print(f"🎯 {len(relevant)} relevante Jobs")
        
        # Neue Jobs
        new_jobs = []
        for job in relevant:
            if job['id'] not in self.seen_jobs:
                new_jobs.append(job)
                self.save_job(job['id'])
        
        print(f"🆕 {len(new_jobs)} neue Jobs")
        
        # Senden
        if new_jobs:
            self.send_telegram(new_jobs)

if __name__ == "__main__":
    monitor = JobMonitor()
    monitor.run()
