
import os
import inspect 
import sqlite3
import pandas as pd
import pprint


def main():
    global db_path
    script_dir = get_script_dir()
    db_path = os.path.join(script_dir, 'people.db')

    # Get the names and ages of all old people
    old_people_list = get_old_people()

    # Print the names and ages of all old people
    print_name_and_age(old_people_list)

    # Save the names and ages of all old people to a CSV file
    old_people_csv = os.path.join(script_dir, 'old_people.csv')
    save_name_and_age_to_csv(old_people_list, old_people_csv)

def get_old_people():
    """Queries the Social Network database for all people who are at least 50 years old.

    Returns:
        list: (name, age) of old people 
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT first_name, last_name, age FROM people WHERE age >= 50")
    old_people = cursor.fetchall()
    conn.close()
    print(f"{len(old_people)} old people found.")
    return old_people

def print_name_and_age(name_and_age_list):
    """Prints name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
    """
    pprint.pprint(name_and_age_list)


def save_name_and_age_to_csv(name_and_age_list, csv_path):
    """Saves name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
        csv_path (str): Path of CSV file
    """
    # if file exists, delete it
    if os.path.exists(csv_path):
        os.remove(csv_path)
    df = pd.DataFrame(name_and_age_list, columns=['first_name', 'last_name', 'age'])
    df.to_csv(csv_path, index=False)
    print(f"Saved {len(name_and_age_list)} old people to {csv_path}.")

def get_script_dir():
    """Determines the path of the directory in which this script resides

    Returns:
        str: Full path of the directory in which this script resides
    """
    script_path = os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)
    return os.path.dirname(script_path)

if __name__ == '__main__':
   main()