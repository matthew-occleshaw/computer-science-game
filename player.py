from random import randint
from item import HealthItem, Apple, Key, UpgradeStation


# noinspection PyMethodMayBeStatic
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
            self.swap_item = input("Your backpack is full. Would you like to swap "
                                   "this item with an item you currently have?(y/n): ")
            if self.swap_item == "y":
                print("Items currently in bag:")
                for i in range(self.backpack_size):
                    print(str(i + 1) + ": " + self.backpack[i])
                self.swap_item = int(input("Enter the number of the item you would "
                                           "like to swap: "))
                self.backpack[self.swap_item - 1] = item
        else:
            self.backpack.append(item)
        # TODO Make sure swap item logic works

    def attack_enemy(self, target):
        damage = self.attack + randint(0, self.attack)
        target.health -= damage
        print(f"{target.type} took {damage} damage and is "
              f"now on {target.health if target.health > 0 else 0} health")

    def fight(self):
        self.current_room.create_enemies()
        for target in self.current_room.enemies.values():
            print(f"\nA {target.type} jumps out")
            while target.health > 0:
                action = int(input("\nATTACK (1) or USE AN ITEM (2): "))
                if action == 1:
                    self.attack_enemy(target)
                else:
                    if self.use_item() == False:
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
            print("You don't have any items")
            return False
        else:
            print("Contents of backpack:")
            for i in range(len(self.backpack)):
                print(f"{i + 1}: {self.backpack[i]}")
            item_index = int(input("Item number: ")) - 1
            item = self.backpack[item_index]
            if issubclass(item, HealthItem):
                self.health += item.health_increase
                self.backpack.pop(item_index)
                print("Item used! You were healed for "
                      f"{item.health_increase} health")
        # TODO Write use item code

    def use_upgrade_station(self):
        upgrade = int(input("Would you like to upgrade "
                            "MAX HEALTH (1), SPEED (2), ATTACK "
                            "(3) or BACKPACK SIZE (4): "))
        if upgrade == 1:
            health_increase = randint(20, 50)
            self.health += health_increase
            self.max_health += health_increase
            print(f"Your max health was increased by {health_increase} "
                  f"and is now {self.max_health}")
        elif upgrade == 2:
            speed_increase = randint(10, 25)
            self.speed += speed_increase
            print(f"Your speed was increased by {speed_increase} "
                  f"and is now {self.speed}")
        elif upgrade == 3:
            attack_increase = randint(5, 10)
            self.attack += attack_increase
            print(f"Your attack was increased by {attack_increase} "
                  f"and is now {self.attack}")
        elif upgrade == 4:
            self.backpack_size += 1
            print("Your backpack size was increased by 1 and is now "
                  f"{self.backpack_size}")
        else:
            print("That is not a valid thing to upgrade. Please try again.")
            self.use_upgrade_station()

    def enter_room(self):
        pass
        # TODO Write enter room code

    def change_room(self):
        pass
        # TODO Write change room code

    def death(self):
        print("You died")
        quit()
