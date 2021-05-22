from enemy import BasicEnemyClass, NormalEnemyClass, HardEnemyClass, BossEnemyClass
from item import Key, UpgradeStation, apple


class LocationClass:  # defines class for rooms
    def __init__(
        self,
        room_name,
        connected_rooms,
        items=None,
        basic_enemy=0,
        normal_enemy=0,
        hard_enemy=0,
        boss=0,
        key_required=False,
    ):
        self.room_name = room_name
        self.key_required = key_required

        self.items = {}
        if items is not None:
            for i in range(len(items)):
                self.items[f"i{i}"] = items[i]

        self.connected_rooms = connected_rooms
        self.connected_room_names = []
        for i in self.connected_rooms:
            self.connected_room_names.append(i.room_name)

        self.enemies = {}
        for i in range(basic_enemy):
            self.enemies[f"be{i}"] = BasicEnemyClass()
        for i in range(normal_enemy):
            self.enemies[f"ne{i}"] = NormalEnemyClass()
        for i in range(hard_enemy):
            self.enemies[f"he{i}"] = HardEnemyClass()
        for i in range(boss):
            self.enemies[f"boss{i}"] = BossEnemyClass()


l9 = LocationClass("9", [], boss=1)
l8 = LocationClass("8", [l9], normal_enemy=2, hard_enemy=1)
l7 = LocationClass("7", [l8], basic_enemy=1, hard_enemy=1)
l6 = LocationClass("6", [l8], basic_enemy=1, hard_enemy=1)
l5 = LocationClass("5", [l8], basic_enemy=1, hard_enemy=1)
l4 = LocationClass("4", [l6, l7], basic_enemy=1, normal_enemy=1)
l3 = LocationClass("3", [l5], basic_enemy=1, normal_enemy=1)
l2 = LocationClass("2", [l3, l4], items=[apple(), UpgradeStation()], basic_enemy=3)
l1 = LocationClass("1", [l2], items=[Key(l2)], basic_enemy=1)
