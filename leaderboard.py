import sqlite3 as sql
from sys import argv

from tabulate import tabulate


def connect_to_db(func):
    def inner(*args, **kwargs):
        connection = sql.connect("leaderboard.db")
        cursor = connection.cursor()
        func(cursor, *args, **kwargs)
        connection.commit()

    return inner


@connect_to_db
def reset_db(c):
    if input("Are you sure (y/n): ") == "y":
        c.execute("""DROP TABLE IF EXISTS leaderboard""")
        print("Table dropped")
        c.execute(
            """CREATE TABLE leaderboard (
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            final_health INTEGER
        )"""
            # TODO Add more fields to leaderboard table
        )
        print("Table created")


@connect_to_db
def get_data(c):
    c.execute("""SELECT username, final_health FROM leaderboard""")
    results = c.fetchall()
    table = tabulate(results, headers=["Username", "Final Health"], tablefmt="github")
    print(table)


@connect_to_db
def insert_record(c, username, final_health):
    query = """INSERT INTO leaderboard (username, final_health) VALUES (?, ?)"""
    args = (username, final_health)
    c.execute(query, args)


def main():
    if len(argv) > 1:
        if argv[1] == "--reset":
            reset_db()
        elif argv[1] == "--get-data":
            get_data()


if __name__ == "__main__":
    main()
