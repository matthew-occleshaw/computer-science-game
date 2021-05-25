import sqlite3 as sql
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
            primary_key INTEGER PRIMARY KEY DESC,
            username TEXT
        )"""
            # TODO Add more fields to leaderboard table
        )


@connect_to_db
def get_data(c):
    pass
    # TODO Implement get data function


@connect_to_db
def insert_record(c):
    pass
    # TODO Implement record insertion


def main():
    reset_db()


if __name__ == "__main__":
    main()
