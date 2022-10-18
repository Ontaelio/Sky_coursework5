from game_objects.arena import Arena
from game_objects.battle import Battle
from game_objects.equipment import EquipmentList

from game_objects.units import PlayerHero, RobotHero
from assets.unit_classes import WARRIOR, THIEF

if __name__ == '__main__':
    Johon = PlayerHero('Johon', WARRIOR)
    Buhach = RobotHero('Buhach', THIEF)
    print(Johon)
    #a = Johon.skill(9)

    arena = Arena()
    battle = Battle(arena, Johon, Buhach)

    print(Buhach.health)
    print(Johon.use_skill(battle))
    print(Buhach.health)
    print(Johon.use_skill(battle))
    print(Johon.stamina)
    Johon.change_stamina(-10)
    print(Johon.stamina)
    Johon.change_stamina(25)
    print(Johon.stamina)

    equipment = EquipmentList()
    equipment.get_data("./data/equipment.json")
    Johon.weapon = equipment.weapons[0]
    Johon.armor = equipment.armors[2]
    Buhach.armor = equipment.armors[1]
    Buhach.weapon = equipment.weapons[1]
    print(Johon.weapon.name)

    print(Johon.damage)
    print(Johon.damage)
    print(Johon.damage)
    print(Johon.damage)

    print(battle.attack())
    battle.swap_units()
    print(battle.attack())
    print(battle.attack())
    print(battle.attack())
    print(battle.attack())
    print(battle.attack())

    print(battle.attack())
    print(battle.attack())
    print(battle.attack())
    print(battle.attack())
    print(battle.attack())
    print(battle.attack())

    print(battle.attack())
    print(battle.attack())
    print(battle.attack())
    print(battle.attack())
    print(battle.attack())
    print(battle.attack())

    print(battle.attack())
    print(battle.attack())
    print(battle.attack())
    print(battle.attack())
    print(battle.attack())
    print(battle.attack())

    print(battle.attack())
    print(battle.attack())
    print(battle.attack())
    print(battle.attack())
    print(battle.attack())
    print(battle.attack())

    print(battle.someone_died)
    try:
        Buhach.change_health(-100)
    except:
        pass

    print(battle.someone_died)








