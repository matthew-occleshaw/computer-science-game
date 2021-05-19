from random import randint


# noinspection PyUnresolvedReferences
class EnemyParentClass:
    def attack_enemy(self, target):
        damage = self.attack + randint(0, self.attack)
        target.health -= damage
        print(
            f"You took {damage} damage and are now on "
            f"{target.health if target.health > 0 else 0} health"
        )


class BasicEnemyClass(EnemyParentClass):
    def __init__(self):
        self.type = "Basic Enemy"
        self.health = 15
        self.speed = 35
        self.attack = 5


class NormalEnemyClass(EnemyParentClass):
    def __init__(self):
        self.type = "Normal Enemy"
        self.health = 25
        self.speed = 50
        self.attack = 10


class HardEnemyClass(EnemyParentClass):
    def __init__(self):
        self.type = "Hard Enemy"
        self.health = 35
        self.speed = 65
        self.attack = 15


class BossEnemyClass(EnemyParentClass):
    def __init__(self):
        self.type = "Boss Enemy"
        self.health = 75
        self.speed = 100
        self.attack = 25
