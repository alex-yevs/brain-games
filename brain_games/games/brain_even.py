"""brain-even game logic."""

from random import randint

from brain_games.cli import engine


def is_even(num):
    """
    Check if the number is even.

    Args:
        num: number

    Returns:
        bool
    """
    return num % 2 == 0


game_description = 'Answer "yes" if the number is even, otherwise answer "no"'


def get_gamedata():
    """
    Generate gamedata for brain-even game.

    Returns:
        list: a list of strings representing a gamedata
    """
    question = randint(0, 100)
    right_answer = 'yes' if is_even(question) else 'no'
    return (str(question), right_answer)


def brain_even():
    """
    Run brain-even game.

    Returns:
        function: a function for execute the brain-even game
    """
    return engine(game_description, get_gamedata)
