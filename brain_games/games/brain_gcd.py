"""brain-gcd game logic."""

from random import randint

from brain_games.index import engine

GAME_DESCRIPTION = 'Find the greatest common divisor of the given numbers.'
MIN_NUM = 1
MAX_NUM = 100


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
    first_num = randint(MIN_NUM, MAX_NUM)
    second_num = randint(MIN_NUM, MAX_NUM)

    question = '{0} {1}'.format(first_num, second_num)
    right_answer = str(get_gcd(first_num, second_num))

    return (question, right_answer)


def brain_gcd():
    """
    Run brain-gcd game.

    Returns:
        function: a function for execute the brain-gcd game
    """
    return engine(GAME_DESCRIPTION, get_gamedata)
