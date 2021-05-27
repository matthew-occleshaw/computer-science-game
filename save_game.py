from json import loads, dumps
from datetime import datetime
from sys import argv

from item import items_dict
from location import locations_dict


def store_game_state(player):
    try:
        open("game_saves.json", "x")
    except FileExistsError:
        with open("game_saves.json", "rt") as read_file:
            file_contents = read_file.read()
            file_data = loads(file_contents)
    else:
        file_data = []

    game_data = vars(player)
    game_data["current_room"] = player.current_room.room_name
    game_data["backpack"] = [item.name for item in player.backpack]
    current_time = datetime.now()
    time_string = current_time.strftime("%H:%M:%S, %d/%m/%y")
    game_data["save_name"] = f"{player.username} @ {time_string}"
    file_data.append(game_data)
    with open("game_saves.json", "wt") as write_file:
        write_file.write(dumps(file_data))


def retrieve_game_state():
    with open("game_saves.json", "rt") as read_file:
        file_contents = read_file.read()
        file_data = loads(file_contents)
        saves = [save["save_name"] for save in file_data]
    if saves:
        print("Saved games: ")
        for num, save in enumerate(saves):
            print(f"{num + 1}: {save}")
        selected_save = file_data[int(input("Enter save number: ")) - 1]
        selected_save.pop("save_name")
        selected_save["backpack"] = [
            items_dict[item]() for item in selected_save["backpack"]
        ]
        selected_save["current_room"] = locations_dict[selected_save["current_room"]]
        return selected_save
    else:
        print("No saves available. Starting a new game.")
        return None

    pass
    # TODO Implement way for saves to be deleted after they have been retrieved
    # (stop things clogging up)


def reset_saves():
    if input("Are you sure (y/n): ") == "y":
        with open("game_saves.json", "wt") as file:
            file_data = []
            file.write(dumps(file_data))
        print("Game saves reset.")


def main():
    if len(argv) > 1 and argv[1] == "--reset":
        reset_saves()


if __name__ == "__main__":
    main()
