# test_saved_digest.py

from app.database.connection import SessionLocal
from app.database.models import Digest

db = SessionLocal()

digests = db.query(Digest).all()

for digest in digests:
    print("\nTITLE:")
    print(digest.title)

    print("\nSUMMARY:")
    print(digest.summary[:500])

db.close()