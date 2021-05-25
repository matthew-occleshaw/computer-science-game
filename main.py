from time import sleep

from player import PlayerClass


def start():
    input("Press ENTER to start")
    username = input("Enter username: ")
    player = PlayerClass(username)
    print(
        "\nYou awake in a small, dingy room. The walls are made of stone brick, and "
        "there are no windows."
    )
    sleep(2)
    return player


def main():
    p = start()
    while True:
        p.change_room()
        p.fight()
        # TODO Add option to use items post fight (possibly make menu
        #   instead of having everything automatically moving forward)
        p.look_for_items()


if __name__ == "__main__":
    main()
