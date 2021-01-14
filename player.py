from random import randint


# noinspection PyMethodMayBeStatic
class PlayerClass:
    def __init__(self, current_room):
        self.health = 100
        self.max_health = 100
        self.speed = 50
        self.attack = 10
        self.backpack_size = 3
        self.backpack = []
        self.current_room = current_room

    def pick_up_item(self, item):
        if len(self.backpack) >= self.backpack_size:
            self.swap_item = input(
                "Your backpack is full. Would you like to swap this item with an item you currently have?(y/n): ")
            if self.swap_item == "y":
                print("Items currently in bag:")
                for i in range(self.backpack_size):
                    print(str(i + 1) + ": " + self.backpack[i])
                self.swap_item = int(input("Enter the number of the item you would like to swap: "))
                self.backpack[self.swap_item - 1] = item
        else:
            self.backpack.append(item)

    def attack_enemy(self, target):
        self.damage = self.attack + randint(0, self.attack)
        target.health -= self.damage
        if target.health <= 0:
            print("You have vanquished the enemy")  # TODO

    def encounter_enemy(self, target):
        print("You have encountered a", target.type)
        # TODO

    def use_upgrade_station(self):
        self.upgrade = input("Would you like to upgrade max health, speed, attack or backpack size: ")
        if self.upgrade == "max health":
            self.health_increase = randint(20, 50)
            self.max_health += self.health_increase
            print("Your max health was increased by", self.health_increase, "and is now", self.max_health)
        elif self.upgrade == "speed":
            self.speed_increase = randint(10, 25)
            self.speed += self.speed_increase
            print("Your speed was increased by", self.speed_increase, "and is now", self.speed)
        elif self.upgrade == "attack":
            self.attack_increase = randint(5, 10)
            self.attack += self.attack_increase
            print("Your attack was increased by", self.attack_increase, "and is now", self.attack)
        elif self.upgrade == "backpack size":
            self.backpack_size += 1
            print("Your backpack size was increased by 1 and is now", self.backpack_size)
        else:
            print("That is not a valid thing to upgrade. Please try again.")
            self.use_upgrade_station()

    def enter_room(self):
        pass  # TODO

    def change_room(self):
        pass  # TODO
