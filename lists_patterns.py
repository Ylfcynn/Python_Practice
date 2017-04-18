'''

>>> a = 'music'
>>> b = [17, 28, 42, 31, 12]

>>> display_indices(a)
m 0
u 1
s 2
i 3
c 4


>>> parallel(a, b)
m 17
u 28
s 42
i 31
c 12

'''

'''

def display_indices(a):
    # This uses a for loop with enumerate()
    # :param a: str or int
    # :param b: str or int
    # :return: None
    
    for index, elem in enumerate(a):
        print(elem, index)

def parallel(a, b):

    # This uses a for loop with zip()
    # :param a: str or int
    # :param b: str or int
    # :return: None
    
    for elem_a, elem_b in zip(a, b):
        print(elem_a, elem_b)
        
'''


'''
def display_indices(a):

    # This uses a while loop with a counter
    # :param a: str or int
    # :return: None

    counter = 0
    while counter < len(a):
        print(a[counter], counter)
        counter += 1


def parallel(a, b):

    # This uses a while loop with a counter
    # :param a: str or int
    # :param b: str or int
    # :return: None

    counter = 0
    while counter < len(a):
        print(a[counter], b[counter])
        counter += 1

'''


def display_indices(a):
    """
    This uses a for loop and range.
    
    :param a: str or int
    :param b: str or int
    :return: None
    """
    for i in range(len(a)):
        print(a[i], i)


def parallel(a, b):
    """
    This uses a for loop and range.

    :param a: str or int
    :return: None
    """
    for i in range(len(a)):
        print(a[i], b[i])





