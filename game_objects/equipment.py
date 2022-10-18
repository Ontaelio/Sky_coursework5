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


# here be tests

if __name__ == '__main__':
    a = EquipmentList()
    a.get_data("../data/equipment.json")
    print(a.weapons)
    print(a.armors)




