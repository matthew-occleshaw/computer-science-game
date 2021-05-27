from time import sleep

from player import PlayerClass
from save_game import retrieve_game_state


def start():
    start_mode = int(input("NEW GAME (1) or OPEN SAVE (2): "))
    if start_mode == 1:
        return new_game()
    elif start_mode == 2:
        player_args = retrieve_game_state()
        if player_args is not None:
            player = PlayerClass(**player_args)
            print("Save data retrieved: \n")
            player.change_room()
            return player
        else:
            return new_game()
    else:
        print("Not a valid option, please try again.")
        start()


def new_game():
    username = input("Enter username: ")
    player = PlayerClass(username)
    print(
        "\nYou awake in a small, dingy room. The walls are made of stone brick, "
        "and there are no windows."
    )
    sleep(2)
    player.change_room()
    return player


def main():
    input("Press ENTER to start")
    player = start()
    while True:
        player.fight()
        player.menu()


if __name__ == "__main__":
    main()
