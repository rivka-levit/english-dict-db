import mysql.connector
import os

from dotenv import load_dotenv

load_dotenv()

conn = mysql.connector.connect(
  host="localhost",
  user=os.environ.get('DB_USER'),
  password=os.environ.get('DB_PASS'),
  database=os.environ.get('DB_NAME')
)
cursor = conn.cursor()

table_1_sql = """CREATE TABLE IF NOT EXISTS words (
id INT PRIMARY KEY AUTO_INCREMENT,
word VARCHAR(300) UNIQUE
)"""
cursor.execute(table_1_sql)

table_2_sql = """CREATE TABLE IF NOT EXISTS definitions (
id INT PRIMARY KEY AUTO_INCREMENT,
definition TEXT,
word_id INT,
FOREIGN KEY (word_id) REFERENCES words(id) ON DELETE CASCADE
)"""
cursor.execute(table_2_sql)

word_idx = """CREATE INDEX word_idx ON words (word)"""
cursor.execute(word_idx)
