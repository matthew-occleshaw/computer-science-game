from location import l1
from player import PlayerClass


def main():
    p0 = PlayerClass(l1)

    input("Press ENTER to start")
    username = input("Enter username: ")
    print(
        "\nYou awake in a small, dingy room "
        "The walls are made of stone brick, and there are no windows "
        "However, there is one doorway on the other side of the room, "
        "which you walk through",
        sep="\n",
        end="",
    )

    p0.fight()


if __name__ == "__main__":
    main()
