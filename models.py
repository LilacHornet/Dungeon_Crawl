from display import display_attack


class Entity:
    def __init__(self, item : dict):
        self.name = item["name"]
        self.attack = item["attack"]
        self.defence = item["defense"]
        self.max_hp = item["hp"]
        self.hp = item["hp"]

    def __eq__(self, other):
        return self.name == other.name

    def is_dead(self):
        return self.hp <= 0

    def attacked_by(self, agressor) -> None:
        # Calcul attaque contre defense
        damage = agressor.attack - self.defence
        # Modification hp 
        self.hp = max(self.hp - damage,0)
        display_attack(self, agressor, damage)

    def to_string(self) -> str:
        return f"{self.name} : {self.attack} ATK, {self.defence} DEF, {self.hp}/{self.max_hp} HP"

class Hero(Entity):
    pass

class Monster(Entity):
    pass

class Score():
    def __init__(self, item : dict):
            self.username = item["player_name"]
            self.waves = item["waves"]
    def to_string(self) -> str:
        return f"{self.username} : {self.waves}"