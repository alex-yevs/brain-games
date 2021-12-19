"""brain-prime game logic."""

from random import randint

from brain_games.index import engine

game_description = (
    'Answer "yes" if given number is prime. Otherwise answer "no".'
)


def is_prime(num):
    """
    Check if the given number is prime.

    Args:
        num : a number

    Returns:
        (bool)
    """
    if num <= 1:
        return False
    i = 2
    while i <= num ** 0.5:
        if num % i == 0:
            return False
        i += 1
    return True


def get_gamedata():
    """
    Generate gamedata for the brain-prime game.

    Returns:
        tuple: a tuple representing a gamedata
    """
    num = randint(1, 100)

    question = num
    right_answer = 'yes' if is_prime(num) else 'no'

    return (question, right_answer)


def brain_prime():
    """
    Run brain-prime game.

    Returns:
        function: a function for execute the brain-prime game
    """
    return engine(game_description, get_gamedata)
