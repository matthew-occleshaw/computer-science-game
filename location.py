class locationClass: #defines class for rooms
  def __init__(self, room_name, basic_enemy, normal_enemy, hard_enemy, boss, connected_rooms, *items):
    self.room_name = room_name
    self.basic_enemy = basic_enemy
    self.normal_enemy = normal_enemy
    self.hard_enemy = hard_enemy
    self.boss = boss
    self.connected_rooms = connected_rooms
    self.items = list(items) #returns a list

  def return_connected_rooms(self):
    connected_rooms_names = []
    for i in self.connected_rooms:
      connected_rooms_names.append(i.room_name)
    return connected_rooms_names

l9 = locationClass("9", 0, 0, 0, 1, [])
l8 = locationClass("8", 1, 2, 1, 0, [l9])
l7 = locationClass("7", 1, 0, 1, 0, [l8])
l6 = locationClass("6", 1, 0, 1, 0, [l8])
l5 = locationClass("5", 1, 0, 1, 0, [l8])
l4 = locationClass("4", 1, 1, 0, 0, [l6, l7])
l3 = locationClass("3", 1, 1, 0, 0, [l5])
l2 = locationClass("2", 3, 0, 0, 0, [l3, l4], "apple", "upgrade_station")
l1 = locationClass("1", 1, 0, 0, 0, [l2], "key")