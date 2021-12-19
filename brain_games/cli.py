"""CLI."""

import prompt


def welcome_user():
    """User presentation."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))
