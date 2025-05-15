from flask import Flask, request, render_template_string
from datetime import datetime

app = Flask(__name__)
comments = []

@app.route("/", methods=["GET", "POST"])
def blog():
    if request.method == "POST":
        name = request.form.get("name", "Anonymous")
        text = request.form.get("comment")
        comments.append({
            "author": name,
            "text": text,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    # 🚨 Note: `comment.text|safe` is unsafe — allows XSS
    # When using |safe,
    # we are telling flask: “I trust this input. Don’t escape it. Render it as raw HTML.”
    # so now this comment "<script>alert('XSS')</script>"
    # will render in the browser as-is, "<script>alert('XSS')</script>"

    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Blog Post</title>
        <style>
            body { font-family: sans-serif; max-width: 600px; margin: auto; }
            .comment-box { border-top: 1px solid #ddd; padding: 10px 0; }
            .author { font-weight: bold; }
            .time { color: #888; font-size: 0.9em; }
        </style>
    </head>
    <body>
        <h1>📜 My Blog Post</h1>
        <p>This is a sample blog post where users can leave comments below.</p>

        <h2>💬 Leave a Comment</h2>
        <form method="POST">
            <input name="name" placeholder="Your name" required><br><br>
            <textarea name="comment" placeholder="Your comment" rows="4" cols="50" required></textarea><br><br>
            <button type="submit">Post Comment</button>
        </form>

        <h2>🗨️ Comments</h2>
        {% for comment in comments %}
            <div class="comment-box">
                <div class="author">{{ comment.author }}</div>
                <div class="time">{{ comment.time }}</div>
                <div class="text">{{ comment.text|safe }}</div>
            </div>
        {% endfor %}
    </body>
    </html>
    """, comments=comments)

if __name__ == "__main__":
    app.run(debug=True)
