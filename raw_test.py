import psycopg2

try:
    conn = psycopg2.connect(
        host="127.0.0.1",
        port=5433,
        database="ai_news",
        user="admin",
        password="admin123"
    )

    print("SUCCESS")
    conn.close()

except Exception as e:
    print("FAILED")
print(e)