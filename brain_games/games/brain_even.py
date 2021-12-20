"""brain-even game logic."""

from random import randint

from brain_games.index import engine

GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no"'
MIN_NUM = 0
MAX_NUM = 100


def is_even(num):
    """
    Check if the number is even.

    Args:
        num: number

    Returns:
        bool
    """
    return num % 2 == 0


def get_gamedata():
    """
    Generate gamedata for the brain-even game.

    Returns:
        tuple: a tuple representing a gamedata
    """
    question = randint(MIN_NUM, MAX_NUM)
    right_answer = 'yes' if is_even(question) else 'no'

    return (question, right_answer)


def brain_even():
    """
    Run brain-even game.

    Returns:
        function: a function for execute the brain-even game
    """
    return engine(GAME_DESCRIPTION, get_gamedata)
