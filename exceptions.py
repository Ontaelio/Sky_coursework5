class SkillUsedUp(Exception):
    message = 'Запас использований навыка исчерпан'


class NotEnoughStamina(Exception):
    message = 'Недостаточно выносливости.'


class PlayerDies(Exception):
    message = 'Здоровье кончилось'