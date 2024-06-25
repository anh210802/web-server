import logging
import sys
import sqlite3
import hashlib

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class SQLite:
    def __init__(self, fileName):
        self.conn = None
        self.cursor = None
        self.fileName = fileName

    def connectSQL(self):
        try:
            self.conn = sqlite3.connect(self.fileName)
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

    def getDataSensor(self):
        if not self.cursor:
            logging.error("Cursor is not initialized. Make sure the database connection was successful.")
            return None
        
        try:
            self.cursor.execute("SELECT * FROM sensor_data ")
            result = self.cursor.fetchall()
            return result
        except sqlite3.Error as e:
            logging.error(f"Error executing query: {e}")
            return None
        
    def showRealTimeData(self):
        if not self.cursor:
            logging.error("Cursor is not initialized. Make sure the database connection was successful.")
            return None
        
        try:
            self.cursor.execute("SELECT * FROM sensor_data ORDER BY id DESC LIMIT 1")
            result = self.cursor.fetchone()
            return result
        except sqlite3.Error as e:
            logging.error(f"Error executing query: {e}")
            return None
        

# # Test the SQLite class
# if __name__ == "__main__":
#     db = SQLite('data_sql.sqlite')
#     db.connectSQL()
#     print(db.isLogin('admin', 'admin'))
#     print(db.isLogin('admin', 'admin1'))
#     print(db.isLogin('admin1', 'admin'))
#     print(db.getDataSensor())


    

    
