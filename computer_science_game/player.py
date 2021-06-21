from __future__ import annotations  # FIXME Can be removed once python 3.10 comes out

from random import randint
from time import sleep
from typing import TYPE_CHECKING, Literal, Optional

from item import Key
from leaderboard import insert_record
from location import l0
from save_game import store_game_state

if TYPE_CHECKING:
    from enemy import Enemy
    from item import Item
    from location import Location


class Player:
    def __init__(
        self,
        username: str,
        current_room: Location = l0,
        max_health: int = 100,
        health: int = 100,
        speed: int = 50,
        attack: int = 10,
        backpack_size: int = 3,
        backpack: Optional[list[Item]] = None,
    ):
        self.username: str = username
        self.current_room: Location = current_room
        self.max_health: int = max_health
        self.health: int = health
        self.speed: int = speed
        self.attack: int = attack
        self.backpack_size: int = backpack_size
        self.backpack: list[Item] = backpack if backpack is not None else []

    def menu(self) -> None:
        print(
            "\nYou can: ",
            "1: Look for items",
            "2: Use an item",
            "3: Move on",
            "4: Save game and exit",
            sep="\n",
        )
        chosen_action = int(input("Number of action: "))
        print("\n")
        if chosen_action == 1:
            self.look_for_items()
            self.menu()
        elif chosen_action == 2:
            self.use_item()
            self.menu()
        elif chosen_action == 3:
            self.change_room()
        elif chosen_action == 4:
            self.save_game()
        else:
            print("Not a valid option - please try again.\n")
            self.menu()
        # TODO Make sure menu() works

    def attack_enemy(self, target: Enemy) -> None:
        damage: int = self.attack + randint(0, self.attack // 2)
        target.health -= damage
        print(
            f"{target.variant} took {damage} damage and is "
            f"now on {target.health if target.health > 0 else 0} health."
        )

    def fight(self) -> None:
        for target in self.current_room.enemies.values():
            sleep(2)
            print(f"A {target.variant} jumps out!")
            while target.health > 0:
                action = int(input("\nATTACK (1) or USE AN ITEM (2): "))
                if action == 1:
                    self.attack_enemy(target)
                else:
                    if not self.use_item():
                        print("You attack instead.")
                        self.attack_enemy(target)
                if target.health > 0:
                    target.attack_enemy(self)
                    if self.health < 0:
                        self.death()
                else:
                    print("You killed it!")

    def use_item(self) -> Optional[Literal[False]]:
        if len(self.backpack) == 0:
            print("You don't have any items.")
            return False
        else:
            print("Contents of backpack: ")
            for index, item in enumerate(self.backpack):
                print(f"{str(index + 1)}: {item.name}")
            item = self.backpack[int(input("Item number: ")) - 1]
            used: bool = item.use_item(self)
            if used:
                self.backpack.remove(item)
            return None

    def pick_up_item(self, item: Item) -> None:
        sleep(1)
        if len(self.backpack) >= self.backpack_size:
            swap_item_choice: str = input(
                "Your backpack is full. Would you like to swap the "
                f"{item.name} with an item you currently have? (y/n): "
            )
            if swap_item_choice == "y":
                print("Items currently in bag: ")
                sleep(1)
                for index, backpack_item in enumerate(self.backpack):
                    print(f"{str(index + 1)}: {backpack_item.name}")
                swap_item: Item = self.backpack[
                    int(input("Enter the number of the item you would like to swap: "))
                    - 1
                ]
                self.backpack.remove(swap_item)
                self.current_room.items.append(swap_item)
                print(f"\n{item.name} added to bag.")
                self.current_room.items.remove(item)
        else:
            self.backpack.append(item)
            print(f"{item.name} added to bag.")
            self.current_room.items.remove(item)

    def look_for_items(self) -> None:
        print("You look around for items ... ", end="")
        sleep(1.5)
        if len(self.current_room.items) != 0:
            print("You find: ")
            for index, item in enumerate(self.current_room.items):
                print(f"{str(index + 1)}: {item.name}")
            selected_items: list[Item] = [
                self.current_room.items[i - 1]
                for i in [
                    int(i)
                    for i in input(
                        "Enter the number(s) of the items you would like "
                        "to pick up (separated by spaces) or nothing to "
                        "not pick anything up: "
                    ).split()
                ]
            ]
            for i in selected_items:
                self.pick_up_item(i)
        else:
            print("There aren't any.")

    def change_room(self) -> None:
        if self.current_room.connected_rooms is None:
            self.win_game()
        num_connected_rooms: int = len(self.current_room.connected_rooms)
        one_connected_room: bool = bool(num_connected_rooms == 1)
        print(
            "There"
            + (
                "'s a door"
                if one_connected_room
                else f" are {num_connected_rooms} doors"
            )
            + " in front of you. ",
            end="",
        )
        sleep(1)
        if not one_connected_room:
            while True:
                try:
                    selected_door: int = int(
                        input("Pick a door number to go through: ")
                    )
                    selected_room: Location = self.current_room.connected_rooms[
                        selected_door - 1
                    ]
                except ValueError:
                    print(
                        "Please enter a number (one of: "
                        f"{[i + 1 for i in range(num_connected_rooms)]})"
                    )
                    continue
                if selected_room.key_required:
                    print("The door is locked and needs a key.")
                    keys_in_backpack: list[bool] = [
                        bool(isinstance(item, Key)) for item in self.backpack
                    ]
                    key_in_backpack: bool = bool(keys_in_backpack.count(True))
                    if key_in_backpack:
                        key_index: int = keys_in_backpack.index(True)
                        print(
                            "You have a key in your backpack. You try it ... ", end=""
                        )
                        sleep(1)
                        print("It fits!")
                        self.backpack.pop(key_index)
                        break
                    else:
                        print("You don't have one! Try a different door.")
                        continue
                else:
                    break
        else:
            selected_room = self.current_room.connected_rooms[0]
        # noinspection PyUnboundLocalVariable
        self.current_room = selected_room
        print("You walk through the door, into the next room.")

    def death(self) -> None:
        print("GAME OVER")
        print(f"You died. You reached level {self.current_room.name}.")
        quit()

    def win_game(self) -> None:
        print("You won!")
        print(f"You finished on {self.health} health.")
        insert_record(
            username=self.username, final_health=self.health
        )  # type: ignore[call-arg]
        quit()

    def save_game(self) -> None:
        if input("Are you sure you want to save and quit? (y/n): ") == "y":
            store_game_state(self)
            print("Game stored.")
            quit()
        else:
            self.menu()
