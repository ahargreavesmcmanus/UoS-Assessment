# Create a connection to MySQL
import os
import dotenv
import mysql.connector

dotenv.load_dotenv()

SCHEMA = os.environ.get("SCHEMA_NAME")

def cnx():
    return mysql.connector.connect(
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASS"),
        host=os.environ.get("DB_HOST"),
        consume_results=True
    )
