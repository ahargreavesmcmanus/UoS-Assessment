# Create a connection to MySQL
import os
import dotenv
import mysql.connector
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection

dotenv.load_dotenv()

SCHEMA = os.environ.get("SCHEMA_NAME")

def get_user() -> str:
    return os.environ.get("DB_USER")
def get_password() -> str:
    return os.environ.get("DB_PASS")
def get_host() -> str:
    return os.environ.get("DB_HOST")
def get_port() -> int:
    return int(os.environ.get("DB_PORT"))


def cnx() -> PooledMySQLConnection | MySQLConnectionAbstract:
    """
    Create and return a MySQL connection
    :return:
    """
    return mysql.connector.connect(
        user=get_user(),
        password=get_password(),
        host=get_host(),
        port=get_port(),
        consume_results=True
    )
