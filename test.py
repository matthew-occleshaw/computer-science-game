from item import Key, apple
from location import l2, l1
from player import PlayerClass


p = PlayerClass(l1)
p.backpack.extend([apple(), Key()])
p.change_room()
