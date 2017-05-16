"""
Goal

Write a function which returns whether a string containing a credit card number is valid as a boolean.
Write as many sub-functions as necessary to solve the problem.
Write doctests for each function.

--------------------

Instructions

1. Slice off the last digit. That is the **check digit**.
2. Reverse the digits.
3. Double every other element in the reversed list.
4. Subtract nine from numbers over nine.
5. Sum all values.
6. Take the second digit of that sum.
7. If that matches the check digit, the whole card number is valid.

For example, the worked out steps would be:

1. `4  5  5  6  7  3  7  5  8  6  8  9  9  8  5  5`
2. `4  5  5  6  7  3  7  5  8  6  8  9  9  8  5`
3. `5  8  9  9  8  6  8  5  7  3  7  6  5  5  4`
4. `10 8  18 9  16 6  16 5  14 3  14 6  10 5  8`
5. `1  8  9  9  7  6  7  5  5  3  5  6  1  5  8`
6. 85
7. 5
8. Valid!
"""


def slicer(account_number: int) -> str:       # Is this a string?
    """
    
    :param account_number: 
    :return: 
    """
    check_digit = str(account_number.pop())
    return check_digit


def reverser(account_number):
    """
    
    :param check_digit: 
    :return: 
    """
    srebmun = account_number[::-1]
    return srebmun


def doubler(srebmun: str):
    """
    
    :param srebmun: 
    :return: 
    """
    plastic_fantastic = list()

    for n in range(len(srebmun)):
        elem = srebmun[n]
        if n % 2 == 0:
            elemite = elem * 2
        else:
            elemite = elem
        plastic_fantastic.append(elemite)

    return plastic_fantastic


def deninerizer(plastic_fantastic):
    """
    
    :param plastic_fantastic: 
    :return: 
    """
    plastic_bombastic = list()

    for n in range(len(plastic_fantastic)):
        num = plastic_fantastic[n]
        if num > 9:
            plastic_bombastic.append(num - 9)
        else:
            plastic_bombastic.append(num)

    return plastic_bombastic


def combiner(plastic_bombastic:list) -> int:    # Reduction op
    """
    
    :param plastic_bombastic: 
    :return: 
    """
    big_num = str(sum(plastic_bombastic))
    return big_num


def seconde(plastic_bombastic: list) -> str:
    """
    
    :param big_num: 
    :return: 
    """
    digi_two = str(sum(plastic_bombastic))[1]
    return digi_two


def comparator(digi_two: int, check_digit:int) -> str:
    """
    
    :param account_number: 
    :return: 
    """
    suffix = 'valid'    # So, so, so, dry. Dessicated in fact.

    if digi_two == check_digit:
        result = f'{suffix}!'
    else:
        result = f'In{suffix}!'

    return result


def validate(account_number: list) -> None:
    """
    
    :param account_number: 
    :return: 
    """
    check_digit = slicer(account_number)
    print(f'Check digit: {check_digit}')

    srebmun = reverser(account_number)

    plastic_fantastic = doubler(srebmun)

    plastic_bombastic = deninerizer(plastic_fantastic)

    big_num = combiner(plastic_bombastic)

    digi_two = seconde(big_num)

    comparator(digi_two, check_digit)


account_number_1 = [4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5]
account_number_2 = [6, 5, 1, 6, 4, 3, 7, 5, 1, 6, 4, 9, 3, 8, 5, 4]

validate()


