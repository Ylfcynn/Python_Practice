"""
>>> arb(1, 2, 3, 4, 5, True, None, False, 'Python')
The 9 args are: (1, 2, 3, 4, 5, True, None, False, 'Python')

>>> arb(1, None)
The 2 args are: (1, None)


>>> stats(1, 67, 88, 44, 55, 33, 44, 22, 55, 7, 88, 9, 55, 66, 44, 33, 876)
Sum: 1587
Max: 876
Min: 1
Avg: 93
Range: 875
Entries: 17

"""


def arb(*args):
    print(f'The {len(args)} args are: {args}')


def stats(*data):
    adder = f'Sum: {sum(data)}'
    print(adder)

    biggest = f'Max: {max(data)}'
    print(biggest)

    littlest = f'Min: {min(data)}'
    print(littlest)

    mean = f'Avg: {sum(data)//len(data)}'
    print(mean)

    max_less_min = f'Range: {max(data)-min(data)}'
    print(max_less_min)

    how_many = f'Entries: {len(data)}'
    print(how_many)
