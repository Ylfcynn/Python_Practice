"""
Doby's broken solution.

>>> locate('l', 'hello')
[2, 3]

>>> locate('b', 'bannanas')
[0]

>>> locate('i', 'mississippi')
[1, 4, 7, 10]


Kieran's solutions

for index, char in enumerate:
    if char == target:
    print(index)

Also...

[index for index, char in enumerate(word) if char == target]


"""


spew = list()


def locate(letter, lexis):


    print(spew)
