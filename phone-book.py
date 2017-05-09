"""
Kieran R Prasch

Phonebook Example Solution


def phonebook():

    phonebook = dict()    # Empty dict {}

    cmd = None
    while cmd != 'quit':
        print('Command? list or add or get or quit')
        cmd = input()
        if cmd == 'list':
            for name in phonebook:
                print(name)
        elif cmd == 'add':
            print('Name?')
            name = input()
            print('Phone number?')
            number = input()
            phonebook[name] = number
        elif cmd == 'get':
            print('Name?')
            name = input()
            number = phonebook.get(name, 'no entry')
            print(name + ' -- ' + number)
        else:
            print('Unknown command: ' + cmd)

phonebook()

"""

"""
This is Doby's effort to create a registry of contacts.
Use .update() to add multiple elements to a dict at the same time.
E.g. update_data = {'bullfrog': ('loud', 'obnoxious'), axolotl: ('cute', 'gilly')}
amphibians.update(update_data)

Use .items() to return both keys *and* values. Good for 'R' operations.
"""

import chalk

contacts = dict()


def create_proc(forname, surname, phone, email):
    contacts = [{'name': (surname, forename),
                 'telephone': phone,
                 'e-mail': email}]


def return_proc(return_hest):
    contacts.get('entities', 'Alas, contact not found. Try again?')


def hest_proc(command):
    """
    Processes the brooker's hest.
    """

    if len(hest) > 1:
        print('Not a command. Please input a single letter command.')

    elif hest not in 'crudl':
        print('Not a command. Acceptable commands are: \'c\', \'r\', \'u\', \'d\', \'l\'.')

    elif hest == 'c':
        forename = input('Enter forename: ')
        surname = input('Enter surname: ')
        phone = input('Enter telephone number: ')
        email = input('Enter e-mail address: ')
        create_proc(forename, surname, phone, email)

    elif hest == 'r':
        return_hest = input('Enter name of contact: ')
        return_proc(return_hest)

    elif hest == 'u':
        update_hest = input('Enter name of contact to update: ')
        update_proc(update_hest)

    elif hest == 'd':
        delete_hest = input('Enter name of contact to delete: ')
        delete_proc(delete_hest)

    elif hest == 'l':
        list_proc(list_hest)


def gather():
    """
    Gathers the brooker's hest.
    """

    # underline solution goes here

    hest = input(' Hello D-Force. What is your bidding?\n'
                 '(\'C\'reate contact, \'R\'etrieve contact, \'U\'pdate contact, \'D\'elete contact, \'L\'ist contacts)\n'
                 'C.R.U.D.L.').lower()

    hest_proc(hest)


gather()




