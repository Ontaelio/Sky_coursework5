# from game_objects.arena import Arena
# from game_objects.units import BaseHero

#import game_objects.arena
#import game_objects.units

from exceptions import SkillUsedUp, NotEnoughStamina, PlayerDies


class Battle:
    def __init__(self, arena, player, enemy):
        self.arena = arena
        self.player = player
        self.enemy = enemy
        self.active_unit = self.player
        self.target_unit = self.enemy

    def restore_stamina(self):
        self.player.change_stamina(self.arena.stamina)
        self.enemy.change_stamina(self.arena.stamina)

    def attack(self) -> str:
        try:
            self.active_unit.change_stamina(- self.active_unit.weapon.stamina_per_hit)
        except NotEnoughStamina:
            return f'{self.active_unit.name} попытался использовать {self.active_unit.weapon.name}, но у него не хватило выносливости.'

        try:
            self.target_unit.change_stamina(- self.target_unit.armor.stamina_per_turn)
            protection = self.target_unit.protection
        except NotEnoughStamina:
            protection = 0

        attack = self.active_unit.damage
        damage = round(attack - protection, 1)

        if damage <= 0:
            return f"{self.active_unit.name}, используя {self.active_unit.weapon.name}, наносит удар, " \
                   f"но {self.target_unit.armor.name} соперника его останавливает."

        result = f"{self.active_unit.name}, используя {self.active_unit.weapon.name}, пробивает " \
                 f"{self.target_unit.armor.name} соперника и наносит {damage} урона."

        try:
            self.target_unit.change_health(-damage)
        except PlayerDies:
            result += f" {self.active_unit.name} выиграл битву!"

        return result

    def swap_units(self):
        self.active_unit, self.target_unit = self.target_unit, self.active_unit

    @property
    def someone_died(self):
        return not (self.player.health > 0 and self.enemy.health > 0)

