from enemy import BasicEnemyClass, NormalEnemyClass, HardEnemyClass, BossEnemyClass
from location import LocationClass, l1, l2, l3, l4, l5, l6, l7, l8, l9
from player import PlayerClass

p1 = PlayerClass(l1)
print(p1.current_room.return_connected_rooms())