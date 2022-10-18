from random import randrange
from typing import Callable, Optional
from abc import ABC, abstractmethod

from assets.unit_classes import UnitClass
from game_objects.equipment import Weapon, Armor
from exceptions import SkillUsedUp, NotEnoughStamina, PlayerDies


class BaseHero(ABC):
    def __init__(self, name: str, unit_class: UnitClass):
        self.name: str = name
        self.role: UnitClass = unit_class
        self._health: float = unit_class.max_health
        self._stamina: float = unit_class.max_stamina
        self.weapon: Optional[Weapon] = None
        self.armor: Optional[Armor] = None

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
        # if self._stamina > self.role.max_stamina:
        #     self._stamina = self.role.max_stamina

    @abstractmethod
    def action(self, act: Callable) -> str:
        pass

    def use_skill(self, *args, **kwargs) -> str:
        try:
            return self.role.skill(*args, **kwargs)
        except SkillUsedUp as e:
            return e.message
        except NotEnoughStamina:
            return f'{self.name} пытается использовать {self.role.skill.name}, но не хватает выносливости.'


class PlayerHero(BaseHero):
    def action(self, act: Callable) -> str:
        return 'Not implemented'


class RobotHero(BaseHero):
    def action(self, act: Callable) -> str:
        if not randrange(10):
            try:
                return self.use_skill()
            except (SkillUsedUp, NotEnoughStamina) as e:
                pass
        return 'Not implemented'






