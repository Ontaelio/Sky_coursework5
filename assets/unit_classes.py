from dataclasses import dataclass
from typing import Callable

import assets.skills


def foo(n):
    return n * n


@dataclass(frozen=True)
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack_mod: float
    stamina_mod: float
    armor_mod: float
    skill: Callable


WARRIOR = UnitClass(
    name='Воин',
    max_health=60.0,
    max_stamina=30.0,
    attack_mod=0.8,
    stamina_mod=0.9,
    armor_mod=1.2,
    skill=assets.skills.ferocious_kick
)


THIEF = UnitClass(
    name='Вор',
    max_health=60.0,
    max_stamina=30.0,
    attack_mod=0.8,
    stamina_mod=0.9,
    armor_mod=1.2,
    skill=assets.skills.mighty_jab
)

HEALER = UnitClass(
    name='Лекарь',
    max_health=40.0,
    max_stamina=25.0,
    attack_mod=0.6,
    stamina_mod=1.8,
    armor_mod=1.0,
    skill=assets.skills.greedy_healer
)



# here be tests

if __name__ == '__main__':
    a1 = WARRIOR
    a2 = HEALER

    print(a1)
    print(a2.skill(40))
