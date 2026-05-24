---
title: Job Market Analyzer
emoji: 💼
colorFrom: blue
colorTo: green
sdk: streamlit
app_file: dashboard/app.py
pinned: false
---

# 💼 Job Market Analyzer

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-green)
![WebScraping](https://img.shields.io/badge/Web-Scraping-orange)

## 📋 Project Overview
A complete web scraping and analytics dashboard that automatically 
collects remote job data and displays real-time insights.

## 🔧 What I Built
- Web Scraping Pipeline → Remotive.io API
- MongoDB Atlas → Data Storage
- Streamlit Dashboard → Live Analytics
- Charts → Jobs by Category, Location, Salary
- Download CSV feature
- Real-time job search & filters

## 🎯 Features
- 🔄 One-click job scraping
- 📊 Interactive charts (Plotly)
- 🔍 Search & filter jobs
- 📥 Download data as CSV
- 🔗 Direct apply links

## 🛠️ Tech Stack
- Language: Python 3.10
- Web Scraping: BeautifulSoup, Requests
- Database: MongoDB Atlas
- Dashboard: Streamlit
- Charts: Plotly
- Data: Pandas, NumPy

## 📁 Project Structure
```
JobMarketAnalyzer/
├── src/
│   ├── scraper/
│   │   └── __init__.py
│   ├── database/
│   │   └── __init__.py
│   └── pipeline/
│       └── __init__.py
├── dashboard/
│   └── app.py
├── main.py
├── requirements.txt
└── README.md
```

## 🚀 How to Run Locally

### 1. Clone Repository
```bash
git clone https://github.com/Asif5588-M/JobMarketAnalyzer.git
cd JobMarketAnalyzer
```

### 2. Create Environment
```bash
conda create -n jobscraper python=3.10 -y
conda activate jobscraper
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables
```bash
# .env file banao
MONGODB_URL="your-mongodb-url"
```

### 5. Scrape Jobs
```bash
python main.py
```

### 6. Run Dashboard
```bash
streamlit run dashboard/app.py
```

## 🌐 Live Demo
[Streamlit App](https://jobmarket-asifmalik.streamlit.app)

## 👨‍💻 Author
**Asif Malik**
- GitHub: [@Asif5588-M](https://github.com/Asif5588-M)
- Upwork: [asif-nawaz-ml](https://www.upwork.com/freelancers/asifmalik)

