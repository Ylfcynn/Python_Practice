def exclude_em(num_seq, target=False):
    """
    >>> exclude_em([56, 57, 58, 59, 60], 57)
    [56, 59, 60]

    >>> exclude_em([43, 67, 456, 23, 878, 5, 65, 34], 456)
    [43, 67, 878, 5, 65, 34]

    >>> exclude_em([43, 67, 456, 23, 878, 5, 65, 34])
    [456, 23, 878, 5, 65, 34]
    
    :return: 
    """

    new_seq = []

    if target:                              # More succinct version of 'if target == True'

        position = num_seq.index(target)

        del num_seq[position:position+2]    # Stop location does not include start location in slices, hence '2'

    else:
        del num_seq[:2:]                    # Removes the first two elements of the list (mutation)
        # del num_seq[0:3]

    return num_seq


def double(factors_left, factors_right):
    """
    >>> double([43, 67, 456, 23, 878, 5, 65, 34], [2, 1, 1, 2, 2, 0, 0, 0])
    [86, 67, 456, 46, 1756, -1, -1, -1]
    
    :return: 
    """

    answers = []
    for left, right in zip(factors_left, factors_right):    # 'zip(factors_left, factors_right)' - treated as one object
        product = left * right

        if product == 0:
                insertoid = -1

        else:
            insertoid = product

            answers.append(insertoid)

    return answers


def punch_in(target, injecta, locus):
    """
    >>> punch_in([43, 67, 456, 23, 878, 5, 65, 34], [2, 1, 1, 2, 2, 0, 0, 0], 2)
    [43, 67, 2, 1, 1, 2, 2, 0, 0, 0, 456, 23, 878, 5, 65, 34]

    """

    injecta_backwards = injecta[::-1]
    for elem in injecta_backwards:
        target.insert(2, elem)

    return target

