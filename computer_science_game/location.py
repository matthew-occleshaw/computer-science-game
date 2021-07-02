from __future__ import annotations  # FIXME Can be removed once python 3.10 comes out

from typing import Optional

from computer_science_game.enemy import (
    Enemy,
    basic_enemy,
    boss_enemy,
    hard_enemy,
    normal_enemy,
)
from computer_science_game.item import Item, Key, UpgradeStation, apple


class Location:
    def __init__(
        self,
        name: str,
        connected_rooms: Optional[list[Location]] = None,
        items: Optional[list[Item]] = None,
        basic_enemy_no: int = 0,
        normal_enemy_no: int = 0,
        hard_enemy_no: int = 0,
        boss_enemy_no: int = 0,
        key_required: bool = False,
    ) -> None:
        self.name: str = name
        self.key_required: bool = key_required

        self.items: list[Item] = items if items is not None else []

        self.connected_rooms: list[Location] = (
            connected_rooms if connected_rooms is not None else []
        )

        self.connected_room_names: list[str] = list(
            map(lambda room: room.name, self.connected_rooms)
        )

        self.enemies: dict[str, Enemy] = {}
        for i in range(basic_enemy_no):
            self.enemies[f"be{i}"] = basic_enemy()
        for i in range(normal_enemy_no):
            self.enemies[f"ne{i}"] = normal_enemy()
        for i in range(hard_enemy_no):
            self.enemies[f"he{i}"] = hard_enemy()
        for i in range(boss_enemy_no):
            self.enemies[f"boss{i}"] = boss_enemy()


l9: Location = Location("9", boss_enemy_no=1)
l8: Location = Location("8", [l9], normal_enemy_no=2, hard_enemy_no=1)
l7: Location = Location("7", [l8], basic_enemy_no=1, hard_enemy_no=1)
l6: Location = Location("6", [l8], basic_enemy_no=1, hard_enemy_no=1)
l5: Location = Location("5", [l8], basic_enemy_no=1, hard_enemy_no=1)
l4: Location = Location(
    "4", [l6, l7], key_required=True, basic_enemy_no=1, normal_enemy_no=1
)
l3: Location = Location("3", [l5], basic_enemy_no=1, normal_enemy_no=1)
l2: Location = Location(
    "2", [l3, l4], items=[apple(), UpgradeStation()], basic_enemy_no=3
)
l1: Location = Location("1", [l2], items=[Key()], basic_enemy_no=1)
l0: Location = Location("Start", [l1])

locations: list[Location] = [l0, l1, l2, l3, l4, l5, l6, l7, l8, l9]
locations_dict: dict[str, Location] = {
    location.name: location for location in locations
}
