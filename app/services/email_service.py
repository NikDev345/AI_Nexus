import os
import smtplib

from dotenv import load_dotenv

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from app.database.connection import SessionLocal
from app.database.repository import Repository

load_dotenv()


def send_latest_digest():

    db = SessionLocal()
    repo = Repository(db)

    digest = repo.get_latest_digest()

    sender_email = os.getenv("EMAIL_ADDRESS")
    app_password = os.getenv("EMAIL_PASSWORD")

    receiver_email = sender_email

    msg = MIMEMultipart("alternative")

    msg["Subject"] = digest.title
    msg["From"] = sender_email
    msg["To"] = receiver_email

    html_part = MIMEText(
        digest.html_content,
        "html"
    )

    msg.attach(html_part)

    with smtplib.SMTP(
        "smtp.gmail.com",
        587
    ) as server:

        server.starttls()

        server.login(
            sender_email,
            app_password
        )

        server.sendmail(
            sender_email,
            receiver_email,
            msg.as_string()
        )

    db.close()

    print("Email sent successfully.")