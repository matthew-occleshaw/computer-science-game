from time import sleep

from location import l1
from player import PlayerClass


def main():
    p = PlayerClass(l1)

    input("Press ENTER to start")
    username = input("Enter username: ")
    print(
        "\nYou awake in a small, dingy room. The walls are made of stone brick, and "
        "there are no windows."
    )
    sleep(2)
    p.change_room()
    p.fight()
    # TODO Implement loop to make the above work
    # TODO Refactor starting commands into their own function?


if __name__ == "__main__":
    main()
