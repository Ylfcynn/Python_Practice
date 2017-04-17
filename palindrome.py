"""
Write a function that returns True if the input is a palindrome, or False, if it is not.

>>> palindrome('hannah')
True

>>> palindrome('racecar')
True

>>> palindrome('a man, a plan, a canal, Panama')
True

>>> palindrome("1 pound coconut.")
False

>>> palindrome(1234321)
True

"""

def palindrome(word):
    word = str(word)    # This converts all inputs into strings. "A str of a str is ok."
    no_punc = word.replace('.', '').replace(',', '')
    no_punc_rev = no_punc[::-1]    # "This is an alien face."

    if no_punc == no_punc_rev:
        result = True
    else:
        result = False

    return result