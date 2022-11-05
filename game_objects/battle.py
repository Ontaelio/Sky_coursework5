# from game_objects.arena import Arena
# from game_objects.units import BaseHero

# import game_objects.arena
# import game_objects.units

from exceptions import SkillUsedUp, NotEnoughStamina, PlayerDies, AttackBlocked, SomethingWentWrong, WrongEquipment


class Battle:
    def __init__(self, arena, player, enemy):
        self.arena = arena
        self.player = player
        self.enemy = enemy
        self.active_unit = self.player
        self.target_unit = self.enemy
        self.actions = {
            'attack': self.make_attack,
            'skill': self.use_skill,
            'pass': self.pass_turn
        }

    @property
    def someone_died(self):
        return not (self.player.health > 0 and self.enemy.health > 0)

    def check_for_bodies(self, string: str) -> str:
        if not self.someone_died:
            return string

        if self.active_unit.health > 0:
            return string + f" {self.active_unit.name} побеждает!"
        if self.target_unit.health > 0:
            return string + f" {self.target_unit.name} побеждает!"
        return string + " Оба героя погибают, ничья!"

    def restore_stamina(self):
        self.active_unit.change_stamina(self.arena.stamina * self.active_unit.role.stamina_mod)
        self.target_unit.change_stamina(self.arena.stamina * self.target_unit.role.stamina_mod)

    def make_attack(self) -> str:
        try:
            damage = self.active_unit.attack(self.target_unit)
        except NotEnoughStamina:
            return f'{self.active_unit.name} пытается использовать {self.active_unit.weapon.name}, ' \
                   f'но не хватает выносливости.'
        except AttackBlocked:
            return f"{self.active_unit.name}, используя {self.active_unit.weapon.name}, наносит удар, " \
                   f"но {self.target_unit.armor.name} соперника его останавливает."

        result = f"{self.active_unit.name}, используя {self.active_unit.weapon.name}, пробивает " \
                 f"{self.target_unit.armor.name} соперника и наносит {damage} урона."

        try:
            self.target_unit.change_health(-damage)
        except PlayerDies:
            result += f" {self.active_unit.name} побеждает!"

        return result

    def use_skill(self, *args, **kwargs) -> str:
        try:
            result = self.active_unit.role.skill(self, *args, **kwargs)
        except SkillUsedUp as e:
            raise SomethingWentWrong(e.message)
        except WrongEquipment:
            raise SomethingWentWrong(
                f"{self.active_unit.name} пытается использовать навык {self.active_unit.role.skill.name}, " \
                f"но экипировка не позволяет это сделать.")
        except NotEnoughStamina:
            self.active_unit.skill_uses += 1
            raise SomethingWentWrong(f"{self.active_unit.name} пытается использовать навык {self.active_unit.role.skill.name}, " \
                   f"но не хватает выносливости.")

        return self.check_for_bodies(f"{self.active_unit.name} использует навык {self.active_unit.role.skill.name} и " + result)

    def pass_turn(self) -> str:
        return f"{self.active_unit.name} пропускает ход."

    def swap_units(self):
        self.active_unit, self.target_unit = self.target_unit, self.active_unit
