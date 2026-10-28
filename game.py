import copy
import random
import time

from display import display_choice_party, display_defeat, display_encounter, display_heroes, display_party, display_victory
from utils import check_int, valid_input
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
    display_choice_party(living_party)
    print(f"{len(living_party) + 1} Abandonner cette equipement")

    choice: int = valid_input(check_int,1, len(living_party) + 1) # type: ignore
    
    try:
        if choice <= len(living_party):
            to_replace = loot.is_better(living_party[choice - 1].equipment)
        else:
            return
    except Exception as e : print(e)
    else :
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

def combat_round(monster : Monster, living_party: List[Hero]) -> None:
    
        # Les trois heros attaquent et inflige le poison
        attack_phase(living_party, monster)

        if monster.is_dead() : 
            return

        # Le monstre attaque
        # Choix aleatoire hero cible parmi heros viavnt
        current_target = random.choice(living_party)
        # Modification hp heros
        # Affichage attaque
        current_target.attacked_by(monster)
        time.sleep(0.5)
        # Inflige les degats du poison
        monster.poison_damage()

def combat(heroes : List[Hero], monsters: List[Monster], loots: List[Loot]) -> int :
    wave = 0
    # Composition de l'equipe
    party = build_party(heroes.copy())
    living_party = party.copy()
    # Affichage equipe
    display_party(party)
    
    while len(living_party) > 0:
    # Lancement de la vague
        # Tirage aleatoire d'un monstre
        monster = copy.deepcopy(random.choice(monsters))
        #    Affichage monstre
        display_encounter(monster, wave)
        time.sleep(0.5)

        while not monster.is_dead() and len(living_party) > 0:

            combat_round(monster, living_party)
            # Interruption si tous heros morts
            living_party = get_living_party(party)

                        
            # Affichage victoire si monstre mort
        if len(living_party) > 0:
            wave += 1
            display_victory(wave, monster)
            time.sleep(0.5)
            looting(living_party, monster, loots)
            time.sleep(0.5)


        # Affichage defaite si heros morts
    display_defeat(wave, monster)
    time.sleep(0.5)
    return wave