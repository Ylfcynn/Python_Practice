"""
This is an arbitrary program to test with PyCharm's built-in debugger.
"""

def palindrome_checker(word):
    backwards = word[::-1]
    if backwards == word:
        print('It\'s a palindrome!')
    else:
        print('Nope.')

def gather():
    word = input('Gimme a word:')
    palindrome_checker(word)

gather()