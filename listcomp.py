"""
# Test Data Below.  Leave this line alone.
>>> names = ['Kieran', 'Suki', 'Alex', 'Serada', 'Jeff', 'Fin', 'Alfonzo']

>>> folk = [('Kieran', 'Prasch', 'Instructor'), ('Alfonzo', 'Ward', 'Student'), ('Fin', 'Balnik', 'Student')]

>>> long_names(names, 5)
['Kieran', 'Serada', 'Alfonzo']

>>> starts_with(names, 'S')
['Suki', 'Serada']

>>> last_names(folk)
['Prasch', 'Ward', 'Balnik']

>>> smoosh(folk)
['Kieran', 'Prasch', 'Instructor', 'Alfonzo', 'Ward', 'Student', 'Fin', 'Balnik', 'Student']

"""


def long_names(names, length):
    result = [name for name in names if len(name) > length]
    return result


def starts_with(names, initial):
    result = [name for name in names if name[0] == initial]
    return result


def last_names(folk):
    result = [name[1] for name in folk]
    return result


def smoosh(folk):
    result = [name for name in folk for name in name]
    return result
