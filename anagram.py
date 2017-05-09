"""
>>> is_anagram('anagram', 'nag a ram')
True

>>> is_anagram('Right. One... two... five!', 'Three, sir.')
False

>>> is_anagram('My ideal time', 'Immediately')
True


Doby's approach to this problem is to generate a numerical 'signature' for each lexical input and compare.

"""


import string


def anagram_proc(word):
    """
    For each input, builds a list of only lowercase letters, 'nekked_little', and generates a second list, 'digisig'. by 
    counting incidences of letters in nekked_little. digi_sig is a list of integers.
    
    """

    alphabet = string.ascii_lowercase

    squashed = word.casefold()

    nekked_little = list()

    for char in squashed:
        if char in alphabet:
            nekked_little.append(char)

    digisig = list()

    for letter in alphabet:
        if letter in nekked_little:
            digisig.append(nekked_little.count(letter))

    return digisig


def is_anagram(word_1, word_2):
    digisig_1 = anagram_proc(word_1)
    digisig_2 = anagram_proc(word_2)

    if digisig_1 == digisig_2:
        return True

    else:
        return False
