from __future__ import annotations

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from models import Entity, Hero, Monster

def display_main_menu(options: List[str]) -> None:
    print("Menu principal")
    for i in  range(len(options)):

        print(f"{i+1}. {options[i]}")

def display_party(party: List[Hero]) -> None:
    for hero in party :
        print(hero.to_string())

def display_encounter(monster: Monster, wave: int) -> None:
    print(f"C'est la vague {wave+1}, votre ennemi est un {monster.to_string()}")
    
def display_attack(victim : Hero | Monster | Entity, agressor: Hero | Monster, damage: int) -> None :
    print(f"{agressor.name} attaque {victim.name} et inflige {damage} dégats")

def display_heroes(heroes: List[Hero], selected: List[int]) -> None:
    for i in range(len(heroes)):
        if i in selected:
            print(f"\033[9m{i+1}. {heroes[i].to_string()}\033[0m")
        else:
            print(f"{i+1}. {heroes[i].to_string()}")

def display_victory(wave: int, monster: Monster)-> None:
    print(f"Vous avez validé la vague {wave} en battant {monster.name}")

def display_defeat(wave: int, monster: Monster):
    print(f"Votre groupe a été défait par {monster.name}, vous avez réussi à vaincre {wave} monstres")