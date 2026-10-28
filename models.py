import math
import time

from display import display_attack, display_poison_damage, display_poisoning


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
        damage = max(agressor.attack - self.defence,0)
        # Modification hp 
        self.hp = self.hp - damage
        display_attack(self, agressor, damage)

    def to_string(self) -> str:
        return f"{self.name} : {self.attack} ATK, {self.defence} DEF, {self.hp}/{self.max_hp} HP"

class Hero(Entity):
    def __init__(self, item: dict):
        super().__init__(item)
        self.poison = item["poison"]

    def to_string(self) -> str:
        return f"{self.name} : {self.attack} ATK, {self.poison} Poison, {self.defence} DEF, {self.hp}/{self.max_hp} HP"


    def poisons(self, monster: Monster) -> None:
        if(self.poison > 0): 
            monster.poisoning = monster.poisoning + self.poison
            display_poisoning(self.poison, monster.poisoning, self.name,monster.name)
            time.sleep(0.5)



class Monster(Entity):
    def __init__(self, item: dict):
        super().__init__(item)
        self.poisoning = 0

    def poison_damage(self) -> None:
        if(self.poisoning > 0):
            damage = self.poisoning
            self.hp = self.hp - self.poisoning
            self.poisoning = math.ceil(self.poisoning / 2)
            display_poison_damage(self.name, damage, self.poisoning)
            time.sleep(0.5)


class Score():
    def __init__(self, item : dict):
            self.username = item["player_name"]
            self.waves = item["waves"]
    def to_string(self) -> str:
        return f"{self.username} : {self.waves}"