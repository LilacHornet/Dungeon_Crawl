from utils import check_int
from models import Hero, Monster
from typing import List


def build_party(heroes: List[Hero]) -> List[Hero]:
#     Affichage de la liste de heros



    party = []
            #     Selection d'un hero repeté trois fois
    for i in range(3):
        while len(party) < i+1:
            display_heroes(HEROES, party)
                #         Verif d'input
            user_choice = input()
            try:
                choice = check_int(user_choice, 1,  (len(heroes) - len(party)) )
            except Exception as e : print(e)
            else :
                party.append(heroes[choice-1])
                heroes.pop(choice-1)


        return party

def attack_phase(party: List[Hero], monster: Monster):
    
    for hero in party:
        # Affichage de l'attaque
        monster.attacked_by(hero)
        # Interruption si monstre mort
        if monster.is_dead():
            break