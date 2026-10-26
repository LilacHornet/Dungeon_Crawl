class Entity:
    def __init__(self, name, attack, defence, max_hp, hp):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.max_hp = max_hp
        self.hp = hp


class Hero(Entity):
    pass

class Monster(Entity):
    pass