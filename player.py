from random import randint
from time import sleep

from item import Key
from location import l0
from leaderboard import insert_record


class PlayerClass:
    def __init__(
        self,
        username,
        max_health=100,
        health=100,
        speed=50,
        attack=10,
        backpack_size=3,
        backpack=[],
        current_room=l0,
    ):
        self.username = username
        self.max_health = max_health
        self.health = health
        self.speed = speed
        self.attack = attack
        self.backpack_size = backpack_size
        self.backpack = backpack
        self.current_room = current_room

    def menu(self):
        print(
            "\nYou can: ", "1: Look for items", "2: Use an item", "3: Move on", sep="\n"
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
        else:
            print("Not a valid option - please try again.\n")
            self.menu()
        # FIXME Make sure menu() works

    def attack_enemy(self, target):
        damage = self.attack + randint(0, self.attack // 2)
        target.health -= damage
        print(
            f"{target.type} took {damage} damage and is "
            f"now on {target.health if target.health > 0 else 0} health."
        )

    def fight(self):
        for target in self.current_room.enemies.values():
            sleep(2)
            print(f"A {target.type} jumps out!")
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

    def use_item(self):
        if len(self.backpack) == 0:
            print("You don't have any items.")
            return False
        else:
            print("Contents of backpack: ")
            for index, item in enumerate(self.backpack):
                print(f"{str(index + 1)}: {item.name}")
            item = self.backpack[int(input("Item number: ")) - 1]
            item.use_item(self)
            self.backpack.remove(item)

    def pick_up_item(self, item):
        sleep(1)
        if len(self.backpack) >= self.backpack_size:
            swap_item = input(
                "Your backpack is full. Would you like to swap the "
                f"{item.name} with an item you currently have? (y/n): "
            )
            if swap_item == "y":
                print("Items currently in bag: ")
                sleep(1)
                for index, backpack_item in enumerate(self.backpack):
                    print(f"{str(index + 1)}: {backpack_item.name}")
                swap_item = self.backpack[
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

    def look_for_items(self):
        print("You look around for items ... ", end="")
        sleep(1.5)
        if len(self.current_room.items) != 0:
            print("You find: ")
            for index, item in enumerate(self.current_room.items):
                print(f"{str(index + 1)}: {item.name}")
            selected_items = [
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

    def change_room(self):
        if self.current_room.connected_rooms is None:
            self.win_game()
        num_connected_rooms = len(self.current_room.connected_rooms)
        one_connected_room = True if num_connected_rooms == 1 else False
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
                    selected_door = int(input("Pick a door number to go through: "))
                    selected_room = self.current_room.connected_rooms[selected_door - 1]
                    break
                except ValueError:
                    print(
                        "Please enter a number (one of: "
                        f"{[i + 1 for i in range(num_connected_rooms)]})"
                    )
        else:
            selected_room = self.current_room.connected_rooms[0]
        if selected_room.key_required:
            print("The door is locked and needs a key.")
            key_in_backpack = any(isinstance(i, Key) for i in self.backpack)
            if key_in_backpack:
                key = self.backpack[
                    list(
                        map(
                            lambda item: True if isinstance(item, Key) else False,
                            self.backpack,
                        )
                    ).index(True)
                ]
                print("You have a key in your backpack. You try it ... ", end="")
                sleep(1)
                print("It fits!")
                self.backpack.pop(key)
        self.current_room = selected_room
        print("You walk through the door, into the next room.")

    def death(self):
        print("GAME OVER")
        print(f"You died. You reached level {self.current_room.name}.")
        quit()

    def win_game(self):
        print("You won!")
        print(f"You finished on {self.health} health.")
        insert_record(self.username, self.health)
        quit()
