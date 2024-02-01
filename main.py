import mysql.connector
import os

from dotenv import load_dotenv

load_dotenv()


def get_definitions(word: str) -> list:
    """Retrieve definitions of the word from database."""

    conn = mysql.connector.connect(
        host="localhost",
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASS'),
        database=os.environ.get('DB_NAME')
    )
    cursor = conn.cursor()
    conn.autocommit = True

    sql = """
        SELECT d.definition
        FROM definitions AS d
        INNER JOIN words AS w ON d.word_id = w.id
        WHERE w.word = %s;
        """
    cursor.execute(sql, (word.lower(),))
    results = cursor.fetchall()

    return [i[0] for i in results]


while True:
    wd = input('Enter a word ("q" to quit): ')

    if wd == 'q':
        break
    else:
        definitions = get_definitions(wd)

        if definitions:
            for item in definitions:
                print(item)
            print()
        else:
            print('No definitions')
