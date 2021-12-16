"""CLI."""


import prompt


def welcome_user():
    """
    Return a user presentation.

    Returns:
        str
    """
    name = prompt.string('May I have your name? ')
    return 'Hello, {name}!'.format(name=name)


def engine(game_description, get_gamedata):
    """
    Run main logic for brain-games.

    Args:
        game_description (str): a game description for the specific game
        get_gamedata (func): return a list of strings representing a gamedata
    """
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=user_name))
    print(game_description)

    game_step = 1
    final_step = 3

    while game_step <= final_step:
        (question, right_answer) = get_gamedata()
        print('Question: {question}'.format(question=question))
        user_answer = prompt.string('Your answer: ')
        if user_answer == right_answer:
            print('Correct!')
            game_step += 1
        else:
            print(
                '"{user_answer}" is wrong answer ;( '
                'Correct answer was "{right_answer}".'.format(
                    user_answer=user_answer, right_answer=right_answer,
                ))
            print("Let's try again, {user_name}!".format(user_name=user_name))
            return
    print('Congratulations, {user_name}!'.format(user_name=user_name))
