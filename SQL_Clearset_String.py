import sqlite3

# Connect to the SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Creating the 'users' table if it doesn't exist (prevents OperationalError)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')

# Insert some sample data into the 'users' table (if not already inserted)
cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Alice', 30))
cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Bob', 25))
conn.commit()  # Save (commit) the changes

# Secure query using prepared statements to avoid SQL injection
user_id = 1  # User input (could come from a web form or API request)
cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))  # Prevents SQL injection

# Fetch and print the result
user = cursor.fetchone()
if user:
    print(f"User ID {user[0]}: Name = {user[1]}, Age = {user[2]}")
else:
    print("No user found with the given ID.")

# Close the database connection
conn.close()
