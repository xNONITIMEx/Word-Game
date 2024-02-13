import sqlite3 as sql

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def get_words():
    conn = sql.connect('data.sqlite')
    cursor = conn.cursor()
    words = dict()

    for i in alphabet:
        cursor.execute(f'select word from nouns where word like "{i}%"')
        raw_data = cursor.fetchall()
        words[i] = [i[0] for i in raw_data]
    conn.close()
    return words


def find_word(word):
    conn = sql.connect('data.sqlite')
    cursor = conn.cursor()
    cursor.execute(f'select word from nouns where word = "{word}"')
    result = True if len(cursor.fetchall()) != 0 else False
    conn.close()
    return result
