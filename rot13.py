"""
Write a function to decrypt an ROT13 Enconded message.

message = "Ohg, bssvpre, V qvqa'g pngpu gurfr -- gurl ner zl crg svfu naq V whfg\
 oevat gurz urer gb fjvz. Jura gurl'er qbar gurl whzc onpx vagb gur ohpxrg."

# Lab: ROT Cipher

###### Delivery Method: Prompt and Test Data

------------------------------

##### Goal

Write a program that decrypts a message encoded with ROT13 on each charachter starting with 'a', and displays it to the user in the terminal.

---------------------------------------------------------

##### Instructions

1. This is a puzzle!  Here is a chart to help with your translation:

| Index   | 0| 1| 2| 3| 4| 5| 6| 7| 8| 9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|
|---------|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
| English | a| b| c| d| e| f| g| h| i| j| k| l| m| n| o| p| q| r| s| t| u| v| w| x| y| z|
| ROT+13  | n| o| p| q| r| s| t| u| v| w| x| y| z| a| b| c| d| e| f| g| h| i| j| k| l| m|



-----------------

#### Advanced

1. Write the ROT Encrypter to go along with the decrypter, and allow encrypting of messages.
1. Allow the user to input the amount of rotation used in the encryption / decryption.

------------------

#### Key Concepts

- String Building Pattern
- `for` looping
- String Manipulation
- Function definition

"""

# Write your code below.


import string


def decrypter(garbled):
    degarbled = list()
    for char in garbled:
        if char in string.ascii_letters:
            true_char = ord(char) + 13
            if true_char > 90:
                true_char = ord(char) - 13
                degarbled.append(chr(true_char))
            else:
                degarbled.append(chr(true_char))
        else:
            degarbled.append(char)
    eureka = ''.join(degarbled)

    print(eureka)


def gather():
    garbled = list(input('Enter encrypted text: '))
    decrypter(garbled)


gather()

