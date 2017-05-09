"""
Write a function that quantifies word occurrences in a given string.

>>> quantify_words("Red touching black is a friend of Jack, Red touching yellow can kill a fellow.")
Lexis: 'a', occurrences: 2
Lexis: 'black', occurrences: 1
Lexis: 'can', occurrences: 1
Lexis: 'fellow', occurrences: 1
Lexis: 'friend', occurrences: 1
Lexis: 'is', occurrences: 1
Lexis: 'jack', occurrences: 1
Lexis: 'kill', occurrences: 1
Lexis: 'of', occurrences: 1
Lexis: 'red', occurrences: 2
Lexis: 'touching', occurrences: 2
Lexis: 'yellow', occurrences: 1


>>> quantify_words("In the end, it's concluded that the airspeed velocity of a (European) unladen swallow is about 24 miles per hour or 11 meters per second.")
(european), occurrences: 1
'11', occurrences: 1
'24', occurrences: 1
'a', occurrences: 1
'about', occurrences: 1
'airspeed', occurrences: 1
'concluded', occurrences: 1
'end', occurrences: 1
'hour', occurrences: 1
'in', occurrences: 1
'is', occurrences: 1
'it's', occurrences: 1
'meters', occurrences: 1
'miles', occurrences: 1
'of', occurrences: 1
'or', occurrences: 1
'per', occurrences: 2
'second', occurrences: 1
'swallow', occurrences: 1
'that', occurrences: 1
'the', occurrences: 2
'unladen', occurrences: 1
'velocity', occurrences: 1
"""


"""
Doby's work. Please don't laugh. I'm new at this.
"""

import os

import re


def display(tallies: dict) -> None:
    """
    Prints the dictionary 'tallies' and prints them out, sorted by values.
    """
    for key, value in sorted(tallies.items(), key=lambda t: t[1], reverse=True)[:10]:
        print(f'Lexis: \'{key}\',', f'occurrences: {value}')


def lexeis_gen(phrase: str) -> str:
    """
    Scrubs punctuation, converts to lowercase

    >>> lexeis_gen('Test: An ungulatory proposition; The llamma, (John), asked, "Let us eat spam and Eggs!".')
    'Test  An ungulatory proposition  The llamma   John   asked   Let us eat spam and Eggs'   
    """

    pattern = re.compile(r'[\d!:;,\.\"()-]')
    no_punc = pattern.sub(' ', phrase)
    wee_no_punc = no_punc.lower()
    return wee_no_punc


def quantify(生: str) -> None:
    """
    Analyzes textual input for lexical frequencies and displays the most frequent occurrences in the terminal. 
    :param 生: 
    """

    cooked = lexeis_gen(生)
    lexeis = cooked.split()
    tallies = dict()
    for word in lexeis:
        try:
            tallies[word] += 1

        except KeyError:
            tallies[word] = 1

    display(tallies)


def loader() -> None:  # 'file handler'
    """
    A 'boilerplate' construction, returns file contents as a string.
    """
    path = input('Path to codex to analyze: ')  # Ex. '/Users/ylf/Git/Python_Practice/Bēowulf.txt'
    with open(path, 'r') as file:
        codex = file.read()
        quantify(codex)


loader()