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

# ✅ Safe: uses parameterized query
# ? symbols are placeholders for parameterized queries (also called prepared statements)
query = "SELECT * FROM users WHERE username = ? AND password = ?"
print("Running safe parameterized query")
cursor.execute(query, (username, password))

if cursor.fetchone():
    print("✅ Login successful")
else:
    print("❌ Login failed")

conn.close()
