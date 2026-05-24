import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.database import MongoDBClient
from src.pipeline import ScrapingPipeline

st.set_page_config(
    page_title="Job Market Analyzer",
    page_icon="💼",
    layout="wide"
)

st.title("💼 Job Market Analyzer")
st.markdown("### Remote Jobs Dashboard — Powered by Web Scraping & MongoDB")
st.markdown("---")

# Database connect
db = MongoDBClient()

# Sidebar
st.sidebar.title("⚙️ Controls")

# Scrape button
if st.sidebar.button("🔄 Scrape New Jobs", use_container_width=True):
    with st.spinner("Scraping jobs... Please wait!"):
        pipeline = ScrapingPipeline()
        job_titles = [
            "Python Developer",
            "Data Scientist",
            "Machine Learning Engineer",
            "Data Analyst",
            "MLOps Engineer"
        ]
        stats = pipeline.run(job_titles=job_titles, locations=["Remote"])
    st.sidebar.success(f"✅ {stats['total_jobs']} jobs found!")
    st.rerun()

# Filter
st.sidebar.markdown("### 🔍 Filters")
search_keyword = st.sidebar.text_input("Search by Title", "")

# Data load
jobs = db.get_all_jobs()

if not jobs:
    st.warning("⚠️ No jobs found! Click 'Scrape New Jobs' button!")
else:
    df = pd.DataFrame(jobs)

    # Search filter
    if search_keyword:
        df = df[df["title"].str.contains(search_keyword, case=False, na=False)]

    # Keyword filter
    keywords = ["All"] + list(df["search_keyword"].unique())
    selected_keyword = st.sidebar.selectbox("Filter by Category", keywords)
    if selected_keyword != "All":
        df = df[df["search_keyword"] == selected_keyword]

    # Stats Cards
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("💼 Total Jobs", len(df))
    with col2:
        st.metric("🏢 Companies", df["company"].nunique())
    with col3:
        st.metric("📍 Locations", df["location"].nunique())
    with col4:
        st.metric("🔑 Categories", df["search_keyword"].nunique())

    st.markdown("---")

    # Charts
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Jobs by Category")
        category_count = df["search_keyword"].value_counts().reset_index()
        category_count.columns = ["Category", "Count"]
        fig1 = px.bar(
            category_count,
            x="Category",
            y="Count",
            color="Count",
            color_continuous_scale="blues"
        )
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.subheader("📍 Jobs by Location")
        location_count = df["location"].value_counts().head(10).reset_index()
        location_count.columns = ["Location", "Count"]
        fig2 = px.pie(
            location_count,
            values="Count",
            names="Location",
            hole=0.4
        )
        st.plotly_chart(fig2, use_container_width=True)

    # Job Type Chart
    st.subheader("💰 Salary Distribution")
    salary_df = df[df["salary"] != "Not Disclosed"]
    if len(salary_df) > 0:
        fig3 = px.histogram(
            salary_df,
            x="salary",
            color="search_keyword"
        )
        st.plotly_chart(fig3, use_container_width=True)
    else:
        st.info("Salary data not available for these jobs")

    # Jobs Table
    st.markdown("---")
    st.subheader("📋 All Jobs")

    # Display table
    display_df = df[["title", "company", "location", "salary", "search_keyword", "scraped_at"]].copy()
    display_df.columns = ["Title", "Company", "Location", "Salary", "Category", "Scraped At"]

    st.dataframe(
        display_df,
        use_container_width=True,
        height=400
    )

    # Download button
    csv = display_df.to_csv(index=False)
    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name="jobs_data.csv",
        mime="text/csv"
    )

    # Job Links
    st.markdown("---")
    st.subheader("🔗 Apply for Jobs")
    for _, row in df.head(10).iterrows():
        with st.expander(f"💼 {row['title']} — {row['company']}"):
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"📍 **Location:** {row['location']}")
                st.write(f"💰 **Salary:** {row['salary']}")
            with col2:
                st.write(f"🏷️ **Category:** {row['search_keyword']}")
                st.write(f"📅 **Scraped:** {row['scraped_at']}")
            st.link_button("Apply Now 🚀", row["link"])