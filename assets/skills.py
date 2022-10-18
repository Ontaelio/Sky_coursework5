from assets.skills_decorators import max_uses, required_stamina, skill_name

# import game_objects.battle


@skill_name('Свирепый пинок')
@required_stamina(6)
@max_uses(1)
def ferocious_kick(battle) -> str:
    # print('СВИРЕПЫЙ ПИНОК!!!111') # ferocious_kick.name = 'Свирепый пинок'
    battle.target_unit.change_health(-12)
    return '<Имя персонажа> использует <название умения> и наносит <урон> урона сопернику.'


@skill_name('Мощный укол')
@required_stamina(5)
@max_uses(1)
def mighty_jab(battle) -> str:
    ...


@skill_name('Жадный лекарь')
@required_stamina(6)
@max_uses(1)
def greedy_healer(battle) -> str:
    ...


# here be tests

if __name__ == '__main__':
    greedy_healer(12)
    print(greedy_healer.name)


