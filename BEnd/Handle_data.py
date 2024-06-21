import logging
import mysql.connector
from mysql.connector import Error

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HandleData:
    def __init__(self):
        self.connection_sql = None
        self.cursor_sql = None
        self.data_sensor = {
            'temperature': 0,
            'humidity': 0,
            'pm1': 0,
            'pm25': 0,
            'pm10': 0,
            'co_value': 0,
            'max_value': 0,
            'level': 0,
            'date': '2021-01-01 00:00:00'
        }
        self.data_login = {
            'username': '',
            'password': ''
        }

    def connectSQL(self):
        try:
            self.connection_sql = mysql.connector.connect(
                host='localhost',
                user='root',
                password='123456',
                database='data_project_iot'  
            )
            if self.connection_sql.is_connected():
                self.cursor_sql = self.connection_sql.cursor()
                logging.info("SQL connection established")
            else:
                logging.error("Failed to establish SQL connection")
        except Error as e:
            logging.error(f"Error establishing SQL connection: {e}")

    def closeSQL(self):
        if self.connection_sql and self.connection_sql.is_connected():
            self.cursor_sql.close()
            self.connection_sql.close()
            logging.info("SQL connection closed")

    def select_sensor_data(self):
        select_query = "SELECT * FROM sensor_data"
        try:
            self.connectSQL()
            self.cursor_sql.execute(select_query)
            records = self.cursor_sql.fetchall()
            logging.info("Sensor data selected")
            for row in records:
                logging.info(row)
            return records
        except Error as e:
            logging.error(f"Error selecting sensor data: {e}")
        finally:
            self.closeSQL()

    def select_login_data(self):
        select_query = "SELECT * FROM users"
        try:
            self.connectSQL()
            self.cursor_sql.execute(select_query)
            records = self.cursor_sql.fetchall()
            logging.info("Login data selected")
            for row in records:
                logging.info(row)
            return records
        except Error as e:
            logging.error(f"Error selecting login data: {e}")
        finally:
            self.closeSQL()


handle_data = HandleData()
handle_data.connectSQL()
sensor_data_records = handle_data.select_sensor_data()
for record in sensor_data_records:
    print(record)

login_data_records = handle_data.select_login_data()
for record in login_data_records:
    print(record)
