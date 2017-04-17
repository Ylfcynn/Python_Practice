'''
(This is an example of a random chooser by Kieran.)


import random

students = ['Doby', 'Rebecca', 'Steve']

def random_chooser(students):
    for _ in range(0, 1000):   # _ is a throwaway variable naming convention.
        random.shuffle(students)
    while len(students) > 0
        choice = students.pop()   #.pop returns what you're 'popping off', mutating the original list, instead of 'none' like most list methods.
        print(choice)

'''

