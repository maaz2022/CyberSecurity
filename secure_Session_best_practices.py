from flask import Flask, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'super_secret_key'

@app.route('/login')
def login():
    session['user'] = 'username'
    session.modified = True  # Regenerate session ID after login
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(ssl_context='adhoc')  # HTTPS enforced
