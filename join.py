"""
Write functions that convert two input args into kebab-case sting output.

>>> link('Chuck', 'Norris')
'Chuck-Norris'

>>> link("hello", 1)
'hello-1'

>>> link(40, 2)
'40-2'
"""


def link(first, last):
    # first, last = str(first), str(last)
    words = [str(first), str(last)]   # This is a 'list literal' --> [first, last]
    kebab = '-'.join(words)
    return kebab
