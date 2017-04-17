"""
Return the number of letter occourances in a string.
>>> count_letter('i', 'Antidisestablishmentterianism')
5
>>> count_letter('p', 'Pneumonoultramicroscopicsilicovolcanoconiosis')
2


Return the letter that appears last in the engligh alphabet.
>>> latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')
'the latest letter is v.'

>>> latest_letter('doby')
'the latest letter is y.'


Convert input strings to lowercase without any surrounding whitespace.
>>> lower_case("SUPER!")
'super!'
>>> lower_case("        NANNANANANA BATMAN        ")
'nannananana batman'

"""

def count_letter(letter, word):
    word = word.lower()
    count = word.count(letter)
    return count

def latest_letter(sucks_to_be_you):
    straggler = max(sucks_to_be_you)
    return 'the latest letter is {}.'.format(straggler)

def lower_case(exclaim):
    miniscule = exclaim.lower()
    terse = miniscule.strip()
    return terse
