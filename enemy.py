from random import randint


class EnemyParentClass:
    def attack_enemy(self, target):
        self.damage = self.attack + randint(0, self.attack)
        target.health -= self.damage


class BasicEnemyClass(EnemyParentClass):
    def __init__(self, current_room):
        self.type = "Basic Enemy"
        self.health = 15
        self.speed = 35
        self.attack = 5
        self.current_room = current_room


class NormalEnemyClass(EnemyParentClass):
    def __init__(self, current_room):
        self.type = "Normal Enemy"
        self.health = 25
        self.speed = 50
        self.attack = 10
        self.current_room = current_room


class HardEnemyClass(EnemyParentClass):
    def __init__(self, current_room):
        self.type = "Hard Enemy"
        self.health = 35
        self.speed = 65
        self.attack = 15
        self.current_room = current_room


class BossEnemyClass(EnemyParentClass):
    def __init__(self, current_room):
        self.type = "Boss Enemy"
        self.health = 75
        self.speed = 100
        self.attack = 25
        self.current_room = current_room


if __name__ == "__main__":
    e1 = BasicEnemyClass()
