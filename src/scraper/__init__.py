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
        self.base_url = "https://www.indeed.com/jobs"
        self.jobs = []

    def scrape_jobs(self, job_title: str, location: str, pages: int = 3):
        print(f"🔍 Scraping: {job_title} in {location}")
        
        for page in range(0, pages * 10, 10):
            try:
                params = {
                    "q": job_title,
                    "l": location,
                    "start": page
                }
                
                response = requests.get(
                    self.base_url,
                    headers=self.headers,
                    params=params,
                    timeout=10
                )
                
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, "lxml")
                    job_cards = soup.find_all("div", class_="job_seen_beacon")
                    
                    if not job_cards:
                        # Alternative selector
                        job_cards = soup.find_all("div", {"class": "cardOutline"})
                    
                    for card in job_cards:
                        job = self.extract_job_data(card, job_title, location)
                        if job:
                            self.jobs.append(job)
                    
                    print(f"✅ Page {page//10 + 1} scraped — {len(job_cards)} jobs found")
                else:
                    print(f"❌ Status code: {response.status_code}")
                
                # Random delay — avoid getting blocked
                time.sleep(random.uniform(2, 4))
                
            except Exception as e:
                print(f"❌ Error on page {page}: {e}")
                continue
        
        print(f"✅ Total jobs scraped: {len(self.jobs)}")
        return self.jobs

    def extract_job_data(self, card, job_title, location):
        try:
            # Title
            title_elem = card.find("h2", class_="jobTitle")
            title = title_elem.get_text(strip=True) if title_elem else "N/A"
            
            # Company
            company_elem = card.find("span", {"data-testid": "company-name"})
            company = company_elem.get_text(strip=True) if company_elem else "N/A"
            
            # Location
            location_elem = card.find("div", {"data-testid": "text-location"})
            job_location = location_elem.get_text(strip=True) if location_elem else location
            
            # Salary
            salary_elem = card.find("div", {"class": "salary-snippet-container"})
            salary = salary_elem.get_text(strip=True) if salary_elem else "Not Disclosed"
            
            # Job Type
            jobtype_elem = card.find("div", {"class": "metadata"})
            job_type = jobtype_elem.get_text(strip=True) if jobtype_elem else "N/A"

            # Job Link
            link_elem = card.find("a", {"class": "jcs-JobTitle"})
            link = "https://www.indeed.com" + link_elem["href"] if link_elem else "N/A"

            return {
                "title": title,
                "company": company,
                "location": job_location,
                "salary": salary,
                "job_type": job_type,
                "link": link,
                "search_keyword": job_title,
                "scraped_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        except Exception as e:
            return None

    def to_dataframe(self):
        return pd.DataFrame(self.jobs)