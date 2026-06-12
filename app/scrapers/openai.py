import requests
from bs4 import BeautifulSoup


def get_openai_articles():
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/137.0.0.0 Safari/537.36"
        )
    }

    response = requests.get(
        "https://openai.com/news/",
        headers=headers
    )

    if response.status_code != 200:
        print("Failed to fetch OpenAI news")
        return []

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    articles = []

    links = soup.find_all("a")

    for link in links:

        href = link.get("href")

        if href and href.startswith("/index/"):

            title = link.get_text(strip=True)

            articles.append({
                "title": title,
                "url": f"https://openai.com{href}"
            })

    return articles