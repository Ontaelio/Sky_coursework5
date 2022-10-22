import json
import random
from dataclasses import dataclass, field

import marshmallow
import marshmallow_dataclass


@dataclass
class Weapon:
    idn: int = field(metadata={"data_key": "id"})
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float

    class Meta:
        unknown = marshmallow.EXCLUDE

    @property
    def damage(self):
        return round(random.uniform(self.min_damage, self.max_damage), 1)


@dataclass
class Armor:
    idn: int = field(metadata={"data_key": "id"})
    name: str
    defence: float
    stamina_per_turn: float

    class Meta:
        unknown = marshmallow.EXCLUDE


WeaponSchema = marshmallow_dataclass.class_schema(Weapon)
ArmorSchema = marshmallow_dataclass.class_schema(Armor)


@dataclass
class EquipmentList:
    weapons: list = field(default_factory=list)
    armors: list = field(default_factory=list)

    def get_data(self, file_name):
        with open(file_name, encoding="utf-8") as fin:
            data = json.load(fin)

        self.weapons = list(WeaponSchema().load(w) for w in data["weapons"])
        self.armors = list(ArmorSchema().load(a) for a in data["armors"])

    def weapon(self, name: str) -> Weapon:
        return next((w for w in self.weapons if w.name == name), NO_WEAPON)

    def armor(self, name: str) -> Armor:
        return next((ar for ar in self.armors if ar.name == name), NO_ARMOR)


NO_ARMOR = Armor(
    idn=9999,
    name='Пустота',
    defence=0,
    stamina_per_turn=0
)

NO_WEAPON = Weapon(
    idn=9999,
    name='Ничто',
    min_damage=0,
    max_damage=0.2,
    stamina_per_hit=0
)


# here be tests

if __name__ == '__main__':
    a = EquipmentList()
    a.get_data("../data/equipment.json")
    print(a.weapons)
    print(a.armors)
    print(a.weapon('топорик'))




