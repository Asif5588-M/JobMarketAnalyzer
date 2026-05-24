from src.pipeline import ScrapingPipeline

if __name__ == "__main__":
    pipeline = ScrapingPipeline()

    job_titles = [
        "Python Developer",
        "Data Scientist",
        "Machine Learning Engineer",
        "Data Analyst",
        "MLOps Engineer"
    ]

    locations = ["Remote"]

    stats = pipeline.run(
        job_titles=job_titles,
        locations=locations,
        pages=2
    )

    print(f"\n✅ Done! {stats['total_jobs']} jobs scraped!")