import requests
from bs4 import BeautifulSoup

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

print("Status:", response.status_code)

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

print("\nPAGE TITLE:")
print(soup.title.text if soup.title else "No title found")

print("\nFIRST 20 LINKS:")

links = soup.find_all("a")

for link in links[:20]:
    print(link.get("href"))