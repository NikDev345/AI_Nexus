# 🚀 AI Nexus

<div align="center">

![Python](https://img.shields.io/badge/Python-3.13-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-18-blue)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![Gemini](https://img.shields.io/badge/Google-Gemini-orange)
![Status](https://img.shields.io/badge/Status-Production%20MVP-success)

### AI-Powered News Aggregation, Summarization & Newsletter Delivery Platform

Collect AI news from multiple sources, generate intelligent daily digests using Google Gemini, store everything in PostgreSQL, and automatically deliver beautiful HTML newsletters via email.

</div>

---

## 🎯 Project Overview

AI News Aggregator is an end-to-end AI-powered news intelligence platform built using Python, PostgreSQL, SQLAlchemy, Docker, and Google Gemini.

The system automatically:

* Scrapes AI news from multiple trusted sources
* Stores articles in PostgreSQL
* Removes duplicates
* Generates AI-powered summaries
* Creates professional HTML newsletters
* Delivers newsletters via email

---

## 🏗️ System Architecture

<p align="center">
  <img src="./public/pipeline.png" width="100%" alt="AI News Aggregator Pipeline">
</p>

### Processing Pipeline

```text
OpenAI News
      │
Anthropic News
      │
YouTube AI Channels
      │
      ▼
  Web Scrapers
      ▼
 PostgreSQL
      ▼
 SQLAlchemy ORM
      ▼
 Google Gemini
      ▼
 Daily Digest
      ▼
 HTML Newsletter
      ▼
 Email Delivery
```

---

## 🌐 News Sources

### OpenAI

* OpenAI News

### Anthropic

* Anthropic News

### YouTube Channels

* AI Explained
* Fireship
* Matt Wolfe
* Two Minute Papers

---

## ⚙️ Tech Stack

### Backend

* Python

### Database

* PostgreSQL
* SQLAlchemy ORM

### Infrastructure

* Docker

### Scraping

* Requests
* BeautifulSoup
* Feedparser

### AI

* Google Gemini 2.5 Flash Lite

### Delivery

* SMTP Email Service

---

## 📂 Project Structure

```text
ai-news/

├── app/
│
├── database/
│   ├── connection.py
│   ├── models.py
│   ├── repository.py
│
├── scrapers/
│   ├── openai.py
│   ├── anthropic.py
│   └── youtube.py
│
├── services/
│   ├── process_openai.py
│   ├── process_anthropic.py
│   ├── process_youtube.py
│   ├── digest_service.py
│   └── email_service.py
│
├── templates/
│   └── digest_template.py
│
├── docker/
│   └── docker-compose.yml
│
├── tests/
│
└── README.md
```

---

## 🗄️ Database Schema

### Sources

```sql
id
name
url
source_type
created_at
```

### Articles

```sql
id
source_id
title
content
url
published_at
created_at
```

### Digests

```sql
id
title
summary
html_content
created_at
```

---

## ✨ Features

### News Collection

* Multi-source aggregation
* OpenAI integration
* Anthropic integration
* YouTube RSS ingestion

### Data Processing

* Duplicate prevention
* Database persistence
* Source tracking

### AI Summarization

* Gemini-powered digest generation
* Topic clustering
* Executive summaries

### Newsletter Generation

* HTML email templates
* Markdown support
* Professional formatting

### Email Delivery

* Gmail SMTP integration
* Automated newsletter sending

---

## 🚀 Setup

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-News-Aggregator.git

cd AI-News-Aggregator
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file

```env
DATABASE_URL=postgresql://admin:password@localhost:5433/ai_news

GEMINI_API_KEY=YOUR_GEMINI_KEY

EMAIL_ADDRESS=YOUR_EMAIL

EMAIL_APP_PASSWORD=YOUR_APP_PASSWORD
```

---

## 🐳 Start PostgreSQL

```bash
docker compose up -d
```

---

## ▶️ Run Complete Pipeline

```bash
python test_pipeline.py
```

Pipeline Execution:

```text
Fetch Articles
      ▼
Store in PostgreSQL
      ▼
Generate Digest
      ▼
Create HTML Newsletter
      ▼
Save Digest
      ▼
Send Email
```

---

## 📧 Sample Newsletter

Features:

* Executive Summary
* AI Model Updates
* Research Breakthroughs
* Industry Developments
* Source References
* Professional HTML Formatting

---

## 📈 Future Improvements

* Scheduled Daily Execution
* FastAPI REST API
* Web Dashboard
* User Authentication
* Subscriber Management
* Analytics Dashboard
* Multi-Language Support
* RSS Feed Export
* AI Trend Detection

---

## 👨‍💻 Author

### Nagraj (Nikhil) Rangarej

B.Tech Artificial Intelligence & Data Science

Passionate about:

* Artificial Intelligence
* Data Science
* Machine Learning
* Automation
* Backend Engineering

---

## ⭐ Project Status

Current Version:

```text
MVP COMPLETE
```

Completed:

* News Scraping
* PostgreSQL Storage
* SQLAlchemy ORM
* Docker Integration
* Gemini Summaries
* HTML Digest Generation
* Email Delivery

Next Milestone:

```text
Automated Daily Scheduling
```
