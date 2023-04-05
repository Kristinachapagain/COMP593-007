"""
Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
"""
import os
import inspect
import sqlite3
from faker import Faker
from datetime import datetime


def main():
    global db_path
    db_path = os.path.join(get_script_dir(), 'people.db')
    if os.path.exists(db_path):
        os.remove(db_path)
    create_people_table()
    populate_people_table()


def create_people_table():
    """Creates the people table in the database"""
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS people
                 (id INTEGER PRIMARY KEY,
                  first_name TEXT,
                  last_name TEXT,
                  age INTEGER,
                  email TEXT,
                  created_at TEXT,
                  updated_at TEXT)''')
    conn.commit()
    conn.close()
print("Database Base Created Successfully")


def populate_people_table():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    faker = Faker()
    for i in range(200):
        first_name = faker.first_name()
        last_name = faker.last_name()
        age = faker.random_int(min=1, max=100)
        email = faker.email()
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c.execute("INSERT INTO people (first_name, last_name, age, email, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)",
                  (first_name, last_name, age, email, created_at, updated_at))
    conn.commit()
    conn.close()
    print("All Data Inserted Successfully In The People Database")


def get_script_dir():
    """Determines the path of the directory in which this script resides

    Returns:
        str: Full path of the directory in which this script resides
    """
    script_path = os.path.abspath(
        inspect.getframeinfo(inspect.currentframe()).filename)
    return os.path.dirname(script_path)


if __name__ == '__main__':
    main()

