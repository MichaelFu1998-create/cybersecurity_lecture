def get_user_data(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id  # Vulnerable to SQL Injection
    cursor.execute(query)