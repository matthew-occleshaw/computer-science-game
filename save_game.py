from __future__ import annotations  # FIXME Can be removed once python 3.10 comes out

from datetime import datetime
from json import dumps, loads
from sys import argv
from typing import TYPE_CHECKING, Optional

from item import items_dict
from location import locations_dict

if TYPE_CHECKING:
    from player import Player


def store_game_state(player: Player) -> None:
    try:
        open("game_saves.json", "x")
    except FileExistsError:
        with open("game_saves.json", "rt") as read_file:
            file_contents: str = read_file.read()
            file_data: list[dict] = loads(file_contents)
    else:
        file_data = []

    game_data: dict = vars(player)
    game_data["current_room"] = player.current_room.name
    game_data["backpack"] = [item.name for item in player.backpack]
    current_time = datetime.now()
    time_string = current_time.strftime("%H:%M:%S, %d/%m/%y")
    game_data["save_name"] = f"{player.username} @ {time_string}"
    file_data.append(game_data)
    with open("game_saves.json", "wt") as write_file:
        write_file.write(dumps(file_data))


def retrieve_game_state() -> Optional[dict]:
    with open("game_saves.json", "rt") as read_file:
        file_contents: str = read_file.read()
        file_data: list[dict] = loads(file_contents)
        saves: list[str] = [save["save_name"] for save in file_data]
    if saves:
        print("Saved games: ")
        for num, save in enumerate(saves):
            print(f"{num + 1}: {save}")
        selected_save_index: int = int(input("Enter save number: ")) - 1
        if selected_save_index == -1:
            print("Starting a new game.")
            return None
        selected_save: dict = file_data[selected_save_index]
        selected_save.pop("save_name")
        print("Save data: ")
        for key, value in selected_save.items():
            print(f"\t{key}: {value}")
        confirmation = bool(input("Does this look right? (y/n): ") == "y")
        if confirmation:
            selected_save["backpack"] = [
                items_dict[item]() for item in selected_save["backpack"]
            ]
            selected_save["current_room"] = locations_dict[
                selected_save["current_room"]
            ]
            file_data.pop(selected_save_index)
            with open("game_saves.json", "wt") as write_file:
                write_file.write(dumps(file_data))
            return selected_save
        else:
            print("Pick another save or type 0 for a new game: ")
            return retrieve_game_state()
    else:
        print("No saves available. Starting a new game.")
        return None


def reset_saves() -> None:
    if input("Are you sure (y/n): ") == "y":
        with open("game_saves.json", "wt") as file:
            file_data: list = []
            file.write(dumps(file_data))
        print("Game saves reset.")


def main() -> None:
    if len(argv) > 1 and argv[1] == "--reset":
        reset_saves()


if __name__ == "__main__":
    main()
