class HealthItem:
    def __init__(self, name, health_increase):
        self.name = name
        self.health_increase = health_increase


class Key:
    def __init__(self, room_for):
        self.room = room_for


class UpgradeStation:
    def __init__(self):
        self.used = False


def apple():
    return HealthItem("Apple", 15)
