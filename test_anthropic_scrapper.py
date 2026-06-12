from app.scrapers.anthropic import get_anthropic_articles

articles = get_anthropic_articles()

print(f"\nFound {len(articles)} articles\n")

for article in articles[:10]:
    print(article)