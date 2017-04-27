def pretty_print(fuglist):
    """This function inserts parentheses and hyphens at the correct places in a phone number."""
    fuglist.insert(0, '(')
    fuglist.insert(4, ')')
    fuglist.insert(8, '-')
    pretty = ''.join(fuglist)
    print(pretty)


def gather():
    fugly = input('Enter a telephone number without punctuation (e.g. 1234567891): ')
    if fugly.isdigit():
        fuglist = list(fugly)
        pretty_print(fuglist)

    else:
        print('Uh oh! Punctuation detected. Please try again.')


gather()