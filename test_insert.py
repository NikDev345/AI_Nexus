from app.database.connection import SessionLocal
from app.database.repository import Repository


db = SessionLocal()

repo = Repository(db)

source = repo.create_source(
    name="OpenAI",
    url="https://openai.com",
    source_type="blog"
)

print(source.id)
print(source.name)