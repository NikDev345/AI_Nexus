from app.database.connection import SessionLocal
from app.database.models import Source
from app.database.models import Article

from app.scrapers.openai import get_openai_articles


def process_openai():

    db = SessionLocal()

    source = (
        db.query(Source)
        .filter(Source.name == "OpenAI")
        .first()
    )

    if not source:

        source = Source(
            name="OpenAI",
            url="https://openai.com/news/",
            source_type="blog"
        )

        db.add(source)
        db.commit()
        db.refresh(source)

    articles = get_openai_articles()

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
        f"Inserted {inserted} articles"
    )