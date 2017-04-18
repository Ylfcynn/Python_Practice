import random

answer = input('Are you feeling lucky punk? ')

affirmative = ['yes', 'Yes', 'yeah', 'Yeah', 'yea', 'Yea', 'uh huh', 'uh huh']

if answer in affirmative:
    spin = (random.randrange(1, 6,))
    if spin in range(1, 5):
        print('<click>')

    else:
        print('<bang>')

else:
    print('<bang>')