import sys

from display import display_defeat, display_encounter, display_main_menu, display_party, display_victory
from game import attack_phase, build_party, combat, get_living_party, looting
from utils import check_int, check_str, valid_input
from pymongo import MongoClient
from models import Hero, Loot,Monster, Score
from typing import Callable, List
import random
import copy
import time

# Récuperation de la bdd
def get_DB():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["Dungeon_Crawl"]
    return db

DATABASE = get_DB()

# Enregistrement des heros dans une liste d'objets heroes
def get_heroes(collection) -> List[Hero]:
    heroes = []
    for hero_mongo in collection:
        heroes.append(Hero(hero_mongo))
    return heroes

# Enregistrement des monstres dans une liste d'objets montres
def get_monsters(collection) -> List[Monster]:
    monsters = []
    for monster_mongo in collection:
        monsters.append(Monster(monster_mongo))
    return monsters

def get_loots(collection) -> List[Loot]:
    loots = []
    for loot_mongo in collection:
        loots.append(Loot(loot_mongo))
    return loots


def get_highscores() -> List[Score]:
    highscores = []
    highscores_mongo = DATABASE.Scores.find().sort("waves", -1).limit(3)
    for score_mongo in highscores_mongo:
        highscores.append(Score(score_mongo))
    return highscores

HEROES = get_heroes(DATABASE.Characters.find({}))
MONSTERS = get_monsters(DATABASE.Monsters.find({}))
LOOTS = get_loots(DATABASE.Loots.find({}))

MAIN_OPTIONS =["Jouer", "Scores", "Quitter"]









# Affichage du menu principal 
while True:
    display_main_menu(MAIN_OPTIONS)
    choice = valid_input(check_int, 1, len(MAIN_OPTIONS))

    match(choice):

            case 1 :
                wave = combat(HEROES, MONSTERS, LOOTS)
                
                # Demander nom d'utilisateur
                print("Entrez votre nom")
                username = valid_input(check_str, 3, 20)
        
                score = {
                    "player_name" : username,
                    "waves" : wave
                }
                DATABASE.Scores.insert_one(score)
                break
                
            case 2:
                # Afficher les scores
        #        Recuperer scores base
        #            ouvrir base
        #            acceder a collection score
        #            find
        #            convertir curseur en list
        #        filtrer les 3 meilleurs
        #             trie le tableau sur element.waves
        #             prendre 3 derniers elements
        #                    array[-3:-1]
                highscores = get_highscores()
        #        Affiche les score
                for score in highscores:
                    print(score.to_string())

            case 3:
                sys.exit()
                break


