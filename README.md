# 📰 News Scraper — Guardian API + Kathmandu Post

A Python news scraper that pulls real-time headlines from two sources: the **Guardian API** and the **Kathmandu Post** website. Built using `requests` and `BeautifulSoup`.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![Libraries](https://img.shields.io/badge/libs-requests%20%7C%20BeautifulSoup4-orange)

---

## 📌 What It Does

### 1. `guardian_scraper.py` — Guardian News API
Fetches the latest articles from **The Guardian** using their public API and prints the title (`webTitle`) of each result.

```
Guardian API → JSON response → filter results → print webTitles
```

### 2. `kathmandu_scraper.py` — Kathmandu Post Web Scraper
Scrapes live headlines directly from [kathmandupost.com](https://kathmandupost.com):

- Grabs the **main headline** (top article)
- Grabs **3 sub-headlines** from the homepage
- Extracts all links from the **Trending Topics** section
- Visits each trending link and scrapes the **full article headline**

```
kathmandupost.com → BeautifulSoup → parse HTML → extract headlines → follow trending links → extract article titles
```

---

## 🗂️ Project Structure

```
scraper/
├── guardian_scraper.py       # Guardian API news fetcher
├── kathmandu_scraper.py      # Kathmandu Post HTML scraper
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- `requests`
- `beautifulsoup4`

### Install Dependencies

```bash
pip install requests beautifulsoup4
```

### Run Guardian Scraper

```bash
python guardian_scraper.py
```

**Output:** A list of article titles from The Guardian's latest content feed.

### Run Kathmandu Post Scraper

```bash
python kathmandu_scraper.py
```

**Output:**
```
[Main Headline]
[Sub Headline 2]
[Sub Headline 3]
[Sub Headline 4]
--- trending topics ---
[Article 1 full title]
[Article 2 full title]
...
```

---

## 🔧 Configuration

### Guardian API Key

The Guardian API key is currently hardcoded in `guardian_scraper.py`. To use your own key:

1. Register at [open-platform.theguardian.com](https://open-platform.theguardian.com/access/)
2. Replace the key in the URL:

```python
api_response = requests.get('https://content.guardianapis.com/search?api-key=YOUR_KEY_HERE')
```

> ⚠️ Avoid committing your API key to public repos. Consider using a `.env` file and `python-dotenv`.

---

## 🧠 How the Scraping Works

### Guardian API (JSON)
```
response.json()
  └── "response"
        └── "results"  ← list of articles
              └── [i]
                    └── "webTitle"  ← what we extract
```

### Kathmandu Post (HTML)
| Target | HTML Selector |
|---|---|
| Main headline | `article.1 > h2 > a` |
| Sub-headlines | `article.article-image--left {2,3,4} > h3 > a` |
| Trending links | `ul.trending-topics-list > a[href]` |
| Article title | `div.col-sm-8 > h1` |

The scraper builds full URLs by prepending `https://kathmandupost.com` to each relative link found in the trending section, then makes a separate request to each one.

---

## 🗺️ Roadmap

- [x] Guardian API integration
- [x] Kathmandu Post homepage scraping
- [x] Trending topics deep-scraping
- [ ] Save output to CSV / JSON file
- [ ] Add more news sources
- [ ] Schedule scraper to run automatically (cron / APScheduler)
- [ ] Error handling for failed requests / changed HTML structure
- [ ] Store API key securely via `.env`

---

## ⚠️ Notes

- Web scraping depends on the site's HTML structure. If Kathmandu Post updates their layout, the CSS selectors may need to be updated.
- Be respectful of websites' `robots.txt` and rate limits. Add `time.sleep()` between requests if scraping many pages.
- The Guardian API has a free tier with a rate limit of 12 calls/second.

---

## 👤 Author

**Ez-Saksham**  
GitHub: [@Ez-Saksham](https://github.com/Ez-Saksham)

---

> ⭐ Star this repo if you find it useful!
