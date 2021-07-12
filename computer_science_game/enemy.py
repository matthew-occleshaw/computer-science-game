from __future__ import annotations  # FIXME Can be removed once python 3.10 comes out

import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from computer_science_game.player import Player


class Enemy:
    def __init__(self, variant: str, health: int, speed: int, attack: int) -> None:
        self.variant: str = variant
        self.health: int = health
        self.speed: int = speed
        self.attack: int = attack

    def attack_enemy(self, target: Player) -> None:
        damage: int = self.attack + random.randint(0, self.attack // 2)
        if random.uniform(0, 100) < 100 - target.speed / 3:
            target.health -= damage
            print(
                f"You took {damage} damage and are now on "
                f"{target.health if target.health > 0 else 0} health"
            )
        else:
            print("You dodged the attack!")


def basic_enemy() -> Enemy:
    return Enemy("Basic Enemy", health=15, speed=35, attack=5)


def normal_enemy() -> Enemy:
    return Enemy("Normal Enemy", health=25, speed=50, attack=10)


def hard_enemy() -> Enemy:
    return Enemy("Hard Enemy", health=35, speed=65, attack=15)


def boss_enemy() -> Enemy:
    return Enemy("Boss Enemy", health=75, speed=100, attack=25)
