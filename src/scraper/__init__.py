import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time
import random


class IndeedScraper:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        self.jobs = []

    def scrape_remotive(self, job_title: str):
        """Remotive.io — Free Remote Jobs API"""
        print(f"🔍 Scraping Remotive: {job_title}")
        try:
            url = f"https://remotive.com/api/remote-jobs?search={job_title}&limit=50"
            response = requests.get(url, headers=self.headers, timeout=10)

            if response.status_code == 200:
                data = response.json()
                jobs = data.get("jobs", [])

                for job in jobs:
                    self.jobs.append({
                        "title": job.get("title", "N/A"),
                        "company": job.get("company_name", "N/A"),
                        "location": job.get("candidate_required_location", "Remote"),
                        "salary": job.get("salary", "Not Disclosed"),
                        "job_type": job.get("job_type", "N/A"),
                        "category": job.get("category", "N/A"),
                        "link": job.get("url", "N/A"),
                        "search_keyword": job_title,
                        "scraped_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })

                print(f"✅ {len(jobs)} jobs found for '{job_title}'")
            else:
                print(f"❌ Status: {response.status_code}")

            time.sleep(random.uniform(1, 2))

        except Exception as e:
            print(f"❌ Error: {e}")

        return self.jobs

    def scrape_jobs(self, job_title: str, location: str = "Remote", pages: int = 2):
        """Main scraping function"""
        return self.scrape_remotive(job_title)

    def to_dataframe(self):
        return pd.DataFrame(self.jobs)