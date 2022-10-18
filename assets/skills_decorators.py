from functools import wraps
from typing import Callable

from exceptions import SkillUsedUp, NotEnoughStamina


def skill_name(name: str) -> Callable:
    skill_name.name = name

    def inner_dec(func: Callable):
        func.name = skill_name.name
        # print('Wrapped with name:', skill_name.name)

        # @wraps(func)
        # def _wrapper(*args, **kwargs):
        return func

        # return _wrapper

    return inner_dec


def max_uses(times: int) -> Callable:
    max_uses.counter = times

    def inner_dec(func: Callable):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            if max_uses.counter == 0:
                raise SkillUsedUp

            max_uses.counter -= 1
            # print('skill used')
            return func(*args, **kwargs)

        return _wrapper

    return inner_dec


def required_stamina(stamina: float) -> Callable:
    required_stamina.value = stamina

    def inner_dec(func: Callable):
        @wraps(func)
        def _wrapper(battle):
            if battle.active_unit.stamina < required_stamina.value:
                raise NotEnoughStamina

            return func(battle)

        return _wrapper

    return inner_dec

# vampire
# football player

@max_uses(8)
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
