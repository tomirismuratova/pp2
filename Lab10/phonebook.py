import psycopg2
import csv

# connect to DB
conn = psycopg2.connect(dbname="suppliers", user="tomiris", host="localhost", port=5432)
cur = conn.cursor()

# create table
cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    phone VARCHAR(20) NOT NULL UNIQUE
)
""")
conn.commit()

def add_contact_console():
    fn = input("First name: ")
    ln = input("Last name: ")
    ph = input("Phone: ")
    cur.execute("INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s,%s,%s) ON CONFLICT (phone) DO NOTHING", (fn, ln, ph))
    conn.commit()
    print("Added.")

def add_contacts_csv():
    try:
        with open('Lab10/contacts.csv', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cur.execute("INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s,%s,%s) ON CONFLICT (phone) DO NOTHING",
                            (row['first_name'], row['last_name'], row['phone']))
        conn.commit()
        print("CSV uploaded.")
    except FileNotFoundError:
        print("contacts.csv not found.")

def update_contact():
    fn = input("First name to update: ")
    new_ph = input("New phone: ")
    cur.execute("UPDATE phonebook SET phone=%s WHERE first_name=%s", (new_ph, fn))
    conn.commit()
    print("Updated.")

def show_contacts():
    print("\nAll contacts:")
    cur.execute("SELECT * FROM phonebook")
    for r in cur.fetchall(): print(r)

def filter_by_name():
    name = input("Filter by first name: ")
    cur.execute("SELECT * FROM phonebook WHERE first_name=%s", (name,))
    for r in cur.fetchall(): print(r)

def filter_by_phone():
    pattern = input("Filter phone starting with: ")
    cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", (pattern+'%',))
    for r in cur.fetchall(): print(r)

def delete_contact():
    key = input("Delete by name or phone: ")
    cur.execute("DELETE FROM phonebook WHERE first_name=%s OR phone=%s", (key, key))
    conn.commit()
    print("Deleted.")

# menu loop
while True:
    print("\n PhoneBook Menu ")
    print("1. Add contact (console)")
    print("2. Add contacts from CSV")
    print("3. Update contact")
    print("4. Show all contacts")
    print("5. Filter by name")
    print("6. Filter by phone")
    print("7. Delete contact")
    print("0. Exit")
    
    choice = input("Choose option: ")
    
    if choice == '1': add_contact_console()
    elif choice == '2': add_contacts_csv()
    elif choice == '3': update_contact()
    elif choice == '4': show_contacts()
    elif choice == '5': filter_by_name()
    elif choice == '6': filter_by_phone()
    elif choice == '7': delete_contact()
    elif choice == '0': break
    else: print("Invalid choice.")

cur.close()
conn.close()
print("Goodbye!")
