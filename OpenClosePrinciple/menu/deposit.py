import os


class ManuItem:

    def __init__(self, prompt, action):
        self.prompt = prompt
        self.action = action


class Deposite:
    def __init__(self, account):
        self.account = account

    def __call__(self):
        amount = input("How much? ")
        self.account.add_money(amount)


class ShowBalance:

    def __init__(self, account):
        self.account = account

    def __call__(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("\n Your balance is: {}".format(self.account.show_balance()))
        input(">> Press enter to continue <<")


class Withdraw:

    def __init__(self, account):
        self.account = account

    def __call__(self):
        amount = input("How much? ")
        self.account.withdraw_money(amount)
