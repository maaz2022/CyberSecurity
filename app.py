from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Setup SQLite database
def init_db():
    conn = sqlite3.connect('simple.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', ('admin', 'password'))
    conn.commit()
    conn.close()

init_db()

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    conn = sqlite3.connect('simple.db')
    c = conn.cursor()
    
    # Vulnerable query (initially)
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    c.execute(query)
    
    user = c.fetchone()
    conn.close()
    
    if user:
        return jsonify({'message': 'Login successful!'})
    else:
        return jsonify({'message': 'Login failed!'}), 401

if __name__ == '__main__':
    app.run(debug=True)
