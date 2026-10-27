class Entity:
    def __init__(self, item : dict):
        self.name = item["name"]
        self.attack = item["attack"]
        self.defence = item["defense"]
        self.max_hp = item["hp"]
        self.hp = item["hp"]


class Hero(Entity):
    pass

class Monster(Entity):
    pass