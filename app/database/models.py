from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey
)

from datetime import datetime


class Base(DeclarativeBase):
    pass


class Source(Base):
    __tablename__ = "sources"

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)

    url = Column(String, nullable=False)

    source_type = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)

    source_id = Column(
        Integer,
        ForeignKey("sources.id")
    )

    title = Column(String)

    content = Column(Text)

    url = Column(
        String,
        nullable=False,
        unique=True
    )

    published_at = Column(DateTime)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


class Digest(Base):
    __tablename__ = "digests"

    id = Column(Integer, primary_key=True)

    title = Column(String)

    summary = Column(Text)

    # NEW COLUMN
    html_content = Column(Text)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )