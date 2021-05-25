from time import sleep

from player import PlayerClass


def main():
    input("Press ENTER to start")
    username = input("Enter username: ")

    p = PlayerClass(username)

    print(
        "\nYou awake in a small, dingy room. The walls are made of stone brick, and "
        "there are no windows."
    )
    sleep(2)
    while True:
        p.change_room()
        p.fight()
    # TODO Implement loop to make the above work
    # TODO Refactor starting commands into their own function?


if __name__ == "__main__":
    main()
