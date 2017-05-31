"""
This is a menu for accessing a user's account. Logic is located in account.py
"""

from account import Account
import pychalk


acct = Account             # pep484 annotations

USER_ACCOUNTS = dict()    # Refactor this. If it stays global, UPPERCASE!


def user_menu(account):
    """
    Displays a menu of user options and initiates operations.
    :return: 
    """
    user_opts = {'1': 'Get balance', '2': 'Make a withdrawal', '3': 'Make a deposit', '4': 'Interest rate report'}
    for key, value in user_opts.items():
        print(key, ' ⟹ ', value, sep='\n')

    selection = input('Please make a selection: ')

    if selection == '1':
        try:
            balance = user_accounts['llama']
        except KeyError:
            print('Insufficient funds')
            user_menu()

    elif selection == '2':
        try:
            account.withdraw()
            #balance = user_accounts['llama']
        except KeyError:
            print('Insufficient funds')
            user_menu()


def make_account() -> acct:
    new_ident = input('Please enter a unique identifier for your account name: ')

    account = Account(new_ident)
    return account


def retrieval():
    pass


def login_menu() -> str:
    """
    Displays a welcome menu with login and new account options.
    :return: 
    """
    welcome_opts = {'1': 'Access your account', '2': 'Open a new account'}
    for key, value in welcome_opts.items():
        print(key, ' ⟹ ', value, sep='\n')
    selection = input('>>> ')

    if selection == '1':
        ident = input('Please enter your account name: ')
        if ident in USER_ACCOUNTS:
            account = Account(ident)
            user_menu(account)
        else:
            print('Account not found.')
            login_menu()


    elif welcome_opt == '2':
        account = make_account()
        print(f'The account {account.ident} has been created.')
        user_menu(account)

    else:                                                            # A while loop can also be used for error handling
        print('Invalid. Please enter an option from the menu below. ')
        return login_menu()                                          # Take care to return this if the call is terminal.


def ようこそ():
    welcome_prompt = '''
                     Welcome to the BankBuddy 2600® - "Keeping it safe. Keeping it secret.™"
                     Chernobog Industries, Inc.
                     Providing powerful and secure solutions for the financial industry since 2017.

                     Please select an option from the menu.
                     '''

    print(welcome_prompt)

    return login_menu()


ようこそ()
    
    
    
    
    
    
    

    




