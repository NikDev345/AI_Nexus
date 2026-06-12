from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.database.models import (
    Source,
    Article,
    Digest
)


class Repository:

    def __init__(self, db: Session):
        self.db = db

    # =========================
    # SOURCES
    # =========================

    def create_source(
        self,
        name,
        url,
        source_type
    ):

        existing = (
            self.db.query(Source)
            .filter(Source.name == name)
            .first()
        )

        if existing:
            return existing

        source = Source(
            name=name,
            url=url,
            source_type=source_type
        )

        self.db.add(source)
        self.db.commit()
        self.db.refresh(source)

        return source

    # =========================
    # ARTICLES
    # =========================

    def create_article(
        self,
        source_id,
        title,
        content,
        url
    ):

        existing = (
            self.db.query(Article)
            .filter(Article.url == url)
            .first()
        )

        if existing:
            return existing

        article = Article(
            source_id=source_id,
            title=title,
            content=content,
            url=url
        )

        self.db.add(article)
        self.db.commit()
        self.db.refresh(article)

        return article

    def get_recent_articles(
        self,
        limit=20
    ):

        return (
            self.db.query(Article)
            .order_by(
                Article.created_at.desc()
            )
            .limit(limit)
            .all()
        )

    def get_recent_articles_with_sources(
        self,
        limit=20
    ):

        return (
            self.db.query(
                Article,
                Source.name
            )
            .join(
                Source,
                Article.source_id == Source.id
            )
            .order_by(
                Article.created_at.desc()
            )
            .limit(limit)
            .all()
        )

    # =========================
    # DIGESTS
    # =========================

    def create_digest(
        self,
        title,
        summary,
        html_content
    ):

        digest = Digest(
            title=title,
            summary=summary,
            html_content=html_content
        )

        self.db.add(digest)
        self.db.commit()
        self.db.refresh(digest)

        return digest

    def get_latest_digest(self):

        return (
            self.db.query(Digest)
            .order_by(
                Digest.id.desc()
            )
            .first()
        )

    def digest_exists_today(self):

        today = datetime.utcnow().date()

        return (
            self.db.query(Digest)
            .filter(
                func.date(
                    Digest.created_at
                ) == today
            )
            .first()
        )