import random
import time

from display import display_choice_party, display_heroes, display_party
from utils import check_int
from models import Hero, Loot, Monster
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

def looting(living_party: List[Hero], monster: Monster, loots: List[Loot]) -> None:
    loot = random_loot(monster, loots)
    print(f"Sur le cadavre du monstre, vous trouvez {loot.to_string()}\nA qui souhaitez vous le donner ?")
    valid_input= False
    while not valid_input:
        display_choice_party(living_party)
        print(f"{len(living_party) + 1} Abandonner cette equipement")
        user_choice = input()
        try:
            choice = check_int(user_choice, 1, len(living_party) + 1)
            if choice <= len(living_party):
                to_replace = loot.is_better(living_party[choice - 1].equipment)
            else:
                return
        except Exception as e : print(e)
        else :
            valid_input = True
            if to_replace == -1:
                living_party[choice - 1].equip(loot)
            else:
                living_party[choice - 1].replace(to_replace, loot)

            

def get_living_party(party: List[Hero]) -> List[Hero]:
    return [p for p in party if not p.is_dead()]

def random_loot(monster: Monster, loots: List[Loot]) -> Loot:
    rand_tier = random.randint(1,100)
    rand_stat = random.randint(1,4)
    if rand_tier <= monster.odds_tier1:
        tier = 1
    elif rand_tier <= monster.odds_tier1 + monster.odds_tier2:
        tier = 2
    else:
        tier = 3

    match rand_stat:
        case 1:
            stat = "atk"
        case 2:
            stat = "def"
        case 3:
            stat = "hp"
        case 4:
            stat = "poison"

    return next(loot for loot in loots if (loot.tier == tier and loot.stat == stat))

