from exceptions import SomethingWentWrong
from game_objects.arena import Arena
from game_objects.battle import Battle
from game_objects.equipment import EquipmentList
from game_objects.ai import AI
from game_objects.game import GamePlayerVsAI
from game_objects.stats import get_verbose_stats

from game_objects.units import BaseHero
from assets.unit_classes import WARRIOR, THIEF, HEALER


def main():
    Johon = BaseHero('Johon', THIEF)
    Buhach = BaseHero('Buhach', WARRIOR)
    print(Johon)

    equipment = EquipmentList()
    equipment.get_data("./data/equipment.json")

    # Johon.equip(weapon=equipment.weapon('топорик'), armor=equipment.armor('панцирь'))
    # Buhach.equip(weapon=equipment.weapon('ножик'))

    print(Johon.weapon.name)

    arena = Arena()
    epic = GamePlayerVsAI(arena, Johon, Buhach)
    epic.game_start(
        equipment=equipment,
        player_weapon='топорик',
        player_armor='панцирь',
        enemy_weapon='ножик',
        enemy_armor='кожаная броня'
    )

    print(epic.get_full_description())

    # epic = GamePlayerVsAI(battle)
    print(epic.make_turn('skill'))
    print(Buhach.health)
    # print(Johon.role.skill.max_uses)
    print(epic.make_turn('skill'))
    print(Buhach.health)
    while not epic.battle.someone_died:
        print(epic.make_turn('attack'))
        # print(Johon.stamina, Buhach.stamina)
    print(Johon.health, Buhach.health)

    print(get_verbose_stats(Johon))
    print(epic.get_full_description())

def check_verbose():
    ...


if __name__ == '__main__':
    main()








