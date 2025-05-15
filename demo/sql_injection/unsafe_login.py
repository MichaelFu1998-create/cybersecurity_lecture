import sqlite3

# Create an in-memory database
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Create table and insert a real user
cursor.execute("CREATE TABLE users (username TEXT, password TEXT)")
cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'supersecret')")

# Simulated login input
username = input("Username: ")
password = input("Password: ")

# ❌ Vulnerable: unsanitized string concatenation
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
print(f"Running query: {query}")
cursor.execute(query)

if cursor.fetchone():
    print("✅ Login successful")
else:
    print("❌ Login failed")

conn.close()
