"""
Create a class named `Account` in a module named `account`.
It must have *private* attributes for the balance and interest rate.
Prefix an underscore to any private attributes.
A newly-instantiated account will have zero balance and an interest rate of 0.1%.

Write class methods in the account class that:

* `get_funds()` Return account balance
* `deposit(amount)` Deposit to the account
* `check_withdrawal(amount)` Return `True` if large enough balance for a withdrawal
* `withdraw(amount)` Withdraw an allowed amount; raise a `ValueError` if insufficient balance
* `calc_interest()` Calculate and return interest on the current account balance

An exercise by D-Force.
"""


class Account:
    """
    
    
    """
    
    def __init__(self, balance: int, account_type: str, ident: str):
        self._balance = balance
        self._interest = 0.001
        self.ident = ident
        self.account_type = account_type
    
    def __repr__(self):
        message = f'{self.__class__.__name__}({self.name}, {self._balance}, {self._interest}, {self.ident})'
        return message

    def __str__(self):
        print(f'{self.__class__.__name__}({self.name}, {self._balance}, {self._interest}, {self.ident})')
        
    def get_funds(self) -> int:
        """
        Return account balance
        :return: 
        """
        return self._balance

    def get_standing(self) -> bool:
        """
    
        :return: 
        """
        if self._balance >= 1000:
           return True
        else:
            return False
    
    def check_withdrawal(self, amount):
        """
        Return `True` if large enough balance for a withdrawal
        :param amount: 
        :return: 
        """

    def deposit(self, amount: int) -> int:
        """
        Deposit to the account
        :param amount: 
        :return: 
        """
        self._balance += amount
        return self._balance
    
    def withdraw(self, amount):
        """
        Withdraw an allowed amount; raise a `ValueError` if insufficient balance
        :param amount: 
        :return: 
        """
        if self._balance - amount >= 0:
            self._balance -= amount

        else:
            raise ValueError('Nuh uh uh. No money for you!')

        return self._balance

    def calc_interest(self, amount):
        """
        Calculate and return interest on the current account balance
        :param amount: 
        :return: 
        """

    @classmethod                             # Class methods take their class as their first argument.
    def from_csv_string(cls, csv_string):    #'@' is a decorator token, modifies the decorated function.
        ident, balance, account_type = csv_string.split(',')
        record = cls(ident=ident, balance=float(balance), account_type=account_type) # Formal kw parameters
        return record


    
    