#!usr/bin/env python3

"""Script for brain-games."""

from brain_games.cli import welcome_user


def main():
    """Run brain-games."""
    print('Welcome to the Brain Games!')
    print(welcome_user())


if __name__ == '__main__':
    main()
