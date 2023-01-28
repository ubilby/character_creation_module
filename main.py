from random import randint

from graphic_arts.start_game_banner import run_screensaver

DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10


class Character:
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'
    RANGE_VALUE_ATTACK = (1, 3)
    RANGE_VALUE_DEFENCE = (1, 5)
    SPECIAL_BUFF = 15
    SPECIAL_SKILL = 'Удача'

    def __init__(self, name: str):
        self.name: str = name

    def atack(self):
        """Метод атаки базового класса."""
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный {value_attack}')

    def defence(self):
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {value_defence} ед. урона.')

    def special(self):
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".')

    def __str__(self):
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.'


class Warrior(Character):
    pass


class Mage(Character):
    pass


class Healer(Character):
    pass


def attack(char_name: str, char_class: str) -> str:
    """Atack function."""
    if char_class == 'warrior':
        damage: int = 5 + randint(3, 5)
        return (f'{char_name} нанёс урон противнику равный {damage}')
    if char_class == 'mage':
        damage = 5 + randint(5, 10)
        return (f'{char_name} нанёс урон противнику равный {damage}')
    if char_class == 'healer':
        damage = 5 + randint(-3, -1)
        return (f'{char_name} нанёс урон противнику равный {damage}')

    return '{char_name} не нанес никакого урона'


def defence(char_name: str, char_class: str) -> str:
    """Defence function."""
    if char_class == 'warrior':
        block: int = 10 + randint(5, 10)
        return (f'{char_name} блокировал {block} урона')

    if char_class == 'mage':
        block = 10 + randint(-2, 2)
        return (f'{char_name} блокировал {block} урона')

    if char_class == 'healer':
        block = 10 + randint(2, 5)
        return (f'{char_name} блокировал {block} урона')

    return f'{char_name} ничего не блокировал'


def special(char_name: str, char_class: str) -> str:
    """Function os specail skill"""
    if char_class == 'warrior':
        skill: int = 80 + 25
        return (
            f'{char_name} применил специальное умение «Выносливость {skill}»')
    if char_class == 'mage':
        skill = 5 + 40
        return (f'{char_name} применил специальное умение «Атака {skill}»')
    if char_class == 'healer':
        skill = 10 + 30
        return (f'{char_name} применил специальное умение «Защита {skill}»')

    return f'{char_name} не применил специальное умение'


def start_training(char_name: str, char_class: str) -> str:
    """Start training funcrion"""
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника '
          'или special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = ""
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Choice class function."""
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        char_class = input(
            'Введи название персонажа, за которого хочешь '
            'играть: Воитель — warrior, Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. '
                  'Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. '
                  'Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. '
                  'Черпает силы из природы, веры и духов.')
        approve_choice = input(
            'Нажми (Y), чтобы подтвердить выбор, или любую другую кнопку, '
            'чтобы выбрать другого персонажа').lower()
    return char_class


def main() -> None:
    """Main function."""
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))


if __name__ == '__main__':
    main()
