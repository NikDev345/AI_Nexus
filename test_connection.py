from sqlalchemy import text

from app.database.connection import engine, DATABASE_URL

print("DATABASE_URL =", DATABASE_URL)

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))

        print("Database Connected Successfully")
        print(result.fetchone())

except Exception as e:
    print("Connection Failed")
    print(e)