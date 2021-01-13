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