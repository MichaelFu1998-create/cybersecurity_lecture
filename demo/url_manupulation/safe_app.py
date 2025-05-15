from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated user database (in-memory)
users = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"},
    3: {"name": "Charlie", "email": "charlie@example.com"}
}

# Simulate logged-in user is user 1 (Alice)
LOGGED_IN_USER_ID = 1

@app.route('/secure_profile')
def secure_profile():
    user_id = int(request.args.get("user_id", 0))

    if user_id != LOGGED_IN_USER_ID:
        return "Unauthorized access", 403

    user_data = users.get(user_id)
    if user_data:
        return jsonify(user_data)
    else:
        return "User not found", 404

if __name__ == '__main__':
    app.run(debug=True)
