from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def home():
    name = request.args.get('name', 'Guest')
    # ❌ XSS vulnerability: directly injecting input
    response = f"<h1>Welcome, {name}</h1>"
    return response

@app.route('/set_cookie')
def set_cookie():
    resp = make_response("Cookie set!")
    # Set a cookie without HttpOnly or Secure
    resp.set_cookie('XSSDemoSession', 'abc123')
    return resp

@app.route('/favicon.ico')
def favicon():
    return '', 204  # No Content

if __name__ == '__main__':
    app.run(debug=True)
