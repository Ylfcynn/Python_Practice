

def backwards(chiral):
    """
    Given an input list, return it in reverse.
    
    >>> backwards([56, 57, 58, 59, 60])
    [60, 59, 58, 57, 56]
    
    :return: 
    """

    chiral.reverse()
    print(chiral)


def maximus(embiggen):
    """
    
    Find the max number in a given list.  Then, change every element in the list containing the first number of the maximum to the maximum number.
    >>> maximus([56, 57, 58, 59, 60])
    [60, 57, 58, 59, 60]

    >>> maximus([56, 67, 56, 59, 60])
    [67, 67, 67, 59, 67]
    
    :return: 
    """

    embiggen.


def compare_first_element(x):
    """
    
    Given two lists, return True if the first two items are equal.
    >>> compare_first_element(['migratory', 'birds', 'fly', 'south'], ['migratory', 'monopoloy', 'mind'])
    True
    
    :return: 
    """


def compare_second_letter(x):
    """
    
    Return True if the first letter of the second element in each list is equal. (Case Insensitive) (you can use .startswith()
    >>> compare_second_letter(['migratory', 'penguins', 'fly', 'south'], ['One', 'Pound', 'Coconut'])
    True

    >>> compare_second_letter(['migratory', 'birds', 'fly', 'south'], ['One', 'Pound', 'Coconut'])
    False
    
    :return: 
    """

def smoosh(x):
    """
    
    Given two lists, return one list, with all of the items of the first list, then the second ('Extending')
    >>> smoosh(['mama', 'llama'], ['baba', 'yaga'])
    ['mama', 'llama', 'baba', 'yaga']


    Use a default argument to allow the user to reverse the order!
    >>> smoosh(['mama', 'llama'], ['baba', 'yaga'], reverse = True)
    ['yaga', 'baba', 'llama', 'mama']
    
    :return: 
    """