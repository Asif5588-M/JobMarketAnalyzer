import os
import pymongo
from dotenv import load_dotenv

load_dotenv()

class MongoDBClient:
    def __init__(self):
        self.client = pymongo.MongoClient(os.getenv("MONGODB_URL"))
        self.db = self.client["jobmarket"]
        self.collection = self.db["jobs"]
    
    def insert_jobs(self, jobs: list):
        if jobs:
            self.collection.insert_many(jobs)
            print(f"✅ {len(jobs)} jobs inserted!")
    
    def get_all_jobs(self):
        return list(self.collection.find({}, {"_id": 0}))
    
    def get_jobs_by_title(self, title: str):
        return list(self.collection.find(
            {"title": {"$regex": title, "$options": "i"}},
            {"_id": 0}
        ))
    
    def clear_old_jobs(self):
        self.collection.delete_many({})
        print("🗑️ Old jobs cleared!")
    
    def get_stats(self):
        total = self.collection.count_documents({})
        locations = self.collection.distinct("location")
        titles = self.collection.distinct("title")
        return {
            "total_jobs": total,
            "unique_locations": len(locations),
            "unique_titles": len(titles)
        }