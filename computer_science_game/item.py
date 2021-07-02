from __future__ import annotations  # FIXME Can be removed once python 3.10 comes out

from random import randint
from typing import TYPE_CHECKING, Any, Callable, Type, Union

if TYPE_CHECKING:
    from computer_science_game.player import Player

# NOTE: All directly used items must have no parameters for creation, a name attribute
#   and a use_item method. They must also be added to the items list.


class Item:
    def __init__(self) -> None:
        self.name: str = ""

    def use_item(self, player: Player) -> bool:
        pass

    # TODO Do something here?


class HealthItem(Item):
    def __init__(self, name: str, health_increase: int) -> None:
        super().__init__()
        self.name: str = name
        self.health_increase: int = health_increase

    def use_item(self, player: Player) -> bool:
        player.health += self.health_increase
        print(f"{self.name} used! You were healed for {self.health_increase} health.")
        return True


def apple() -> HealthItem:
    return HealthItem("Apple", health_increase=15)


class Key(Item):
    def __init__(self) -> None:
        super().__init__()
        self.name: str = "Key"

    @staticmethod
    def use_item(player: Player, **kwargs: Any) -> bool:
        print("You can't use this item here.")
        return False


class UpgradeStation(Item):
    def __init__(self) -> None:
        super().__init__()
        self.name: str = "Upgrade Station"

    def use_item(self, player: Player) -> bool:
        print(
            "\nWould you like to upgrade: ",
            "1: Max Health",
            "2: Speed",
            "3: Attack",
            "4: Backpack Size",
            sep="\n",
        )
        upgrade: int = int(input("Attribute number: "))
        if upgrade == 1:
            health_increase: int = randint(20, 50)
            player.health += health_increase
            player.max_health += health_increase
            print(
                f"Your max health was increased by {health_increase} and is now "
                f"{player.max_health}. You were healed for {health_increase} health "
                f"and re now on {player.health} health."
            )
        elif upgrade == 2:
            speed_increase: int = randint(10, 25)
            player.speed += speed_increase
            print(
                f"Your speed was increased by {speed_increase} "
                f"and is now {player.speed}."
            )
        elif upgrade == 3:
            attack_increase: int = randint(5, 10)
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
            self.use_item(player)
        return True


items: list[Union[Type[Item], Callable[[], Item]]] = [
    Key,
    UpgradeStation,
    apple,
]
items_dict = {item().name: item for item in items}
