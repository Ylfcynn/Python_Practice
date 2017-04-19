'''

# Practice: Pig Latin

Create a program asks for a _single_ English word and translates it to **Pig Latin**.
It prints out the input word and the resulting translation like the example below.

Rules:

1. If the first letter is a consonant, move it to the end.
1. Add "ay" to the end of that.
1. If the first letter is a vowel, just ad "yay" to the end.

> Word? hat
>
> hat in Pig Latin is athay
>
> Word? apple
>
> apple in Pig Latin is appleyay

## Advanced

Properly maintain the position of capitalization and punctuation.

> Word? Cat
>
> Cat in Pig Latin is Atcay
>
> Word? hat.
>
> hat. in Pig Latin is athay.

## Super Advanced

Handle words that start with multiple consonants by moving all of the consonants
 to the end.

> Word? string
>
> string in Pig Latin is ingstray

'''

'''

This version uses list methods to accomplish the task.


import string


def pigify(oink):
    oink.append('-')                                  # Appends a hyphen to the user input
    alphabet = list(string.ascii_letters)             # Casts the alphabet as a list
    first_letter = oink[0]

    for char in 'aeiouAEIOU':                         # For loop that removes all vowels from the list 'alphabet'
        alphabet.remove(char)

    consonants = alphabet

    if first_letter in consonants:                    # If first letter is in the list 'consonants'
        c_suffix = first_letter + 'ay'                # This is a creates the suffix for c-initial user input
        oink.remove(first_letter)
        oink.append(c_suffix)
        print(''.join(oink))

    else:
        v_suffix = 'yay'                              # This is the suffix for v-initial user input
        oink.append(v_suffix)                         # Appends the suffix 'yay' to the hyphenated user input
        print(''.join(oink))


def gather():
    oink = list(input('Ive-gay emay ayay ordway: '))  # Gathers user input

    pigify(oink)


gather()

'''

'''

The version below uses string methods to accomplish the task.

'''

'''

import string


def pigify(lexis):
    lexis_dash = lexis + '-'                       # Appends a hyphen to the user input
    first_letter = lexis_dash[0]
    alphabet = list(string.ascii_letters)          # Casts the alphabet as a list

    for vowels in 'aeiouAEIOU':                    # For loop that removes all vowels from the list 'alphabet'
        alphabet.remove(vowels)

    consonants = alphabet

    if first_letter in consonants:                 # If first letter is in the list 'consonants'
        c_suffix = first_letter + 'ay'             # This is a creates the suffix for c-initial user input
        trunk = lexis_dash[1:]
        c_oink = trunk.capitalize() + c_suffix     # Capitalizes initial letter and appends suffix '-ay'
        print(c_oink)

    else:
        v_oink = lexis_dash.capitalize() + 'yay'   # Capitalizes initial letter and appends suffix 'yay'
        print(v_oink)


def gather():
    lexis = input('Ive-gay emay ayay ordway: ')    # Gathers user input

    pigify(lexis)


gather()

'''
import string


def pigify(lexis):
    lexis_dash = lexis + '-'  # Appends a hyphen to the user input
    lexis_dash_list = list(lexis_dash)  # Casts the lexis_dash as a list

    alphabet = list(string.ascii_letters)  # Casts the alphabet as a list

    for vowels in 'aeiouAEIOU':  # For loop that removes all vowels from the list 'alphabet'
        alphabet.remove(vowels)

    consonants = alphabet

    # for letter in consonants:

    if lexis_dash_list[0] in consonants:

        while lexis_dash_list[0] in consonants:
            lexis_dash_list.append(lexis_dash_list[0])  # Removes initial onsonant
            lexis_dash_list.remove(lexis_dash_list[0])  # Removes initial onsonant


        lexis_dash = ''.join(lexis_dash_list)
        c_oink = lexis_dash.capitalize() + 'ay'  # Capitalizes initial letter and appends suffix 'ay'
        print(c_oink)

    else:
        lexis_dash = ''.join(lexis_dash_list)
        v_oink = lexis_dash.capitalize() + 'yay'  # Capitalizes initial letter and appends suffix 'yay'
        print(v_oink)


def gather():
    lexis = input('Ive-gay emay ayay ordway: ')  # Gathers user input

    pigify(lexis)


gather()