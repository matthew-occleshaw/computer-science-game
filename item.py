from random import randint


class HealthItem:
    def __init__(self, name, health_increase):
        self.name = name
        self.health_increase = health_increase

    def use_item(self, player):
        player.health += self.health_increase
        print(f"{self.name} used! You were healed for {self.health_increase} health.")


def apple():
    return HealthItem("Apple", 15)


class Key:
    def __init__(self, room_for):
        self.room = room_for

    # TODO Implement keys for rooms


class UpgradeStation:
    def __init__(self):
        self.name = "Upgrade Station"

    def use_item(self, player):
        print(
            "Would you like to upgrade: ",
            "1: Max Health",
            "2: Speed",
            "3: Attack",
            "4: Backpack Size",
            sep="\n",
        )
        upgrade = int(input("Attribute number: "))
        if upgrade == 1:
            health_increase = randint(20, 50)
            player.health += health_increase
            player.max_health += health_increase
            print(
                f"Your max health was increased by {health_increase} and is now "
                f"{player.max_health}. You were healed for {health_increase} health "
                f"and re now on {player.health} health."
            )
        elif upgrade == 2:
            speed_increase = randint(10, 25)
            player.speed += speed_increase
            print(
                f"Your speed was increased by {speed_increase} "
                f"and is now {player.speed}."
            )
        elif upgrade == 3:
            attack_increase = randint(5, 10)
            player.attack += attack_increase
            print(
                f"Your attack was increased by {attack_increase} "
                f"and is now {player.attack}."
            )
        elif upgrade == 4:
            player.backpack_size += 1
            print(
                "Your backpack size was increased by 1 and is now "
                f"{player.backpack_size}."
            )
        else:
            print("That is not a valid thing to upgrade. Please try again.")
            self.use_item()
