from game_objects.units import BaseHero


def get_verbose_stats(unit: BaseHero) -> dict:
    return {
        "name": unit.name,
        "class": unit.role.name,
        "weapon": f"Оружие: {unit.weapon.name}, урон: {unit.weapon.min_damage:.1f} - {unit.weapon.max_damage:.1f}",
        "armor": f"Броня: {unit.armor.name}, защита: {unit.armor.defence:.1f}",
        "health": f"Очки здоровья: {unit.health:.1f}/{unit.role.max_health:.1f}",
        "stamina": f"Очки выносливости: {unit.stamina:.1f}/{unit.role.max_stamina:.1f}"
    }


def get_unit_stats(unit: BaseHero) -> dict:
    return {
        "name": unit.name,
        "health": round(unit.health, 1),
        "stamina": round(unit.stamina, 1)
    }


def get_unit_stats_full(unit: BaseHero) -> dict:
    return {
        "name": unit.name,
        "class": unit.role.name,
        "health": round(unit.health, 1),
        "max_health": unit.role.max_health,
        "stamina": round(unit.stamina, 1),
        "max_stamina": unit.role.max_stamina,
        "weapon": unit.weapon.name,
        "weapon_min": unit.weapon.min_damage,
        "weapon_max": unit.weapon.max_damage,
        "armor": unit.armor.name,
        "defence": unit.armor.defence,
    }