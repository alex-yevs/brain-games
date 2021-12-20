"""Main logic for brain-games."""

import prompt

FINAL_STEP = 3


def engine(game_description, get_gamedata):
    """
    Run main logic for brain-games.

    Args:
        game_description (str): a game description for the specific game
        get_gamedata (func): return a tuple (question, right_answer)
    """
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(user_name))
    print(game_description)

    game_step = 1

    while game_step <= FINAL_STEP:
        (question, right_answer) = get_gamedata()
        print('Question: {0}'.format(question))
        user_answer = prompt.string('Your answer: ')
        if user_answer == right_answer:
            print('Correct!')
            game_step += 1
        else:
            print(
                '"{0}" is wrong answer ;( Correct answer was "{1}".'.format(
                    user_answer, right_answer,
                ))
            print("Let's try again, {0}!".format(user_name))
            return
    print('Congratulations, {0}!'.format(user_name))
