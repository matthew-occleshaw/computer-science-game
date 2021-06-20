import sqlite3 as sql
from sqlite3 import Connection, Cursor
from sys import argv
from typing import Any, Callable, TypeVar, cast

from tabulate import tabulate

decorator_type = TypeVar("decorator_type", bound=Callable[..., Any])


def connect_to_db(func: decorator_type) -> decorator_type:
    def inner(*args: list, **kwargs: dict) -> Any:
        connection: Connection = sql.connect("leaderboard.db")
        cursor: Cursor = connection.cursor()
        return_value: Any = func(cursor, *args, **kwargs)
        connection.commit()
        return return_value

    return cast(decorator_type, inner)


@connect_to_db
def reset_db(c: Cursor) -> None:
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
def get_data(c: Cursor) -> str:
    c.execute("""SELECT username, final_health FROM leaderboard""")
    results = c.fetchall()
    table: str = tabulate(
        results, headers=["Username", "Final Health"], tablefmt="simple"
    )
    return table


@connect_to_db
def insert_record(c: Cursor, username: str, final_health: int) -> None:
    query = """INSERT INTO leaderboard (username, final_health) VALUES (?, ?)"""
    args = (username, final_health)
    c.execute(query, args)


def main() -> None:
    if len(argv) > 1:
        if argv[1] == "--reset":
            reset_db()  # type: ignore[call-arg]
        elif argv[1] == "--get-data":
            print(get_data())  # type: ignore[call-arg]


if __name__ == "__main__":
    main()
