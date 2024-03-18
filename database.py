import json
import sqlite3
import random


class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

        self.words = []

    def create_table(self):
        """Создаем таблицу в базе данных для хранения данных."""
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS saved_data (
                                id INTEGER PRIMARY KEY,
                                data TEXT
                                )''')
        self.connection.commit()

    def insert_data(self, data):
        data_json = json.dumps(data)
        self.cursor.execute("INSERT INTO saved_data (data) VALUES (?)", (data_json,))
        self.connection.commit()

    def get_random_word(self):
        return random.choice(self.words) if self.words else ("", "")

    def add_word(self, english, russian):

        self.words.append((english, russian))


