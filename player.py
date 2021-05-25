from random import randint
from time import sleep

from item import Key
from location import l0
from leaderboard import insert_record


class PlayerClass:
    def __init__(self, username, current_room=l0):
        self.username = username
        self.max_health = 100
        self.health = self.max_health
        self.speed = 50
        self.attack = 10
        self.backpack_size = 3
        self.backpack = []
        self.current_room = current_room

    def pick_up_item(self, item):
        if len(self.backpack) >= self.backpack_size:
            swap_item = input(
                "Your backpack is full. Would you like to swap the "
                f"{item.name} with an item you currently have? (y/n): "
            )
            if swap_item == "y":
                print("Items currently in bag: ")
                for index, backpack_item in enumerate(self.backpack):
                    print(f"{str(index + 1)}: {backpack_item.name}")
                swap_item = int(
                    input("Enter the number of the item you would like to swap: ")
                )
                self.backpack[swap_item - 1] = item
                print(f"{item.name} added to bag.")
                self.current_room.items.remove(item)
        else:
            self.backpack.append(item)
            print(f"{item.name} added to bag.")
            self.current_room.items.remove(item)

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
                    print("You killed it!\n")

    def use_item(self):
        if len(self.backpack) == 0:
            print("You don't have any items.")
            return False
        else:
            print("Contents of backpack: ")
            for index, item in enumerate(self.backpack):
                print(f"{str(index + 1)}: {item.name}")
            item_index = int(input("Item number: ")) - 1
            item = self.backpack[item_index]
            self.backpack.pop(item_index)
            item.use_item(self)

    def look_for_items(self):
        sleep(1)
        print("You look around for items ... ", end="")
        sleep(1)
        if self.current_room.items is not None:
            print("You find: ")
            for index, item in enumerate(self.backpack):
                print(f"{str(index + 1)}: {item.name}")
            selected_items = [
                self.current_room.items[i - 1]
                for i in [
                    int(i)
                    for i in input(
                        "Enter the number(s) of the items you would like "
                        "to pick up (separated by spaces): "
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
