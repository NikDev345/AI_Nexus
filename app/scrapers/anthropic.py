import requests
from bs4 import BeautifulSoup


def get_anthropic_articles():

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/137.0.0.0 Safari/537.36"
        )
    }

    response = requests.get(
        "https://www.anthropic.com/news",
        headers=headers
    )

    if response.status_code != 200:
        print("Failed to fetch Anthropic news")
        return []

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    articles = []

    links = soup.find_all("a")

    for link in links:

        href = link.get("href")

        if href and "/news/" in href:

            title = link.get_text(strip=True)

            if title:

                if href.startswith("/"):
                    href = f"https://www.anthropic.com{href}"

                articles.append({
                    "title": title,
                    "url": href
                })

    # Remove duplicate URLs
    unique_articles = {}

    for article in articles:
        unique_articles[article["url"]] = article

    return list(unique_articles.values())   