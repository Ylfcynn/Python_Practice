"""

Use a list building pattern with `list.append()` to store the Fibbonacci values.

Write a function that outputs a list of fibbonacci numbers up to the ceiling _value_.

>>> fibo(10)
[0, 1, 1, 2, 3, 5, 8]

>>> fibo(20)
[0, 1, 1, 2, 3, 5, 8, 13]

>>> fibo(30)
[0, 1, 1, 2, 3, 5, 8, 13, 21]


"""

"""
Kieran showed me this solution. It is considered 'optimal'.

def fibo(ceiling):
    fibonaccia = list()

    former, latter = 0, 1         # These are seed values.

    while former < ceiling:
        fibonaccia.append(former)
        former, latter = latter, former + latter

    print(fibonaccia)

"""


"""
def fibo(ceiling):                # Infinite generator function
    fibonaccia = list()
    
    former = 0
    latter = 1
    yield former
    yield latter

    while True:                   # This loop generates numbers forever
        yield latter
        next_num = former + latter
        former = latter
        latter = next_num        

    print(fibonaccia)
"""


def fibo(ceiling):                # This is my way of doing it. I prefer a third variable.
    fibonaccia = list()

    """
    These are seed values.
    """
    former = 0
    latter = 1

    while former < ceiling:
        fibonaccia.append(former)
        next_num = former + latter
        former = latter
        latter = next_num

    print(fibonaccia)