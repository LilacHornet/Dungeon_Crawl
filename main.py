from utils import check_int
from pymongo import MongoClient
from models import Hero,Monster
from typing import List

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



# Affichage du menu principal 
while True:
    #     Choix de commencer le jeu
    display_main_menu()
    user_choice = input()
    #     Verif d'input
    try:
        choice = check_int(user_choice, 1, 3 )
    except Exception as e : print(e)
    else :
        match(choice):

            case 1 :
            # Composition de l'equipe
                party = build_party(HEROES)
            

            # Lancement du jeu
            # Tirage aleatoire d'un monstre
            #    Affichage monstre
            # Les trois heros attaquent
                # Calcul attaque contre defense
                # Modification hp monstre
                    # Affichage de l'attaque
                # Interruption si monstre mort
                    # Affichage victoire
            # Le monstre attaque
                # Choix aleatoire hero cible
                # Calcul attaque contre defense
                # Modification hp heros
                    # Affichage attaque
                # Interruption si tous heros morts
                    # Affichage defaite
            case 2:
                # Afficher score

            case 3:
                # Fin du programme
                break


