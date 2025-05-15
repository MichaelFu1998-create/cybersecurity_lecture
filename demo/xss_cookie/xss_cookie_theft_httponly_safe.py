from flask import Flask, request, make_response
import html

app = Flask(__name__)

@app.route('/')
def home():
    name = request.args.get('name', 'Guest')
    # ❌ XSS vulnerability: no sanitization
    response = f"<h1>Welcome, {name}</h1>"
    return response

@app.route('/set_cookie')
def set_cookie():
    resp = make_response("Cookie set with security!")
    # Set a cookie with HttpOnly, Secure, and SameSite
    resp.set_cookie(
        'XSSDemoSession', 'abc123',
        path='/',
        httponly=True,       # Prevent JS access
        secure=True,         # Only over HTTPS
        samesite='Strict'    # Prevent cross-site request leakage
    )
    return resp

@app.route('/favicon.ico')
def favicon():
    return '', 204  # No Content

if __name__ == '__main__':
    app.run(debug=True)
