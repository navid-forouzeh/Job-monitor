#!/usr/bin/env python3
"""
Automatischer Job-Monitor für Navid Forouzeh
Sucht täglich nach relevanten Teilzeitstellen in Zürich (Finance/Banking/Consulting)
Sendet Benachrichtigungen via Telegram
"""

import requests
import os
from datetime import datetime
import time
import re

# Telegram Config
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

# Suchkriterien für Navid
KEYWORDS = [
    "finance", "banking", "financial", "analyst", "investment",
    "consulting", "consultant", "business analyst", "corporate finance",
    "asset management", "wealth management", "risk management",
    "controller", "accounting", "treasury", "m&a", "private equity",
    "portfolio", "credit", "equity", "operations"
]

EXCLUDE_KEYWORDS = [
    "senior", "lead", "head of", "director", "vp", "vice president",
    "10+ years", "5+ jahre", "erfahrung erforderlich", "mehrjährige",
    "langjährige", "experienced"
]

class JobMonitor:
    def __init__(self):
        self.seen_jobs_file = "seen_jobs.txt"
        self.seen_jobs = self.load_seen_jobs()
        
    def load_seen_jobs(self):
        """Lädt bereits gesehene Job-IDs"""
        if os.path.exists(self.seen_jobs_file):
            try:
                with open(self.seen_jobs_file, 'r') as f:
                    return set(line.strip() for line in f if line.strip())
            except:
                return set()
        return set()
    
    def save_job_id(self, job_id):
        """Speichert Job-ID als gesehen"""
        if job_id not in self.seen_jobs:
            self.seen_jobs.add(job_id)
            try:
                with open(self.seen_jobs_file, 'a') as f:
                    f.write(f"{job_id}\n")
            except:
                pass
    
    def search_indeed(self):
        """Durchsucht Indeed nach Jobs"""
        jobs = []
        
        search_terms = [
            "finance teilzeit zürich",
            "banking teilzeit zürich",
            "consulting teilzeit zürich"
        ]
        
        for term in search_terms:
            try:
                # Indeed Jobs API
                url = "https://ch.indeed.com/jobs"
                params = {
                    'q': term,
                    'l': 'Zürich',
                    'jt': 'parttime',
                    'sort': 'date',
                    'fromage': '7'
                }
                
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                }
                
                response = requests.get(url, params=params, headers=headers, timeout=15)
                
                if response.status_code == 200:
                    # Einfaches Scraping der Job-Karten
                    html = response.text
                    
                    # Finde Job-Links
                    job_pattern = r'<a[^>]*href="/rc/clk\?jk=([^"]+)"[^>]*><span[^>]*>([^<]+)</span>'
                    matches = re.findall(job_pattern, html)
                    
                    for job_id, title in matches[:10]:
                        # Finde Firma
                        company_pattern = rf'{re.escape(title)}.*?<span[^>]*data-testid="company-name"[^>]*>([^<]+)</span>'
                        company_match = re.search(company_pattern, html, re.DOTALL)
                        company = company_match.group(1) if company_match else "Unbekannt"
                        
                        full_id = f"indeed_{job_id}"
                        
                        jobs.append({
                            'id': full_id,
                            'title': title.strip(),
                            'company': company.strip(),
                            'url': f"https://ch.indeed.com/viewjob?jk={job_id}",
                            'source': 'Indeed'
                        })
                
            except Exception as e:
                print(f"Indeed Fehler: {e}")
            
            time.sleep(2)
        
        return jobs
    
    def search_jobsch(self):
        """Durchsucht jobs.ch nach Jobs"""
        jobs = []
        
        search_terms = ["finance", "banking", "consulting"]
        
        for term in search_terms:
            try:
                url = "https://www.jobs.ch/de/stellenangebote/"
                params = {
                    'term': f"{term} teilzeit",
                    'location': 'Zürich',
                    'employment': 'parttime'
                }
                
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                }
                
                response = requests.get(url, params=params, headers=headers, timeout=15)
                
                if response.status_code == 200:
                    html = response.text
                    
                    # Einfaches Pattern für jobs.ch
                    job_pattern = r'<a[^>]*href="(/de/stellenangebote/detail/[^"]+)"[^>]*>([^<]+)</a>'
                    matches = re.findall(job_pattern, html)
                    
                    for url_part, title in matches[:10]:
                        job_id = f"jobsch_{hash(url_part)}"
                        
                        jobs.append({
                            'id': job_id,
                            'title': title.strip(),
                            'company': 'jobs.ch',
                            'url': f"https://www.jobs.ch{url_part}",
                            'source': 'jobs.ch'
                        })
                
            except Exception as e:
                print(f"jobs.ch Fehler: {e}")
            
            time.sleep(2)
        
        return jobs
    
    def filter_relevant_jobs(self, jobs):
        """Filtert Jobs nach Relevanz"""
        relevant = []
        
        for job in jobs:
            title_lower = job['title'].lower()
            
            # Ausschluss-Check
            if any(exclude.lower() in title_lower for exclude in EXCLUDE_KEYWORDS):
                continue
            
            # Keyword-Check
            if any(keyword.lower() in title_lower for keyword in KEYWORDS):
                relevant.append(job)
        
        return relevant
    
    def send_telegram(self, jobs):
        """Sendet Telegram-Nachricht mit Jobs"""
        if not jobs:
            print("ℹ️ Keine neuen Jobs gefunden")
            return
        
        message = f"🎯 *{len(jobs)} neue Teilzeitstellen gefunden!*\n\n"
        
        for i, job in enumerate(jobs[:5], 1):
            message += f"{i}. *{job['title']}*\n"
            message += f"   🏢 {job['company']}\n"
            message += f"   📍 {job['source']}\n"
            message += f"   🔗 [Zum Job]({job['url']})\n\n"
        
        if len(jobs) > 5:
            message += f"\n_... und {len(jobs) - 5} weitere Jobs_"
        
        message += f"\n\n_Gesucht am {datetime.now().strftime('%d.%m.%Y %H:%M')}_"
        
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
                print(f"✅ Telegram-Nachricht gesendet: {len(jobs)} Jobs")
            else:
                print(f"❌ Telegram-Fehler: {response.status_code}")
        except Exception as e:
            print(f"❌ Telegram-Fehler: {e}")
    
    def run(self):
        """Hauptfunktion"""
        print(f"🔍 Starte Job-Suche ({datetime.now().strftime('%d.%m.%Y %H:%M')})")
        
        all_jobs = []
        
        # Durchsuche alle Quellen
        print("📊 Durchsuche Indeed...")
        all_jobs.extend(self.search_indeed())
        
        print("📊 Durchsuche jobs.ch...")
        all_jobs.extend(self.search_jobsch())
        
        print(f"✅ {len(all_jobs)} Jobs insgesamt gefunden")
        
        # Filtere relevante Jobs
        relevant = self.filter_relevant_jobs(all_jobs)
        print(f"🎯 {len(relevant)} relevante Jobs nach Filterung")
        
        # Finde neue Jobs
        new_jobs = []
        for job in relevant:
            if job['id'] not in self.seen_jobs:
                new_jobs.append(job)
                self.save_job_id(job['id'])
        
        print(f"🆕 {len(new_jobs)} neue Jobs gefunden")
        
        # Sende Benachrichtigung
        if new_jobs:
            self.send_telegram(new_jobs)
        else:
            print("ℹ️ Keine neuen Jobs - keine Benachrichtigung")

if __name__ == "__main__":
    monitor = JobMonitor()
    monitor.run()
