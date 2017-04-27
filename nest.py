"""
>>> letters = [['a', 'b', 'c'], ['d', 'e', 'f', 'g'], ['h', 'i']]

>>> denest(letters)
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
"""


def denest(letters):

    spew = [letter for letter in letters for letter in letter]

    return spew