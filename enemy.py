from random import randint

class enemyParentClass:
  def __init__(self, current_room):
    self.current_room = current_room

  def attackEnemy(self, target):
    self.damage = self.attack + randint(0, self.attack)
    target.health -= self.damage

class basicEnemyClass(enemyParentClass):
  def __init__(self, current_room):
    enemyParentClass.__init__(current_room)
    self.type = "Basic Enemy"
    self.health = 15
    self.speed = 35
    self.attack = 5

class normalEnemyClass(enemyParentClass):
  def __init__(self):
    self.type = "Normal Enemy"
    self.health = 25
    self.speed = 50
    self.attack = 10

class hardEnemyClass(enemyParentClass):
  def __init__(self):
    self.type = "Hard Enemy"
    self.health = 35
    self.speed = 65
    self.attack = 15

class bossEnemyClass(enemyParentClass):
  def __init__(self):
    self.type = "Boss Enemy"
    self.health = 75
    self.speed = 100
    self.attack = 25