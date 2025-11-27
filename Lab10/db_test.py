import psycopg2

conn = psycopg2.connect(
    dbname="suppliers",  
    user="tomiris",
    host="localhost",
    port=5432
)

cur = conn.cursor()

# Вставка
cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", ("Dana", "dana@example.com"))
conn.commit()

# Выбор
cur.execute("SELECT * FROM users")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()
