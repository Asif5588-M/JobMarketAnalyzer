from src.scraper import IndeedScraper
from src.database import MongoDBClient
from datetime import datetime

class ScrapingPipeline:
    def __init__(self):
        self.scraper = IndeedScraper()
        self.db = MongoDBClient()

    def run(self, job_titles: list, locations: list, pages: int = 2):
        print("🚀 Pipeline shuru ho rahi hai!")
        print(f"⏰ Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Old jobs clear karo
        self.db.clear_old_jobs()
        
        all_jobs = []
        
        for title in job_titles:
            for location in locations:
                jobs = self.scraper.scrape_jobs(title, location, pages)
                all_jobs.extend(jobs)
        
        # MongoDB mein save karo
        if all_jobs:
            self.db.insert_jobs(all_jobs)
        
        # Stats print karo
        stats = self.db.get_stats()
        print("\n📊 Pipeline Complete!")
        print(f"Total Jobs: {stats['total_jobs']}")
        print(f"Unique Locations: {stats['unique_locations']}")
        print(f"Unique Titles: {stats['unique_titles']}")
        
        return stats