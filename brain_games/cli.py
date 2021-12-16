"""User presentation."""


import prompt


def welcome_user():
    """User presentation function."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))
