"""
>>> is_anagram('anagram', 'nag a ram')
True

>>> is_anagram('Right. One... two... five!', 'Three, sir.')
False

>>> is_anagram('My ideal time', 'Immediately')
True

"""

import string

word_1 = 'anagram'

word_2 = 'nag a ram'


# def is_anagram(word_1, word_2):

def is_anagram(digisig):
    digisig_1 =

    digisig_2

    if digisig_1 == digisig_2:
        return True

    else:
        return False


def digisig_gen(nekked_little):
    digisig = list()

    alphabet = string.ascii_lowercase

    for letter in alphabet:
        if letter in nekked_little
            digisig.append(nekked_little.count(letter))

    is_anagram(digisig)


def strip_and_squash(word):
    nekked_little = list()

    squashed = word.casefold()

    for char in squashed:
        if char in string.ascii_lowercase:
            nekked_little.append(char)

    digisig_gen(nekked_little)



