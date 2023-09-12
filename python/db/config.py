import pymysql
import os
from dotenv import load_dotenv

loaded = load_dotenv("../.env")
if not loaded: 
    exit("Not found .env file!")

def connect_to_mysql():
    conn = pymysql.connect(
        host=os.getenv("MYSQL_HOST"),
        port=int(os.getenv("MYSQL_PORT")),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASS"),
        database=os.getenv("MYSQL_NAME"),
    )
    return conn
