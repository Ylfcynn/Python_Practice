'''
This is Doby's first Python program. This program will create a madlib.
(This is known as the 'Module level docstring'.)
'''


#    ^^ Two new lines for PEP8
# Code goes below

# Data collection phase

# Output phase
def retort(name, birth_place, color):
    about_me = 'My name is {0}. I was born in {1}. My favorite color is {2}.'.format(name, birth_place, color)
    spit_it_out = print(about_me)
    return spit_it_out


def gather():
    name = input('What is your name? >> ')
    birth_place = input('Where were you born? >> ')
    color = input('What is your favorite color? >> ')
    retort(name, birth_place, color)


gather()

'''
My name is Doby. I was born in Peoria, IL. My favorite color is cerulean.
'''