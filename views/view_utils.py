import json
from dataclasses import dataclass

import requests


# Need to create these classes here for compatibility with provided HTML template

@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float


@dataclass
class Armor:
    name: str
    defence: float


@dataclass
class Weapon:
    name: str
    max_damage: float
    min_damage: float


@dataclass
class Unit:
    name: str
    unit_class: UnitClass
    stamina_points: float
    health_points: float
    weapon: Weapon
    armor: Armor


@dataclass
class Heroes:
    player: Unit
    enemy: Unit


def get_game_data() -> dict:
    equipment = json.loads(requests.get('http://127.0.0.1:10001/equipment').content)
    roles = json.loads(requests.get('http://127.0.0.1:10001/roles').content)

    result = {
        "header": 'Выбор героя',  # для названия страниц
        "classes": roles['roles'],  # для названия классов
        "weapons": equipment['weapons'],  # для названия оружия
        "armors": equipment['armors']  # для названия брони
    }

    return result


def get_game_status(game_id):
    data = json.loads(requests.get(f'http://127.0.0.1:10001/gamestats/{game_id}').content)
    player_weapon = Weapon(
        name=data['player']['weapon'],
        max_damage=data['player']['weapon_max'],
        min_damage=data['player']['weapon_min'])
    player_armor = Armor(
        name=data['player']['armor'],
        defence=data['player']['defence'])
    player_class = UnitClass(
        name=data['player']['class'],
        max_health=data['player']['max_health'],
        max_stamina=data['player']['max_stamina'])
    player = Unit(
        name=data['player']['name'],
        unit_class=player_class,
        stamina_points=data['player']['stamina'],
        health_points=data['player']['health'],
        weapon=player_weapon,
        armor=player_armor)

    enemy_weapon = Weapon(
        name=data['enemy']['weapon'],
        max_damage=data['enemy']['weapon_max'],
        min_damage=data['enemy']['weapon_min'])
    enemy_armor = Armor(
        name=data['enemy']['armor'],
        defence=data['enemy']['defence'])
    enemy_class = UnitClass(
        name=data['enemy']['class'],
        max_health=data['enemy']['max_health'],
        max_stamina=data['enemy']['max_stamina'])
    enemy = Unit(
        name=data['enemy']['name'],
        unit_class=enemy_class,
        stamina_points=data['enemy']['stamina'],
        health_points=data['enemy']['health'],
        weapon=enemy_weapon,
        armor=enemy_armor)

    heroes = Heroes(player=player, enemy=enemy)
    return heroes


if __name__ == '__main__':
    print(get_game_status(0))
