import mysql.connector
from mysql.connector import Error

# Initialize connection variable
connection = None

try:
    # Replace with your database credentials
    connection = mysql.connector.connect(
        host='localhost',        # e.g., 'localhost' or an IP address
        port='3306',             # MySQL port
        database='anu',          # Ensure this database exists
        user='root',
        password='vIVEK@1121'
    )

    if connection.is_connected():
        print("Successfully connected to the database")

except Error as e:
    print("Error while connecting to MySQL:", e)

finally:
    if connection and connection.is_connected():  # Check if connection was successful
        connection.close()
        print("MySQL connection is closed")
