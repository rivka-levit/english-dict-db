import mysql.connector
import os

from dotenv import load_dotenv

load_dotenv()

conn = mysql.connector.connect(
  host="localhost",
  user=os.environ.get('DB_USER'),
  password=os.environ.get('DB_PASS')
)

cursor = conn.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS dictionary')
