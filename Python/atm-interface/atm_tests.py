import unittest
from account import Account


class TestAccountCreation(unittest.TestCase):
    def setUp(self):
        self.test_c_account = Account(balance=270, account_type='chequing', ident='Alice')
        self.test_s_account = Account(balance=10454, account_type='savings', ident='Bob')

    def test_initial_chequing_account_open(self):
        self.assertNotEqual(self.test_c_account._balance, 210)
        self.assertEqual(self.test_c_account.account_type, 'chequing')

    def test_initial_savings_account_open(self):
        self.assertEqual(self.test_s_account._balance, 10454)
        self.assertEqual(self.test_s_account.account_type, 'savings')

    def test_account_creation_from_csv_string(self):
        record = 'ident,151.5,chequing'
        test_account = Account.from_csv_string(record)
        self.assertEqual(test_account._balance, 151.50)
        self.assertEqual(test_account.account_type, 'chequing')


class TestAccountOperations(TestAccountCreation):

    def test_get_balance(self):
        ident = 'Alice'
        test_account = Account(500, 'chequing', ident)
        self.assertEqual(test_account.get_funds(), 500)
        test_account.withdraw(250)
        self.assertEqual(test_account.get_funds(), 250)

    def test_valid_withdrawal_in_good_standing(self):
        self.assertEqual(self.test_s_account.withdraw(100), 10354)

    def test_overdraw_error(self):
        with self.assertRaises(ValueError):
            self.test_c_account.withdraw(999999999)

    def test_deposit(self):
        self.assertEqual(self.test_c_account.deposit(100), 370)

    def test_simple_interest(self):
        pass

    def test_check_withdrawal_bool(self):
        self.assertFalse(self.test_c_account.check_withdrawal(999999999))

    def test_get_standing_bool(self):
        self.assertFalse(self.test_c_account.get_standing())
        self.assertTrue(self.test_s_account.get_standing())

'''
class TestATMInterface(TestAccountCreation):
    pass
'''
