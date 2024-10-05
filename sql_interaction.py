import sqlite3

def connect_db(db_name="sample.db"):
    try:
        conn = sqlite3.connect(db_name)
        print("successful connected!")
        return conn
    except sqlite3.Error as e:
        print(f"error while connecting to database: {e}")
        return None
    
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   age INTEGER NOT NULL
                   );
                   '''
                   )
    conn.commit()

def insert_user(conn, name: str, age: int):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()

def read_users(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def update_user_age(conn, user_id, new_age):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET age = ? WHERE id = ?", (new_age, user_id))
    conn.commit()

def delete_user(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()

def custom_queries(conn):
    cursor = conn.cursor()

    # First query: Get users older than 25

    age_threshold = 25
    cursor.execute("SELECT * FROM users WHERE age > ?", (age_threshold,))
    result = cursor.fetchall()
    for user in result:
        print(user)

    # Second query: Count number of users in the table
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]
    print(f"Total users: {count}")


if __name__ == "__main__":
    conn = connect_db()
    if conn:
        create_table(conn)
        insert_user(conn, "Alice", 30)
        insert_user(conn, "Bob", 22)
        read_users(conn)
        update_user_age(conn, 1, 35)
        delete_user(conn, 2)
        custom_queries(conn)
        conn.close()