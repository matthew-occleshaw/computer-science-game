from random import randint


class PlayerClass:
    def __init__(self, current_room):
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
                "Your backpack is full. Would you like to swap "
                "this item with an item you currently have?"
                "(y/n): "
            )
            if swap_item == "y":
                print("Items currently in bag: ")
                for i in range(self.backpack_size):
                    print(f"{str(i + 1)}: {self.backpack[i]}")
                swap_item = int(
                    input("Enter the number of the item you would " "like to swap: ")
                )
                self.backpack[swap_item - 1] = item
        else:
            self.backpack.append(item)

    def attack_enemy(self, target):
        damage = self.attack + randint(0, self.attack)
        target.health -= damage
        print(
            f"{target.type} took {damage} damage and is "
            f"now on {target.health if target.health > 0 else 0} health."
        )

    def fight(self):
        for target in self.current_room.enemies.values():
            print(f"\nA {target.type} jumps out")
            while target.health > 0:
                action = int(input("\nATTACK (1) or USE AN ITEM (2): "))
                if action == 1:
                    self.attack_enemy(target)
                else:
                    if not self.use_item():
                        print("You attack instead")
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
            for i in range(len(self.backpack)):
                print(f"{i + 1}: {self.backpack[i].name}")
            item_index = int(input("Item number: ")) - 1
            item = self.backpack[item_index]
            self.backpack.pop(item_index)
            item.use_item(self)

    def change_room(self):
        num_connected_rooms = len(self.current_room.connected_rooms)
        one_connected_room = True if num_connected_rooms == 1 else False
        print(
            "There "
            + (
                "is 1 door"
                if one_connected_room
                else f"are {num_connected_rooms} doors"
            )
            + " in front of you"
        )
        if not one_connected_room:
            while True:
                try:
                    selected_door = int(input("Pick a door number to go through: "))
                    selected_room = self.current_room.connected_rooms[selected_door - 1]
                    break
                except ValueError:
                    print("Please enter a number")
        else:
            selected_room = self.current_room.connected_rooms[0]
        self.current_room = selected_room
        print("You walk through the door, into the next room")
        self.fight()

    # noinspection PyMethodMayBeStatic
    def death(self):
        print("You died")
        quit()
