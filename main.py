# noinspection PyUnresolvedReferences
from enemy import (BasicEnemyClass, NormalEnemyClass,
    HardEnemyClass, BossEnemyClass)
from location import (LocationClass, l1, l2, l3, l4,
    l5, l6, l7, l8, l9)
from player import PlayerClass
from item import Apple, Key, UpgradeStation


p0 = PlayerClass(l1)


input("Press ENTER to start")
username = input("Enter username: ")
print("\nYou awake in a small, dingy room "
"The walls are made of stone brick, and there are no windows "
"However, there is one doorway on the other side of the room, "
"which you walk through",
sep="\n", end="")

p0.fight()
