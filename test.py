from enemy import BasicEnemyClass
from player import PlayerClass
from save_game import *

p = PlayerClass("username")
e = BasicEnemyClass()
e.attack_enemy(p)
store_game_state(p)
