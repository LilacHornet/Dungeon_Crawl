from pymongo import MongoClient

import os


client = MongoClient("mongodb://localhost:27017")
db = client["Dungeon_Crawl"]

characters = db["Characters"]
monsters = db["monsters"]

CHARACTERS = [
  {"name": "Paladin", "attack": 20, "defense": 12, "hp": 120, "poison":0},
  {"name": "Chevalier", "attack": 22, "defense": 10, "hp": 110, "poison":0},
  {"name": "Berserker", "attack": 29, "defense": 6, "hp": 90, "poison":0},
  {"name": "Archer", "attack": 26, "defense": 7, "hp": 85, "poison":0},
  {"name": "Sorcier", "attack": 32, "defense": 4, "hp": 75, "poison":0},
  {"name": "Guerrier", "attack": 24, "defense": 8, "hp": 100, "poison":0},
  {"name": "Moine", "attack": 22, "defense": 9, "hp": 95, "poison":0},
  {"name": "Voleur", "attack": 28, "defense": 5, "hp": 80, "poison":0},
  {"name": "Chasseur", "attack": 23, "defense": 8, "hp": 90, "poison":0},
  {"name": "Druide", "attack": 21, "defense": 9, "hp": 100, "poison":0},
  {"name": "Alchimiste", "attack": 0, "defense": 7, "hp": 80, "poison":10}
]
characters.delete_many({})
characters.insert_many(CHARACTERS)


MONSTERS = [
  {"name": "Gobelin", "attack": 10, "defense": 6, "hp": 150},
  {"name": "Orc", "attack": 10, "defense": 8, "hp": 180},
  {"name": "Dragon", "attack": 10, "defense": 12, "hp": 200},
  {"name": "Zombie", "attack": 10, "defense": 7, "hp": 160},
  {"name": "Troll", "attack": 10, "defense": 10, "hp": 190},
  {"name": "Spectre", "attack": 24, "defense": 6, "hp": 170},
  {"name": "Golem", "attack": 21, "defense": 14, "hp": 210},
  {"name": "Vampire", "attack": 26, "defense": 9, "hp": 175},
  {"name": "Loup-garou", "attack": 24, "defense": 8, "hp": 185},
  {"name": "Squelette", "attack": 19, "defense": 7, "hp": 155}
]
monsters.delete_many({})
monsters.insert_many(MONSTERS)