"""

##### Instructions

Here are the rules for the FizzBuzz problem:

Given the length of the output of numbers from 1 - n:
If a number is divisible by 3, append "Fizz" to a list.
If a number is divisible by 5, append "Buzz" to that same list.
If a number is divisible by both 3 and 5, append "FizzBuzz" to the list.
If a number meets none of these rules, just append the string of the number.

Append each value to a list starting with 1, and ending at `n` and return the resulting list.

>>> fizz_buzz(15)
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']

REMEMBER: Use Encapsulation! D.R.Y.
>>> joined_buzz(15)
'1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz'

"""


def fizz_buzz(n):
    fizzy_list = list()
    for i in range(1, n+1):

        if i % 3 == 0 and i % 5 == 0:
            fizzy_list.append('FizzBuzz')

        elif i % 3 == 0:
            fizzy_list.append('Fizz')

        elif i % 5 == 0:
            fizzy_list.append('Buzz')

        else:
            fizzy_list.append(str(i))

    return fizzy_list


def joined_buzz(n):
    fizzy_string = ' '.join(fizz_buzz(n))

    return fizzy_string


"""
Ex. from Ned Batchelder -- bit.ly/pyiter

def evens(stream):
    for n in stream:
        if n % 2 == 0:
            yield n

    for n in evens(nums):
        do something(n)
"""