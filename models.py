import math
import time
from typing import List

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
        self.equipment = []

    def to_string(self) -> str:
        loot_string = ""
        for item in self.equipment:
            loot_string += "\n\t"
            loot_string += item.to_string()
        return f"{self.name} : {self.attack} ATK, {self.poison} Poison, {self.defence} DEF, {self.hp}/{self.max_hp} HP" + loot_string
    
    def equip( self, loot: Loot) -> None :
        self.equipment.append(loot)
        match loot.stat:
            case "atk":
                self.attack += loot.amount
            case "def":
                self.defence += loot.amount
            case "hp":
                self.hp += loot.amount
                self.max_hp += loot.amount
            case "poison":
                self.poison += loot.amount

    def replace(self, to_replace : int, loot: Loot ) -> None:
        current_upgrade = self.equipment[to_replace].amount
        self.equipment.pop(to_replace)
        self.equipment.append(loot)
        match loot.stat:
            case "atk":
                self.attack += loot.amount - current_upgrade
            case "def":
                self.defence += loot.amount- current_upgrade
            case "hp":
                self.hp += loot.amount- current_upgrade
                self.max_hp += loot.amount- current_upgrade
            case "poison":
                self.poison += loot.amount- current_upgrade

    def poisons(self, monster: Monster) -> None:
        if(self.poison > 0): 
            monster.poisoning = monster.poisoning + self.poison
            display_poisoning(self.poison, monster.poisoning, self.name,monster.name)
            time.sleep(0.5)



class Monster(Entity):
    def __init__(self, item: dict):
        super().__init__(item)
        self.poisoning = 0
        self.odds_tier1 = item["odds_tier1"]
        self.odds_tier2 = item["odds_tier2"]
        self.odds_tier3 = item["odds_tier3"]

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

class Loot():
    def __init__(self, item: dict):
        self.name = item["name"]
        self.stat = item["stat"]
        self.amount = item["amount"]
        self.tier = item["tier"]

    def is_better(self, equiped: List[Loot]) -> int:
        if len(equiped) == 0:
            return -1
        for i in range(len(equiped)):
            if self.stat == equiped[i].stat and self.tier <= equiped[i].tier:
                raise Exception("Ce heros possede deja une piece d'équipement supérieur ou equivalente")
            elif self.stat == equiped[i].stat:
                return i
        return -1
        

    def to_string(self) -> str:
        return f"{self.name} augmentant {self.stat} de {self.amount}"