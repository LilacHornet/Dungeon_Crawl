import time

from display import display_heroes
from utils import check_int
from models import Hero, Monster
from typing import List


def build_party(heroes: List[Hero]) -> List[Hero]:


    selected :List[int] = []
    party=[]
            #     Selection d'un hero repeté trois fois
    for i in range(3):
        while len(selected) < i+1:
            #     Affichage de la liste de heros
            display_heroes(heroes, selected)
                #         Verif d'input
            user_choice = input()
            try:
                choice = check_int(user_choice, 1,  len(heroes) , selected )
            except Exception as e : print(e)
            else :
                selected.append(choice)
                party.append(heroes[choice-1])


    return party

def attack_phase(party: List[Hero], monster: Monster):
    
    for hero in party:
        # Affichage de l'attaque
        monster.attacked_by(hero)
        time.sleep(0.5)

        # Empoisonne
        hero.poisons(monster)
        # Interruption si monstre mort
        if monster.is_dead():
            break