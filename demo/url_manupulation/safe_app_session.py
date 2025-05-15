from flask import Flask, session, jsonify, redirect, url_for

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed to use sessions

# Fake database
users = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"}
}

# Fake login route
@app.route('/login/<int:user_id>')
def login(user_id):
    if user_id in users:
        session['user_id'] = user_id
        return f"Logged in as user {user_id}"
    return "User not found", 404

# Secure profile route — no ID in URL
@app.route('/profile')
def profile():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login', user_id=1))  # default login for demo

    user_data = users.get(user_id)
    if user_data:
        return jsonify(user_data)
    else:
        return "User not found", 404

# Logout
@app.route('/logout')
def logout():
    session.clear()
    return "Logged out"

if __name__ == '__main__':
    app.run(debug=True)
