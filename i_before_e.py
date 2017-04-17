"""
Check that a word follows "I before E except after C".

>>> check("recieve")
receive doesn't follow the rule


>>> check("receive")
receive does follow the rule

"""

def check(word):

    if word.count('cei', 0, len(word)):
        print('receive does follow the rule')

    else:
        print('receive doesn\'t follow the rule')

