from app.scrapers.openai import get_openai_articles

articles = get_openai_articles()

print(f"\nFound {len(articles)} articles\n")

for article in articles[:10]:
    print(article)
    