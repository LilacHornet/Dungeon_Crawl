# Connexion à Mongo
from pymongo import MongoClient


def get_DB():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["Dungeon_Crawl"]
    return db

# Enregistrement des heros dans une liste d'objets heroes

# Enregistrement des monstres dans une liste d'objets montres

# Affichage du menu principal 
#     Choix de commencer le jeu
#     Verif d'input'

# Composition de l'equipe
#     Affichage de la liste de heros
#     Selection d'un hero repeté trois fois
#         Verif d'input
#         Enregistrements des heroes selectionés dans une liste

# Lancement du jeu
# Tirage aleatoire d'un monstre
# Les trois heros attaquent
    # Calcul attaque contre defense
    # Modification hp monstre
    # Interruption si monstre mort
# Le monstre attaque
    # Choix aleatoire hero cible
    # Calcul attaque contre defense
    # Modification hp heros
    # Interruption si tous heros morts
