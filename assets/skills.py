from assets.skills_decorators import check_if_used, required_stamina, skill_name

# import game_objects.battle
from exceptions import PlayerDies


@skill_name('Свирепый пинок')
@check_if_used
@required_stamina(6)
def ferocious_kick(battle) -> str:
    try:
        battle.target_unit.change_health(-12)
    except PlayerDies:
        pass
    return 'наносит 12 урона сопернику.'


@skill_name('Мощный укол')
@required_stamina(5)
@check_if_used
def mighty_jab(battle) -> str:
    try:
        battle.target_unit.change_health(-15)
    except PlayerDies:
        pass
    return 'наносит 15 урона сопернику.'


@skill_name('Жадный лекарь')
@check_if_used
@required_stamina(6)
def greedy_healer(battle) -> str:
    battle.active_unit.change_health(battle.active_unit.role.max_health)
    return 'полностью восстанавливает здоровье!'


# here be tests

if __name__ == '__main__':
    greedy_healer(12)
    print(greedy_healer.name)


