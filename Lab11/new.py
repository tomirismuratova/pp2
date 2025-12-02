import psycopg2
import csv
import re

conn = psycopg2.connect(dbname="suppliers", user="tomiris", host="localhost", port=5432)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    phone VARCHAR(20) NOT NULL UNIQUE
);
""")
conn.commit()

# pattern search
def search_pattern():
    pat = input("Enter pattern: ")
    pattern = "%" + pat + "%"
    cur.execute("""
        SELECT * FROM phonebook
        WHERE first_name ILIKE %s 
           OR last_name ILIKE %s
           OR phone LIKE %s
    """, (pattern, pattern, pattern))
    for row in cur.fetchall():
        print(row)


# add user
def add_or_update():
    fn = input("First name: ")
    ln = input("Last name: ")
    ph = input("Phone: ")

    # update
    cur.execute("UPDATE phonebook SET phone=%s WHERE first_name=%s", (ph, fn))

    if cur.rowcount == 0:  # если никто не обновился вставляем нового
        cur.execute(
            "INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s,%s,%s)",
            (fn, ln, ph)
        )

    conn.commit()
    print("Saved.")


# add many users
def add_many():
    bad_numbers = []
    print("Enter many contacts. Write 'stop' to finish.")

    while True:
        fn = input("First name: ")
        if fn == "stop":
            break

        ln = input("Last name: ")
        ph = input("Phone: ")

        # проверка на корректность
        if not re.fullmatch(r"\d{10,12}", ph):
            bad_numbers.append((fn, ln, ph))
            continue

        cur.execute("UPDATE phonebook SET phone=%s WHERE first_name=%s", (ph, fn))

        if cur.rowcount == 0:
            cur.execute(
                "INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s,%s,%s)",
                (fn, ln, ph)
            )

        conn.commit()

    print("Incorrect phone numbers:")
    for b in bad_numbers:
        print(b)


# pagination
def pagination():
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))

    cur.execute("SELECT * FROM phonebook ORDER BY id LIMIT %s OFFSET %s", (limit, offset))

    for row in cur.fetchall():
        print(row)


# delete
def delete_user():
    k = input("Enter name or phone to delete: ")
    cur.execute("DELETE FROM phonebook WHERE first_name=%s OR phone=%s", (k, k))
    conn.commit()
    print("Deleted.")


# menu
while True:
    print("\nPhoneBook Menu")
    print("1. Search by pattern")
    print("2. Add or update user")
    print("3. Add MANY users (with validation)")
    print("4. Show paginated")
    print("5. Delete")
    print("0. Exit")

    choice = input("Choose: ")

    if choice == "1": search_pattern()
    elif choice == "2": add_or_update()
    elif choice == "3": add_many()
    elif choice == "4": pagination()
    elif choice == "5": delete_user()
    elif choice == "0": break
    else:
        print("Invalid.")

cur.close()
conn.close()
print("Goodbye!")
