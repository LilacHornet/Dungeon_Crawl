import sys

from utils import check_int
from pymongo import MongoClient
from models import Hero,Monster
from typing import List
import random

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

HEROES = get_heroes(DATABASE.Characters.find({}))
MONSTERS = get_monsters(DATABASE.Monsters.find({}))

MAIN_OPTIONS =["Jouer", "Scores", "Quitter"]

# Affichage du menu principal 
while True:
    #     Choix de commencer le jeu
    display_main_menu(MAIN_OPTIONS)
    user_choice = input()
    #     Verif d'input
    try:
        choice = check_int(user_choice, 1, len(MAIN_OPTIONS) )
    except Exception as e : print(e)
    else :
        match(choice):

            case 1 :
                wave = 0
                # Composition de l'equipe
                party = build_party(HEROES)
                living_party = party.copy()
                # Affichage equipe
                display_party(party)
            
                while len(living_party) > 0:
                    # Lancement de la vague
                    wave += 1
                    # Tirage aleatoire d'un monstre
                    monster = current_monster(MONSTERS)
                    #    Affichage monstre
                    display_encounter(monster)

                    while not monster.isdead() or len(living_party) != 0:
                        
                        # Les trois heros attaquent
                        attack_phase(living_party, monster)
                                

                        # Le monstre attaque
                            # Choix aleatoire hero cible parmi heros viavnt
                        current_target = random.choice(living_party)
                            # Modification hp heros
                            # Affichage attaque
                        current_target.attacked_by(monster)
                            # Interruption si tous heros morts
                        living_party = [p for p in party if not p.is_dead()]
                    
                        
                # Affichage victoire si monstre mort
                # Affichage defaite si heros morts
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
        #        Affiche les score

            case 3:
                sys.exit()
                break


