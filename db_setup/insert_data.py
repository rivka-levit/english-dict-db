import mysql.connector
from mysql.connector.errors import IntegrityError

import os
import json

from dotenv import load_dotenv

load_dotenv()

with open('data.json') as file:
    data = json.load(file)

conn = mysql.connector.connect(
        host="localhost",
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASS'),
        database=os.environ.get('DB_NAME')
    )
cursor = conn.cursor()
conn.autocommit = True

for w, dfs in data.items():
    try:
        cursor.execute('INSERT INTO words (word) VALUES (%s)', (w,))
    except IntegrityError:
        pass

    cursor.execute('SELECT * FROM words WHERE word = %s', (w,))
    w_id = cursor.fetchone()[0]

    for d in dfs:
        sql = ('INSERT INTO definitions (definition, word_id) '
               'VALUES (%s, %s)')
        cursor.execute(sql, (d, w_id))
