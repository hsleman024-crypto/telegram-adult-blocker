import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT NOT NULL
        )''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS blacklist (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            reason TEXT,
            FOREIGN KEY (user_id) REFERENCES users (user_id)
        )''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS whitelist (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            reason TEXT,
            FOREIGN KEY (user_id) REFERENCES users (user_id)
        )''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS logs (
            log_id INTEGER PRIMARY KEY,
            action TEXT,
            user_id INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (user_id)
        )''')
        self.conn.commit()

    def add_user(self, username):
        self.cursor.execute('INSERT INTO users (username) VALUES (?)', (username,))
        self.conn.commit()

    def add_to_blacklist(self, user_id, reason):
        self.cursor.execute('INSERT INTO blacklist (user_id, reason) VALUES (?, ?)', (user_id, reason))
        self.conn.commit()

    def add_to_whitelist(self, user_id, reason):
        self.cursor.execute('INSERT INTO whitelist (user_id, reason) VALUES (?, ?)', (user_id, reason))
        self.conn.commit()

    def log_action(self, action, user_id):
        self.cursor.execute('INSERT INTO logs (action, user_id) VALUES (?, ?)', (action, user_id))
        self.conn.commit()

    def close(self):
        self.conn.close()