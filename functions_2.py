"""

>>> combine(7, 4)
11

>>> combine(42)
42

>>> combine_many(980, 667, 4432, 788, 122, 9, 545, 222)
7765

>>> choose_longest("Greg", "Rooney")
'Rooney'

>>> choose_longest("Greg", "Rooney", "Philip", "Maximus", "Gabrielle")
'Gabrielle'

>>> choose_longest("Greg", [0, 0, 0, 0, 4])
[0, 0, 0, 0, 4]

"""


def combine(romulus, remus=0):

    brothers = [romulus, remus]    # This also works: result = romulus + remus
    result = sum(brothers)
    return result


def combine_many(*args):
    return sum(args)


def choose_longest(*args):
    good_seq = sorted(args, key=len, reverse=True)
    return good_seq[0]



