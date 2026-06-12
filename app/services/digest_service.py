import os
import time
import markdown

from dotenv import load_dotenv
from datetime import datetime

# Gemini SDK
try:
    from google import genai
except Exception:
    import google.genai as genai

from app.database.connection import SessionLocal
from app.database.repository import Repository
from app.templates.digest_template import create_html_digest

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_digest():

    db = SessionLocal()
    repo = Repository(db)

    try:

        # Fetch latest articles
        articles = repo.get_recent_articles(20)


        article_text = ""

        # Build a plain-text block of recent articles. Handle cases where
        # repo.get_recent_articles returns either a list of Article objects
        # or a list of (article, source_name) tuples.
        for item in articles:
            if isinstance(item, tuple) and len(item) == 2:
                article, source_name = item
            else:
                article = item
                source_name = "Unknown Source"

            article_text += f"""
Source: {source_name}
Title: {article.title}
URL: {article.url}

"""

        today = datetime.now().strftime("%d %B %Y")

        # Prompt
        prompt = f"""
You are an expert AI technology newsletter editor.

Today's date is {today}.

CRITICAL RULES:

- Do NOT generate a date section.
- Do NOT invent any dates.
- The system already displays the date.
- Use Markdown formatting only.
- Use headings (#, ##, ###).
- Use bullet points.
- Use bold text where appropriate.
- Mention source names whenever possible.
- Mention source URLs when relevant.
- Group similar stories together.
- Keep the newsletter concise and professional.
- End with a short conclusion.

News Data:

{article_text}

Output Structure:

# AI Daily Digest

## Executive Summary

(2-3 paragraph summary)

## Major AI Model Updates

(stories)

## Research & Breakthroughs

(stories)

## Industry & Business Developments

(stories)

## Interesting Insights

(stories)

## Sources

- Source Name — URL

## Conclusion

(short conclusion)
"""

        # Retry Gemini if busy
        response = None

        for attempt in range(3):

            try:

                response = client.models.generate_content(
                    model="gemini-2.5-flash-lite",
                    contents=prompt
                )

                break

            except Exception as e:

                print(
                    f"Gemini attempt {attempt + 1} failed: {e}"
                )

                time.sleep(5)

        if response is None:
            raise Exception(
                "Gemini unavailable after 3 attempts."
            )

        summary_text = (
            getattr(response, "text", None)
            or str(response)
        )

        # Convert Markdown -> HTML
        formatted_html = markdown.markdown(
            summary_text,
            extensions=[
                "extra",
                "nl2br"
            ]
        )

        # Build final email HTML
        html_digest = create_html_digest(
            formatted_html
        )

        # Save local HTML file
        with open(
            "daily_digest.html",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(html_digest)

        print(
            "HTML digest created successfully."
        )

        print(
            "\n===== DAILY DIGEST =====\n"
        )

        print(summary_text)

        # Save to database
        digest = repo.create_digest(
            title="AI Daily Digest",
            summary=summary_text,
            html_content=html_digest
        )

        print(
            f"\nDigest saved successfully. ID={digest.id}"
        )

    except Exception as e:

        print(
            f"\nError generating digest: {e}"
        )

    finally:

        db.close()  