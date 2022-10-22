class SkillUsedUp(Exception):
    message = 'Запас использований навыка исчерпан.'


class SomethingWentWrong(Exception):
    pass


class NotEnoughStamina(Exception):
    message = 'Недостаточно выносливости.'


class PlayerDies(Exception):
    message = 'Здоровье кончилось.'


class AttackBlocked(Exception):
    message = 'Броня справилась с атакой.'