

def backwards(chiral):
    """
    Given an input list, return it in reverse.
    
    >>> backwards([56, 57, 58, 59, 60])
    [60, 59, 58, 57, 56]
    
    :return: 
    """

    chiral.reverse()
    return chiral


def maximus(sequence):
    """
    
    Find the max number in a given list.  Then, change every element in the list containing the first number of the maximum to the maximum number.
    >>> maximus([56, 57, 58, 59, 60])
    [60, 57, 58, 59, 60]

    >>> maximus([56, 67, 56, 59, 60])
    [67, 67, 67, 59, 67]
    
    :return: 
    """

    biggest = max(sequence)
    first_num = str(biggest)[0]
    embiggened = []

    for elem in sequence:
        if first_num in str(elem):
            intron = biggest  # Two instances of the same method is 'wet'. So...
        else:
            intron = elem  # ...this functions like a 'router'

        embiggened.append(intron)

    result = embiggened

    return result



def compare_first_element(sequence_a, sequence_b):
    """
    
    Given two lists, return True if the first two items are equal.
    >>> compare_first_element(['migratory', 'birds', 'fly', 'south'], ['migratory', 'monopoloy', 'mind'])
    True
    
    :return: 
    """

    if sequence_a[0] == sequence_b[0]:              #Ternary operation works well here.
        return True                                 #E.g. return True if sequence_a[0] == sequence_b[0] else False
    else:
        return False


def compare_second_letter(sequence_a, sequence_b):
    """
    
    Return True if the first letter of the second element in each list is equal. (Case Insensitive) (you can use .startswith()
    >>> compare_second_letter(['migratory', 'penguins', 'fly', 'south'], ['One', 'Pound', 'Coconut'])
    True

    >>> compare_second_letter(['migratory', 'birds', 'fly', 'south'], ['One', 'Pound', 'Coconut'])
    False
    
    :return: 
    """

    letter_a = sequence_a[1][0].lower()
    letter_b = sequence_b[1][0].lower()

    if letter_a == letter_b:
        return True
    else:
        return False


def smoosh(sequence_mama, sequence_baba, reverse=False):
    """
    
    Given two lists, return one list, with all of the items of the first list, then the second ('Extending')
    >>> smoosh(['mama', 'llama'], ['baba', 'yaga'])
    ['mama', 'llama', 'baba', 'yaga']


    Use a default argument to allow the user to reverse the order!
    >>> smoosh(['mama', 'llama'], ['baba', 'yaga'], reverse=True)
    ['yaga', 'baba', 'llama', 'mama']
    
    :return: 
    """

    smooshed = sequence_mama + sequence_baba
    if reverse:
        smooshed.reverse()

    print(smooshed)
