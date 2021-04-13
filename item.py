class HealthItem:
    pass

class Apple(HealthItem):
    def __init__(self):
        self.health_increase = 15

class Key:
    def __init__(self, room_for):
        self.room = room_for


class UpgradeStation:
    def __init__(self):
        self.used = False
