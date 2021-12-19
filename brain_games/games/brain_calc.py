"""brain-calc game logic."""

from random import choice, randint

from brain_games.cli import engine

game_description = 'What is the result of the expression?'


def calc(first_num, second_num, operator):
    """
    Calculate the operation depending on the operator.

    Args:
        first_num : a number
        second_num: a number
        operator (str): an operator for the operation

    Returns:
        (num) a result of the operation
    """
    if operator == '+':
        return first_num + second_num
    elif operator == '-':
        return first_num - second_num
    return first_num * second_num


def get_gamedata():
    """
    Generate gamedata for the brain-calc game.

    Returns:
        tuple: a tuple representing a gamedata
    """
    first_num = randint(1, 10)
    second_num = randint(1, 10)
    operators = ('+', '-', '*')
    operator = choice(operators)

    question = '{0} {1} {2}'.format(first_num, operator, second_num)
    right_answer = str(calc(first_num, second_num, operator))
    return (question, right_answer)


def brain_calc():
    """
    Run brain-calc game.

    Returns:
        function: a function for execute the brain-calc game
    """
    return engine(game_description, get_gamedata)
