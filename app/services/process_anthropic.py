from app.database.connection import SessionLocal
from app.database.models import Source
from app.database.models import Article

from app.scrapers.anthropic import get_anthropic_articles


def process_anthropic():

    db = SessionLocal()

    source = (
        db.query(Source)
        .filter(Source.name == "Anthropic")
        .first()
    )

    if not source:

        source = Source(
            name="Anthropic",
            url="https://www.anthropic.com/news",
            source_type="blog"
        )

        db.add(source)
        db.commit()
        db.refresh(source)

    articles = get_anthropic_articles()

    inserted = 0

    for article in articles:

        exists = (
            db.query(Article)
            .filter(
                Article.url == article["url"]
            )
            .first()
        )

        if exists:
            continue

        new_article = Article(
            source_id=source.id,
            title=article["title"],
            url=article["url"],
            content=""
        )

        db.add(new_article)

        inserted += 1

    db.commit()

    print(
        f"Inserted {inserted} Anthropic articles"
    )