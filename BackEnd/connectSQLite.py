import logging
import sys
import sqlite3
import hashlib

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class SQLite:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connectSQL(self):
        try:
            self.conn = sqlite3.connect("BackEnd/data_sql.db")
            self.cursor = self.conn.cursor()
            logging.debug("Connected to the database successfully.")
        except sqlite3.Error as e:
            logging.error(f"Error connecting to database: {e}")
            self.conn = None
            self.cursor = None
            sys.exit(1)

    def isLogin(self, username, password):
        if not self.cursor:
            logging.error("Cursor is not initialized. Make sure the database connection was successful.")
            return False
        
        passed = hashlib.sha256(password.encode()).hexdigest()
        try:
            self.cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, passed))
            result = self.cursor.fetchone()
            if result:
                logging.debug("Login successful.")
                return True
            else:
                logging.debug("Login failed: Invalid username or password.")
                return False
        except sqlite3.Error as e:
            logging.error(f"Error executing query: {e}")
            return False

    def closeSQL(self):
        if self.cursor:
            self.cursor.close()
            logging.debug("Cursor closed.")
        if self.conn:
            self.conn.close()
            logging.debug("Connection closed.")

# if __name__ == '__main__':
#     db = SQLite()
#     db.connectSQL()
#     if db.isLogin("admin", "admin"):
#         print("Login successful!")
#     else:
#         print("Login failed!")
#     db.closeSQL()
