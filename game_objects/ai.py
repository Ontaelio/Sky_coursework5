from random import randrange
from typing import Callable

from exceptions import SkillUsedUp, NotEnoughStamina, SomethingWentWrong


class AI:

    @classmethod
    def robot_action(cls, battle, chance: int = 10) -> str:
        if not randrange(chance):
            try:
                return battle.use_skill()
            except SomethingWentWrong as e:
                pass
        return battle.make_attack()
