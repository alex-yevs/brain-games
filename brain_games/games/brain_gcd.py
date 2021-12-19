"""brain-gcd game logic."""

from random import randint

from brain_games.cli import engine

game_description = 'Find the greatest common divisor of the given numbers.'


def get_gcd(first_num, second_num):
    """
    Calculate the greatest common divisor of the given numbers.

    Args:
        first_num : a number
        second_num: a number

    Returns:
        (num) the greatest common divisor of the given numbers
    """
    rest = first_num % second_num
    if rest == 0:
        return second_num
    return get_gcd(second_num, rest)


def get_gamedata():
    """
    Generate gamedata for the brain-gcd game.

    Returns:
        tuple: a tuple representing a gamedata
    """
    first_num = randint(1, 100)
    second_num = randint(1, 100)

    question = '{0} {1}'.format(first_num, second_num)
    right_answer = str(get_gcd(first_num, second_num))

    return (question, right_answer)


def brain_gcd():
    """
    Run brain-gcd game.

    Returns:
        function: a function for execute the brain-gcd game
    """
    return engine(game_description, get_gamedata)
