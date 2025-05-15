# false_positive.py

def debug_test_query():
    query = "SELECT * FROM users WHERE id = " + "5"  # False positive — no user input (safe)
    cursor.execute(query)
