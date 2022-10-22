from typing import Optional

from assets.unit_classes import UnitClass
from game_objects.equipment import Weapon, Armor, NO_ARMOR, NO_WEAPON
from exceptions import SkillUsedUp, NotEnoughStamina, PlayerDies, AttackBlocked


class BaseHero:
    def __init__(self, name: str, unit_class: UnitClass):
        self.name: str = name
        self.role: UnitClass = unit_class
        self.skill_uses = self.role.skill_uses
        self._health: float = unit_class.max_health
        self._stamina: float = unit_class.max_stamina
        self.weapon: Weapon = NO_WEAPON
        self.armor: Armor = NO_ARMOR

    @property
    def health(self):
        return self._health

    @property
    def stamina(self):
        return self._stamina

    @property
    def protection(self) -> float:
        if self.stamina < self.armor.stamina_per_turn:
            return 0
        return round(self.armor.defence * self.role.armor_mod, 1)

    @property
    def damage(self) -> float:
        return round(self.weapon.damage * self.role.attack_mod, 1)

    # @health.setter
    # def health(self, val: float):
    #     self._health = val
    #
    # @stamina.setter
    # def stamina(self, val: float):
    #     self._stamina = val

    def change_health(self, val: float):
        self._health = min(self._health + val, self.role.max_health)
        if self._health <= 0:
            self._health = 0
            raise PlayerDies (f'{self.name} получает {val} урона и умирает.')
        # if self._health > self.role.max_health:
        #     self._health = self.role.max_health

    def change_stamina(self, val: float):
        if -val > self._stamina:
            raise NotEnoughStamina
        self._stamina = min(self._stamina + val, self.role.max_stamina)

    def equip(self, *args, **kwargs):
        if weapon := kwargs.get('weapon', None):
            self.weapon = weapon
        if armor := kwargs.get('armor', None):
            self.armor = armor

    def attack(self, target_unit) -> float:
        self.change_stamina(- self.weapon.stamina_per_hit)
        # print('attacker', self.name, self.health, self.stamina)

        try:
            target_unit.change_stamina(- target_unit.armor.stamina_per_turn)
            # print('defender', target_unit.name, target_unit.health, target_unit.stamina)
            protection = target_unit.protection
        except NotEnoughStamina:
            protection = 0

        damage = round(self.damage - protection, 1)
        if damage <= 0:
            raise AttackBlocked

        return damage

    def use_skill(self, *args, **kwargs) -> str:
        try:
            return self.role.skill(*args, **kwargs)
        except SkillUsedUp as e:
            return e.message
        except NotEnoughStamina:
            return f'{self.name} пытается использовать {self.role.skill.name}, но не хватает выносливости.'


# class PlayerHero(BaseHero):
#     def action(self, act: Callable) -> str:
#         return 'Not implemented'
#
#
# class RobotHero(BaseHero):
#     def action(self, act: Callable) -> str:
#         if not randrange(10):
#             try:
#                 return self.use_skill()
#             except (SkillUsedUp, NotEnoughStamina) as e:
#                 pass
#         return 'Not implemented'






