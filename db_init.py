from pymongo import MongoClient

import os


client = MongoClient("mongodb://localhost:27017")
db = client["Dungeon_Crawl"]

characters = db["Characters"]
monsters = db["Monsters"]
loots = db["Loots"]

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
  {"name": "Gobelin", "attack": 10, "defense": 6, "hp": 150, "odds_tier1": 70, "odds_tier2": 25, "odds_tier3": 5},
  {"name": "Orc", "attack": 10, "defense": 8, "hp": 180, "odds_tier1": 60, "odds_tier2": 30, "odds_tier3": 10},
  {"name": "Zombie", "attack": 10, "defense": 7, "hp": 160, "odds_tier1": 55, "odds_tier2": 35, "odds_tier3": 10},
  {"name": "Squelette", "attack": 19, "defense": 7, "hp": 155, "odds_tier1": 50, "odds_tier2": 35, "odds_tier3": 15},
  {"name": "Troll", "attack": 10, "defense": 10, "hp": 190, "odds_tier1": 40, "odds_tier2": 45, "odds_tier3": 15},
  {"name": "Spectre", "attack": 24, "defense": 6, "hp": 170, "odds_tier1": 30, "odds_tier2": 50, "odds_tier3": 20},
  {"name": "Loup-garou", "attack": 24, "defense": 8, "hp": 185, "odds_tier1": 20, "odds_tier2": 55, "odds_tier3": 25},
  {"name": "Vampire", "attack": 26, "defense": 9, "hp": 175, "odds_tier1": 15, "odds_tier2": 45, "odds_tier3": 40},
  {"name": "Golem", "attack": 21, "defense": 14, "hp": 210, "odds_tier1": 10, "odds_tier2": 40, "odds_tier3": 50},
  {"name": "Dragon", "attack": 10, "defense": 12, "hp": 200, "odds_tier1": 5, "odds_tier2": 25, "odds_tier3": 70}
]

monsters.delete_many({})
monsters.insert_many(MONSTERS)


LOOTS = [
  {"name": "Épée de fer émoussée", "stat": "atk", "amount": 5, "tier": 1},
  {"name": "Épée d'acier poli", "stat": "atk", "amount": 15, "tier": 2},
  {"name": "Lame mythique en adamantium", "stat": "atk", "amount": 35, "tier": 3},
  {"name": "Armure de cuir usée", "stat": "def", "amount": 3, "tier": 1},
  {"name": "Armure de plaques en bronze", "stat": "def", "amount": 12, "tier": 2},
  {"name": "Harnois de chevalier en mithril", "stat": "def", "amount": 28, "tier": 3},
  {"name": "Anneau de vie mineur", "stat": "hp", "amount": 20, "tier": 1},
  {"name": "Amulette de vigueur robuste", "stat": "hp", "amount": 60, "tier": 2},
  {"name": "relique sacrée de vitalité", "stat": "hp", "amount": 150, "tier": 3},
  {"name": "Dague enduite de venin de serpent", "stat": "poison", "amount": 2, "tier": 1},
  {"name": "Fiole de toxine concentrée", "stat": "poison", "amount": 8, "tier": 2},
  {"name": "Orbe de peste noire", "stat": "poison", "amount": 22, "tier": 3}
]

loots.delete_many({})
loots.insert_many(LOOTS)