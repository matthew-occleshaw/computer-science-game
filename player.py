from random import randint

class playerClass: #defines player class
  def __init__(self, current_room):
    self.health = 100
    self.max_health = 100
    self.speed = 50
    self.attack = 10
    self.backpack_size = 3
    self.backpack = [] #backpack list contains carried items
    self.current_room = current_room
  
  def pickUpItem(self, item): #defines the method to pick up an item - takes the item's name
    if len(self.backpack) >= self.backpack_size:
      self.swap_item = input("Your backpack is full. Would you like to swap this item with an item you currently have?(y/n): ")
      if self.swap_item == "y":
        print("Items currently in bag:")
        for i in range(self.backpack_size):
          print(str(i+1) + ": " + self.backpack[i])
        self.swap_item = int(input("Enter the number of the item you would like to swap: "))
        self.backpack[self.swap_item - 1] = item
    else:
      self.backpack.append(item)

  def attackEnemy(self, target): #defines the method to attack an enemy - takes the enemy's name
    self.damage = self.attack + randint(0, self.attack)
    target.health -= self.damage
    if target.health <= 0:
      print("You have vanquished the enemy")#***PLACEHOLDER***

  def encounterEnemy(self, target):
    print("You have encountered a", target.type)
    #***PLACEHOLDER***
  
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

  def enterRoom(self):
    pass #***PLACEHOLDER***
  
  def changeRoom(self):
    pass #***PLACEHOLDER***