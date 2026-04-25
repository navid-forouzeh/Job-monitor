#!/usr/bin/env python3
"""
Automatischer Job-Monitor für Navid Forouzeh
Sucht täglich nach relevanten Teilzeitstellen in Zürich (Finance/Banking/Consulting)
Sendet Benachrichtigungen via Telegram
"""

import requests
import json
import os
from datetime import datetime
from typing import List, Dict, Set
import time

# Konfiguration
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

# Suchkriterien für Navid
KEYWORDS = [
    "finance", "banking", "financial", "analyst", "investment",
    "consulting", "consultant", "business analyst", "corporate finance",
    "asset management", "wealth management", "risk management",
    "controller", "accounting", "treasury", "m&a", "private equity"
]

EXCLUDE_KEYWORDS = [
    "senior", "lead", "head of", "director", "vp", "vice president",
    "10+ years", "5+ jahre", "erfahrung erforderlich"
]

LOCATION = "zürich"
JOB_TYPE = "teilzeit"  # oder "part time"

class JobMonitor:
    def __init__(self):
        self.seen_jobs_file = "seen_jobs.txt"
        self.seen_jobs: Set[str] = self.load_seen_jobs()
        
    def load_seen_jobs(self) -> Set[str]:
        """Lädt bereits gesehene Job-IDs aus Textdatei"""
        if os.path.exists(self.seen_jobs_file):
            try:
                with open(self.seen_jobs_file, 'r') as f:
                    return set(line.strip() for line in f if line.strip())
            except:
                return set()
        return set()
    
    def is_job_seen(self, job_id: str) -> bool:
        """Prüft, ob Job bereits gesehen wurde"""
        return job_id in self.seen_jobs
    
    def mark_job_seen(self, job_id: str, title: str, company: str, url: str):
        """Markiert Job als gesehen"""
        if job_id not in self.seen_jobs:
            self.seen_jobs.add(job_id)
            try:
                with open(self.seen_jobs_file, 'a') as f:
                    f.write(f"{job_id}\n")
            except Exception as e:
                print(f"Fehler beim Speichern: {e}")
    
    def search_indeed(self) -> List[Dict]:
        """Durchsucht Indeed nach passenden Jobs"""
        jobs = []
        
        # Indeed Job Search API (öffentlich zugänglich)
        base_url = "https://api.indeed.com/ads/apisearch"
        
        for keyword in ["finance teilzeit zürich", "banking teilzeit zürich", "consulting teilzeit zürich"]:
            params = {
                'publisher': '1234567890',  # Wird durch GitHub Secret ersetzt
                'q': keyword,
                'l': 'Zürich',
                'sort': 'date',
                'radius': '10',
                'st': 'jobsite',
                'jt': 'parttime',
                'start': 0,
                'limit': 25,
                'fromage': 7,  # Jobs der letzten 7 Tage
                'format': 'json',
                'v': '2'
            }
            
            try:
                # Fallback: Web-Scraping wenn API nicht verfügbar
                # Nutze Indeed RSS Feed (öffentlich)
                rss_url = f"https://www.indeed.ch/rss?q={keyword.replace(' ', '+')}&l=Z%C3%BCrich&jt=parttime&sort=date"
                response = requests.get(rss_url, timeout=10)
                
                if response.status_code == 200:
                    # Einfaches RSS-Parsing
                    import xml.etree.ElementTree as ET
                    root = ET.fromstring(response.content)
                    
                    for item in root.findall('.//item')[:10]:
                        title = item.find('title').text if item.find('title') is not None else ""
                        link = item.find('link').text if item.find('link') is not None else ""
                        description = item.find('description').text if item.find('description') is not None else ""
                        pub_date = item.find('pubDate').text if item.find('pubDate') is not None else ""
                        
                        # Extrahiere Firma aus Titel (Format: "Job Title - Company")
                        company = title.split(' - ')[-1] if ' - ' in title else "Unbekannt"
                        job_title = title.split(' - ')[0] if ' - ' in title else title
                        
                        job_id = f"indeed_{hash(link)}"
                        
                        jobs.append({
                            'id': job_id,
                            'title': job_title,
                            'company': company,
                            'url': link,
                            'source': 'Indeed',
                            'description': description[:200],
                            'date': pub_date
                        })
                        
            except Exception as e:
                print(f"Indeed Fehler: {e}")
                
            time.sleep(2)  # Rate limiting
        
        return jobs
    
    def search_jobs_ch(self) -> List[Dict]:
        """Durchsucht jobs.ch"""
        jobs = []
        
        search_terms = ["finance", "banking", "consulting"]
        
        for term in search_terms:
            try:
                # jobs.ch JSON API
                url = "https://www.jobs.ch/api/search"
                params = {
                    'term': f"{term} teilzeit",
                    'location': 'Zürich',
                    'employment': 'parttime',
                    'limit': 20
                }
                
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
                }
                
                response = requests.get(url, params=params, headers=headers, timeout=10)
                
                if response.status_code == 200:
                    data = response.json()
                    
                    if 'jobs' in data:
                        for job in data['jobs'][:10]:
                            job_id = f"jobsch_{job.get('id', hash(job.get('url', '')))}"
                            
                            jobs.append({
                                'id': job_id,
                                'title': job.get('title', 'Kein Titel'),
                                'company': job.get('company', {}).get('name', 'Unbekannt'),
                                'url': job.get('url', ''),
                                'source': 'jobs.ch',
                                'description': job.get('description', '')[:200],
                                'date': job.get('publicationDate', '')
                            })
                
            except Exception as e:
                print(f"jobs.ch Fehler: {e}")
                
            time.sleep(2)
        
        return jobs
    
    def filter_relevant_jobs(self, jobs: List[Dict]) -> List[Dict]:
        """Filtert Jobs nach Relevanz für Navid"""
        relevant_jobs = []
        
        for job in jobs:
            title_lower = job['title'].lower()
            desc_lower = job.get('description', '').lower()
            combined = f"{title_lower} {desc_lower}"
            
            # Ausschlusskriterien
            if any(exclude.lower() in combined for exclude in EXCLUDE_KEYWORDS):
                continue
            
            # Muss mindestens ein Keyword enthalten
            if any(keyword.lower() in combined for keyword in KEYWORDS):
                # Prüfe ob "zürich" oder "zurich" vorkommt
                if "zürich" in combined or "zurich" in combined or "zh" in combined:
                    relevant_jobs.append(job)
        
        return relevant_jobs
    
    def send_telegram_message(self, jobs: List[Dict]):
        """Sendet Telegram-Benachrichtigung mit neuen Jobs"""
        if not jobs:
            return
        
        message = f"🎯 *{len(jobs)} neue relevante Teilzeitstellen gefunden!*\n\n"
        
        for i, job in enumerate(jobs[:5], 1):  # Max 5 Jobs pro Message
            message += f"{i}. *{job['title']}*\n"
            message += f"   🏢 {job['company']}\n"
            message += f"   📍 {job['source']}\n"
            message += f"   🔗 [Zum Job]({job['url']})\n\n"
        
        if len(jobs) > 5:
            message += f"\n_... und {len(jobs) - 5} weitere Jobs_"
        
        message += f"\n\n_Gesucht am {datetime.now().strftime('%d.%m.%Y %H:%M')}_"
        
        # Telegram API Call
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            'chat_id': TELEGRAM_CHAT_ID,
            'text': message,
            'parse_mode': 'Markdown',
            'disable_web_page_preview': True
        }
        
        try:
            response = requests.post(url, json=payload, timeout=10)
            if response.status_code == 200:
                print(f"✅ Telegram-Nachricht gesendet: {len(jobs)} Jobs")
            else:
                print(f"❌ Telegram-Fehler: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"❌ Telegram-Fehler: {e}")
    
    def run(self):
        """Hauptfunktion: Sucht Jobs und sendet Benachrichtigungen"""
        print(f"🔍 Starte Job-Suche für Navid ({datetime.now().strftime('%d.%m.%Y %H:%M')})")
        
        all_jobs = []
        
        # Durchsuche alle Quellen
        print("📊 Durchsuche Indeed...")
        all_jobs.extend(self.search_indeed())
        
        print("📊 Durchsuche jobs.ch...")
        all_jobs.extend(self.search_jobs_ch())
        
        print(f"✅ {len(all_jobs)} Jobs insgesamt gefunden")
        
        # Filtere relevante Jobs
        relevant_jobs = self.filter_relevant_jobs(all_jobs)
        print(f"🎯 {len(relevant_jobs)} relevante Jobs nach Filterung")
        
        # Finde neue Jobs
        new_jobs = []
        for job in relevant_jobs:
            if not self.is_job_seen(job['id']):
                new_jobs.append(job)
                self.mark_job_seen(job['id'], job['title'], job['company'], job['url'])
        
        print(f"🆕 {len(new_jobs)} neue Jobs gefunden")
        
        # Sende Benachrichtigung
        if new_jobs:
            self.send_telegram_message(new_jobs)
            print(f"✅ Telegram-Benachrichtigung gesendet")
        else:
            print("ℹ️ Keine neuen Jobs - keine Benachrichtigung gesendet")

if __name__ == "__main__":
    monitor = JobMonitor()
    monitor.run()
