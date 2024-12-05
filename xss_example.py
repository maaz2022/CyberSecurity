# xss_example.py
from flask import Flask, request, render_template_string
from markupsafe import Markup

app = Flask(__name__)

# Simulated database of comments
comments = []

# Vulnerable route to XSS
@app.route('/vulnerable', methods=['GET', 'POST'])
def vulnerable():
    if request.method == 'POST':
        comment = request.form['comment']
        comments.append(comment)
    # Render comments without sanitization (vulnerable to XSS)
    return render_template_string('''
        <h1>Comments (Vulnerable)</h1>
        <form method="post">
            <textarea name="comment"></textarea>
            <input type="submit" value="Submit">
        </form>
        <ul>
            {% for comment in comments %}
                <li>{{ comment|safe }}</li>  <!-- Disable escaping to demonstrate vulnerability -->
            {% endfor %}
        </ul>
    ''', comments=comments)

# Secure route against XSS
@app.route('/secure', methods=['GET', 'POST'])
def secure():
    if request.method == 'POST':
        comment = request.form['comment']
        comments.append(comment)
    # Render comments with sanitization (secure against XSS)
    return render_template_string('''
        <h1>Comments (Secure)</h1>
        <form method="post">
            <textarea name="comment"></textarea>
            <input type="submit" value="Submit">
        </form>
        <ul>
            {% for comment in comments %}
                <li>{{ comment | e }}</li>  <!-- Escape output to prevent XSS -->
            {% endfor %}
        </ul>
    ''', comments=comments)

if __name__ == '__main__':
    app.run(debug=True)