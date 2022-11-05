from dataclasses import dataclass
from typing import Callable

import assets.skills


@dataclass(frozen=True)
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack_mod: float
    stamina_mod: float
    armor_mod: float
    skill: Callable
    skill_uses: int


ROLES = {
    'Воин': UnitClass(
        name='Воин',
        max_health=60.0,
        max_stamina=30.0,
        attack_mod=0.8,
        stamina_mod=0.9,
        armor_mod=1.2,
        skill=assets.skills.ferocious_kick,
        skill_uses=1
    ),

    "Вор": UnitClass(
        name='Вор',
        max_health=60.0,
        max_stamina=30.0,
        attack_mod=0.8,
        stamina_mod=0.9,
        armor_mod=1.2,
        skill=assets.skills.mighty_jab,
        skill_uses=1
    ),

    "Лекарь": UnitClass(
        name='Лекарь',
        max_health=40.0,
        max_stamina=25.0,
        attack_mod=0.5,
        stamina_mod=1.8,
        armor_mod=1.0,
        skill=assets.skills.greedy_healer,
        skill_uses=3
    ),

    "Футболист": UnitClass(
        name="Футболист",
        max_health=25.0,
        max_stamina=60.0,
        attack_mod=1.2,
        stamina_mod=4.1,
        armor_mod=0.1,
        skill=assets.skills.penalty_kick,
        skill_uses=9999
    ),

    "Вампир": UnitClass(
        name="Вампир",
        max_health=25.0,
        max_stamina=100.0,
        attack_mod=0.8,
        stamina_mod=1.1,
        armor_mod=1.5,
        skill=assets.skills.vampire_bite,
        skill_uses=9999
    ),

    "Волшебник": UnitClass(
        name="Волшебник",
        max_health=25.0,
        max_stamina=30.0,
        attack_mod=0.4,
        stamina_mod=7.1,
        armor_mod=1.5,
        skill=assets.skills.magic_spell,
        skill_uses=9999
    )
}

# here be tests

if __name__ == '__main__':
    a1 = ROLES['Воин']
    a2 = ROLES['Лекарь']

    print(a1)
    print(a2.skill)
