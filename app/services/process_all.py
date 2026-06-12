from app.services.process_openai import process_openai
from app.services.process_anthropic import process_anthropic
from app.services.process_youtube import process_youtube


def process_all():

    process_openai()
    process_anthropic()
    process_youtube()

    print("All sources processed successfully.")