class Entity:
    def __init__(self, item : dict):
        self.name = item["name"]
        self.attack = item["attack"]
        self.defence = item["defense"]
        self.max_hp = item["hp"]
        self.hp = item["hp"]

    def is_dead(self):
        return self.hp <= 0

    def attacked_by(self, agressor) -> None:
        # Calcul attaque contre defense
        damage = agressor.attack - self.defence
        # Modification hp 
        self.hp = self.hp - damage
        display_attack(self, agressor, damage)


class Hero(Entity):
    pass

class Monster(Entity):
    pass