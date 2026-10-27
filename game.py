from utils import check_int
from models import Hero
from typing import List


def build_party(heroes: List[Hero]) -> List[Hero]:
#     Affichage de la liste de heros
                
            #     Selection d'un hero repeté trois fois
                for i in range(3):
                    display_heroes(HEROES, party)
            #         Verif d'input
                    user_choice = input()
                    try:
                        choice = check_int(user_choice, 1,  (len(HEROES) - len(party)) )
                    except Exception as e : print(e)
                    else :
                        party.append(choice)
            #         Enregistrements des heroes selectionés dans une liste