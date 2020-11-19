from random import randint #imports random module
class playerClass: #defines player class
  def __init__(self):
    self.health = 100
    self.max_health = 100
    self.speed = 50
    self.attack = 10
    self.backpack_size = 3
    self.backpack = [] #backpack array contains carried items
    self.current_room = "l1"
  
  def pickUpItem(self, item): #defines the method to pick up an item - takes the item's name
    if len(self.backpack) >= self.backpack_size:
      self.swapItem = input("Your backpack is full. Would you like to swap")
    else:
      self.backpack.append(item)

  def attackEnemy(self, target): #defines the method to attack an enemy - takes the enemy's name
    self.damage = self.attack + randint(0, self.attack)
    target.health -= self.damage
    if target.health <= 0:
      print("You have vanquished the enemy")#***PLACEHOLDER***
  
  def encounterEnemy(self, target):
    print("You have encountered a", target.type)
  
  def useUpgradeStation(self):
    while True:
      self.upgrade = input("Would you like to upgrade max health, speed, attack or backpack size? ")
      if self.upgrade == "max health":
        self.health_increase = randint(20,50)
        self.max_health += self.health_increase
        print("Your max health was increased by", self.health_increase, "and is now", self.max_health)
        break
      elif self.upgrade == "speed":
        self.speed_increase = randint(10,25)
        self.speed += self.speed_increase
        print("Your speed was increased by", self.speed_increase, "and is now", self.speed)
        break
      elif self.upgrade == "attack":
        self.attack_increase = randint(5,10)
        self.attack += self.attack_increase
        print("Your attack was increased by", self.attack_increase, "and is now", self.attack)
        break
      elif self.upgrade == "backpack size":
        self.backpack_size += 1
        print("Your backpack size was increased by 1 and is now", self.backpack_size)
        break
      else:
        print("That is not a valid thing to upgrade. Please try again.")



class enemyParentClass:
  def attackEnemy(self, target):
    self.damage = self.attack + randint(0, self.attack)
    target.health -= self.damage

class basicEnemyClass(enemyParentClass):
  def __init__(self ):
    self.type = "Basic Enemy"
    self.health = 15
    self.speed = 35
    self.attack = 5

class normalEnemyClass(enemyParentClass):
  def __init__(self ):
    self.type = "Normal Enemy"
    self.health = 25
    self.speed = 50
    self.attack = 10

class hardEnemyClass(enemyParentClass):
  def __init__(self ):
    self.type = "Hard Enemy"
    self.health = 35
    self.speed = 65
    self.attack = 15



class locationClass: #defines class for rooms
  def __init__(self, basic_enemy, normal_enemy, hard_enemy, *items):
    self.basic_enemy = basic_enemy
    self.normal_enemy = normal_enemy
    self.hard_enemy = hard_enemy
    self.items = items #could be an array?



p1 = playerClass() #creates the player object
l1 = locationClass(1, 0, 0) #creates the first room (referenced in player class so deletion would cause errors)

p1.useUpgradeStation()