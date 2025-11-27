import psycopg2

# подключение к базе
conn = psycopg2.connect(
    dbname="suppliers",  # твоя база
    user="tomiris",      # твой пользователь PostgreSQL
    host="localhost",
    port=5432
)

cur = conn.cursor()

# 1. Все контакты
cur.execute("SELECT * FROM phonebook")
print("All contacts:")
print(cur.fetchall())

# 2. Контакты с именем 'Tomiris'
cur.execute("SELECT * FROM phonebook WHERE first_name = %s", ("Tomiris",))
print("\nContacts with first name 'Tomiris':")
print(cur.fetchall())

# 3. Контакты с телефоном, который начинается на '8700'
cur.execute("SELECT * FROM phonebook WHERE phone LIKE '8700%'")
print("\nContacts with phone starting '8700':")
print(cur.fetchall())

cur.execute("DELETE FROM phonebook WHERE first_name = %s OR phone = %s", ("Aruzhan", "87005556677"))
conn.commit()


cur.close()
conn.close()
