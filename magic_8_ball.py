"""

Write a tet based python game to simulate a classic "Magic Eight Ball".

##### Instructions

- Print a welcome screen to the user.
- use the random module's `random.choice()` to choose a prediction (or with your own clever logic).
- Display the result of the 8 ball.
- Ask the user if they want to play again.
- Say Goodbye on exit.

#### Documentation

1. [Python Official: Random: `random.choice()`](https://docs.python.org/3/library/random.html#random.choice)

#### Key Concepts

- Event Loops
- User I/O
- Random Module

"""

import random

import sys

import time

affirmatives = ['yes', 'yeah', 'yea', 'yup', 'yass', 'y', 'ya', 'gea', 'ok']

"""
I can't take credit for the slow_print function. I found this trick on http://stackoverflow.com/
"""


def slow_print(type_out):
    """Slows printing to emulate natural typing."""
    for letter in type_out:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.125)


def gather_more():
    """Follow up user-input boolean processor."""
    print('')
    type_out = 'Have I slaked your thirst to know? '
    slow_print(type_out)
    yea_or_nay_for_more = input('>> ')

    if yea_or_nay_for_more in affirmatives:
        type_out = '''
            "Perhaps one day men will no longer be interested in the unknown, no longer tantalized by mystery. \n
             This is possible, but when man loses his curiosity one feels he will have lost most of the other \n
             things that make him human." \n
             Arthur C. Clarke, The Promise of Space \n
             Stay curious my friend.'''

        slow_print(type_out)

    else:
        type_out = 'Ask away. '
        slow_print(type_out)
        query = input('>> ')
        cleromancer(query)


def positives(roll):
    if roll == 1:
        type_out = 'Totally dude.'
        slow_print(type_out)
        gather_more()

    if roll == 2:
        type_out = 'Yup.'
        slow_print(type_out)
        gather_more()

    if roll == 3:
        type_out = 'That\'s an affirm.'
        slow_print(type_out)
        gather_more()

    if roll == 4:
        type_out = 'Without a doubt.'
        slow_print(type_out)
        gather_more()

    if roll == 5:
        type_out = 'Uh, lemme check my Magic 8 Ball.                                       \nYeah, man. Definitely.'
        slow_print(type_out)
        gather_more()

    if roll == 6:
        type_out = 'Abso-frickin-lutely.'
        slow_print(type_out)
        gather_more()

    if roll == 7:
        type_out = 'Probably. It\'s a good bet.'
        slow_print(type_out)
        gather_more()

    if roll == 8:
        type_out = 'Is the Pope Catholic?'
        slow_print(type_out)
        gather_more()

    if roll == 9:
        type_out = 'Yessiree.'
        slow_print(type_out)
        gather_more()

    if roll == 10:
        type_out = 'My alt-right neighbor says no so I\'m pretty sure the answer\'s yes.'
        slow_print(type_out)
        gather_more()


def neutrals(roll):
    if roll == 11:
        type_out = 'Sorry, I wasn\'t listening.'
        slow_print(type_out)
        gather_more()

    if roll == 12:
        type_out = 'That\'s a dumb question so I\'m just gunna laugh at you now.\nlol'
        slow_print(type_out)
        gather_more()

    if roll == 13:
        type_out = 'I\'ve decided it would be funny if I didn\'t tell you.'
        slow_print(type_out)
        gather_more()

    if roll == 14:
        type_out = 'Uh...you\'re not going to believe this but my hovercraft is full of eels. brb     '
        slow_print(type_out)
        gather_more()

    if roll == 15:
        type_out = 'Ummm, who are you again?'
        slow_print(type_out)
        gather_more()


def negatives(roll):
    if roll == 16:
        type_out = 'Totally negatory.'
        slow_print(type_out)
        gather_more()

    if roll == 17:
        type_out = 'Nope.'
        slow_print(type_out)
        gather_more()

    if roll == 18:
        type_out = 'I asked this chick down at the bar that same question and she said, \"Never in a thousand years.\"'
        slow_print(type_out)
        gather_more()

    if roll == 19:
        type_out = 'Like that\'s ever gunna happen. lol'
        slow_print(type_out)
        gather_more()

    if roll == 20:
        type_out = 'Wow, really? Never dude. Stupid question.'
        slow_print(type_out)
        gather_more()


def cleromancer(query):
    roll = random.randrange(1, 20, )

    if roll in range(1, 10):
        positives(roll)

    elif roll in range(11, 15):
        neutrals(roll)

    else:
        negatives(roll)


def gather():
    """
    Prints a welcome screen to the user and gathers initial input (boolean).
    """
    type_out = '''I am Magic 8 Ball!\nI answer questions, any and all.\nBut take care in your play.\nYou may not like what I have to say.\nDo you wish to ask me something? '''
    slow_print(type_out)
    yea_or_nay_to_play = input('>> ').lower()

    if yea_or_nay_to_play in affirmatives:
        type_out = 'Ask away. '
        slow_print(type_out)
        query = input('>> ')
        cleromancer(query)

    else:
        type_out = 'Fine then. Go away. \n'
        slow_print(type_out)


gather()