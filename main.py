from enemy import basicEnemyClass, normalEnemyClass, hardEnemyClass, bossEnemyClass
from location import locationClass, l1, l2, l3, l4, l5, l6, l7, l8, l9
from player import playerClass

p1 = playerClass(l1)
print(p1.current_room.return_connected_rooms())