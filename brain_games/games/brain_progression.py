"""brain-progression game logic."""

from random import randint

from brain_games.index import engine

GAME_DESCRIPTION = 'What number is missing in the progression?'
MIN_NUM = 1
MAX_NUM = 10
PROGRESSION_LENGTH = 10


def get_gamedata():
    """
    Generate gamedata for the brain-progression game.

    Returns:
        tuple: a tuple representing a gamedata
    """
    start = randint(MIN_NUM, MAX_NUM)
    delta = randint(MIN_NUM, MAX_NUM)

    progression = [str(start + delta * i) for i in range(0, PROGRESSION_LENGTH)]

    random_index = randint(0, PROGRESSION_LENGTH - 1)
    right_answer = progression[random_index]
    progression[random_index] = '..'
    question = ' '.join(progression)

    return (question, right_answer)


def brain_progression():
    """
    Run brain-progression game.

    Returns:
        function: a function for execute the brain-progression game
    """
    return engine(GAME_DESCRIPTION, get_gamedata)
