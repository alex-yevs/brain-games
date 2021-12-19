"""brain-progression game logic."""

from random import randint

from brain_games.index import engine

game_description = 'What number is missing in the progression?'


def get_gamedata():
    """
    Generate gamedata for the brain-progression game.

    Returns:
        tuple: a tuple representing a gamedata
    """
    start = randint(1, 10)
    delta = randint(1, 10)
    progression_length = 10
    progression = [str(start + delta * i) for i in range(0, progression_length)]

    random_index = randint(0, progression_length - 1)
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
    return engine(game_description, get_gamedata)
