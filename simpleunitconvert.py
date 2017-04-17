'''
This is a unit converion Python program. It will prompt the user for a number of miles and converts to feet.

It will use input(), int(), and operator Module, and other stuff.
'''


#    ^^ Two new lines for PEP8
# Code goes below


# Data collection phase

def gather():
    answer = input('Enter the number of miles.  >>')
    number = int(answer)

'''
The two lines above are equivalent to this: number = int(input('Enter the number of miles.  >>'))
'''

feet = number * 5280


# Output phase
print('There are', feet, 'feet in', answer, 'miles.')

'''
This is a way of accomplishing the same thing with functions.

def pretty_print(feet, miles):
    print('There are', feet, 'feet in', miles, 'miles.')


def calculate(miles):
    feet = miles * 5280
    pretty_print(feet, miles)


def gather():
    '''Data collection phase'''
    answer = input('Enter the number of miles.  >>')
    number = int(answer)
    calculate(number)

def run():
    gather()

run()
'''
