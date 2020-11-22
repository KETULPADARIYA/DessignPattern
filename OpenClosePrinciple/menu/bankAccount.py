import locale


class BankAccount():

    def __init__(self,balance=0):
        self.balance = balance
        self.account = None

    def add_money(self,amount):
        """
        Add money to a Bank account
        :param amount: A numerical Value by which the bank account's balance will increase
        :type amount: int
        """
        self.balance += float(amount)


    def withdraw_money(self,amount):
        """
            withdraw money to a bank account
        :param amount: A numerical value by which the bank account's balance will decrease
        """
        self.amount -= float(amount)


    def show_balance(self):
        """ Show formatted balance"""
        locale.setlocale(locale.LC_ALL,"")

        return locale.currency(self.balance,grouping=True)