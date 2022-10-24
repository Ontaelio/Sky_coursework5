import datetime
from random import randrange

from assets.skills_decorators import check_if_used, required_stamina, skill_name, required_equipment

# import game_objects.battle
from exceptions import PlayerDies


def deal_damage(battle, dmg):
    try:
        battle.target_unit.change_health(-dmg)
    except PlayerDies:
        pass


def suffer_damage(battle, dmg):
    try:
        battle.active_unit.change_health(-dmg)
    except PlayerDies:
        pass


@skill_name('Свирепый пинок')
@check_if_used
@required_stamina(6)
def ferocious_kick(battle) -> str:
    deal_damage(battle, 12)
    return 'наносит 12 урона сопернику.'


@skill_name('Мощный укол')
@required_stamina(5)
@check_if_used
def mighty_jab(battle) -> str:
    deal_damage(battle, 15)
    return 'наносит 15 урона сопернику.'


@skill_name('Жадный лекарь')
@check_if_used
@required_stamina(6)
def greedy_healer(battle) -> str:
    battle.active_unit.change_health(battle.active_unit.role.max_health)
    return 'полностью восстанавливает здоровье!'


@skill_name('Пенальти')
@required_equipment(weapon='футбольный мяч', armor='футболка')
@required_stamina(15)
def penalty_kick(battle) -> str:
    # if battle.active_unit.armor.name == "футболка" and battle.active_unit.weapon.name == "футбольный мяч":
    if not randrange(2):
        dmg = battle.target_unit.role.max_health/5
        deal_damage(battle, dmg)
        return f'забивает гол, нанося {dmg} урона сопернику.'
    return f'промахивается.'
    # return f'судья его останавливает из-за неправильной экипировки.'


@skill_name('Укус')
@required_stamina(15)
def vampire_bite(battle) -> str:
    now = datetime.datetime.now()
    if now.hour > 22 or now.hour < 4:
        deal_damage(battle, battle.target_unit.role.max_health)
        return f'выпивает всю кровь соперника!'

    suffer_damage(battle, battle.active_unit.role.max_health)
    return 'и поздновато понимает, что на улице светло. Солнце сжигает вампира!'


@skill_name('Заклинание')
@required_equipment(weapon='посох')
@required_stamina(30)
def magic_spell(battle) -> str:
    spell = randrange(10)
    mult = 1
    if battle.active_unit.armor.name == 'мантия':
        mult = 1.5
    if spell < 3:
        dmg = randrange(9, 15) * mult
        deal_damage(battle, dmg)
        return f'и запускает Огненную стрелу, нанося сопернику {dmg} урона.'
    if spell < 6:
        dmg = randrange(5, 20) * mult
        deal_damage(battle, dmg)
        return f'и запускает Ледяную пулю, нанося сопернику {dmg} урона.'
    if spell < 9:
        heal = randrange(8, 20) * mult
        battle.active_unit.change_health(heal)
        return f'и лечится на {heal} очков здоровья.'
    dmg = randrange(15, 30) * mult
    deal_damage(battle, dmg)
    suffer_damage(battle, dmg)
    return f'с перепугу шарашит файрболлом на {dmg} урона всем присутствующим.'







# here be tests

if __name__ == '__main__':
    greedy_healer(12)
    print(greedy_healer.name)


