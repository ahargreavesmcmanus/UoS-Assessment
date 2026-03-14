# Create a connection to MySQL
import os
import dotenv
import mysql.connector

dotenv.load_dotenv()

def cnx():
    return mysql.connector.connect(
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASS"),
        host=os.environ.get("DB_HOST"),
        consume_results=True
    )
