import sys

from display import display_defeat, display_encounter, display_main_menu, display_party, display_victory
from game import attack_phase, build_party
from utils import check_int, check_str
from pymongo import MongoClient
from models import Hero,Monster, Score
from typing import List
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

def get_highscores() -> List[Score]:
    highscores = []
    highscores_mongo = DATABASE.Scores.find().sort("waves", -1).limit(3)
    for score_mongo in highscores_mongo:
        highscores.append(Score(score_mongo))
    return highscores

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
                party = build_party(HEROES.copy())
                living_party = party.copy()
                # Affichage equipe
                display_party(party)
            
                while len(living_party) > 0:
                    # Lancement de la vague
                    
                    # Tirage aleatoire d'un monstre
                    monster = copy.deepcopy(random.choice(MONSTERS))
                    #    Affichage monstre
                    display_encounter(monster, wave)
                    time.sleep(0.5)

                    while not monster.is_dead() and len(living_party) > 0:
                        
                        # Les trois heros attaquent et inflige le poison
                        attack_phase(living_party, monster)

                        # Affichage victoire si monstre mort
                        if monster.is_dead() : 
                            wave += 1
                            display_victory(wave, monster)
                            time.sleep(0.5)
                            break

                        # Le monstre attaque
                            # Choix aleatoire hero cible parmi heros viavnt
                        current_target = random.choice(living_party)
                            # Modification hp heros
                            # Affichage attaque
                        current_target.attacked_by(monster)
                        time.sleep(0.5)

                        # Inflige les degats du poison
                        monster.poison_damage()
                            # Interruption si tous heros morts
                        living_party = [p for p in party if not p.is_dead()]


                # Affichage defaite si heros morts
                display_defeat(wave, monster)
                time.sleep(0.5)
                # Demander nom d'utilisateur
                while True:
                    print("Entrez votre nom")
                    username = input()
                    # Verifier validité
                    try:
                        check_str(username, 3, 20)
                    except Exception as e: print(e)
                    else:
                        #Enregistrer le score dans la BDD
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


