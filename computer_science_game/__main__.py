from time import sleep
from typing import Optional

from player import Player
from save_game import retrieve_game_state


def start() -> Player:
    start_mode: int = int(input("NEW GAME (1) or OPEN SAVE (2): "))
    if start_mode == 1:
        return new_game()
    elif start_mode == 2:
        player_args: Optional[dict] = retrieve_game_state()
        if player_args is not None:
            player: Player = Player(**player_args)
            print("Save data retrieved: \n")
            player.change_room()
            return player
        else:
            return new_game()
    else:
        print("Not a valid option, please try again.")
        return start()


def new_game() -> Player:
    username: str = input("Enter username: ")
    player: Player = Player(username)
    print(
        "\nYou awake in a small, dingy room. The walls are made of stone brick, "
        "and there are no windows."
    )
    sleep(2)
    player.change_room()
    return player


def main() -> None:
    input("Press ENTER to start")
    player: Player = start()
    while True:
        player.fight()
        player.menu()


if __name__ == "__main__":
    main()
