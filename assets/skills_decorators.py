from functools import wraps
from typing import Callable

from exceptions import SkillUsedUp, NotEnoughStamina


def skill_name(name: str) -> Callable:
    skill_name.name = name

    def inner_dec(func: Callable):
        func.name = skill_name.name
        return func

    return inner_dec


def check_if_used(func) -> Callable:
    @wraps(func)
    def _wrapper(battle):
        if battle.active_unit.skill_uses == 0:
            raise SkillUsedUp

        battle.active_unit.skill_uses -= 1
        return func(battle)

    return _wrapper


def required_stamina(stamina: float) -> Callable:
    required_stamina.value = stamina

    def inner_dec(func: Callable):
        func.required_stamina = required_stamina.value

        @wraps(func)
        def _wrapper(battle):
            battle.active_unit.change_stamina(- func.required_stamina)
            return func(battle)

        return _wrapper

    return inner_dec


# vampire
# football player

@check_if_used
@required_stamina(1)
def foo(n):
    foo.name = "Me foo"
    return n * 3


# here be tests

if __name__ == '__main__':
    print(foo(2))
    print(foo(2))
    print(foo(2))
    print(foo(2))

    print(foo.name)
    print(foo)
