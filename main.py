from src.pipeline import ScrapingPipeline

if __name__ == "__main__":
    pipeline = ScrapingPipeline()
    
    # Job titles to search
    job_titles = [
        "Python Developer",
        "Data Scientist",
        "Machine Learning Engineer",
        "Data Analyst",
        "MLOps Engineer"
    ]
    
    # Locations
    locations = [
        "Remote",
        "New York",
        "San Francisco"
    ]
    
    # Run pipeline
    stats = pipeline.run(
        job_titles=job_titles,
        locations=locations,
        pages=2
    )
    
    print(f"\n✅ Done! {stats['total_jobs']} jobs scraped!")