class User:
    def __init__(self, name, amount = 0):
        self.name = name
        self.bal = amount
    def make_deposit(self, amount):
        self.bal += amount
        return self
    def display_user_balance(self):
        print(self.name, self.bal)
        return self
    def make_withdrawal(self, amount):
        self.bal -= amount
        return self
    def transfer_money(self, other_user, amount):
        self.bal -= amount
        other_user.bal += amount
        return self

Revel, O, P = User("Revel"), User("O"), User("P")

Revel.make_deposit(10).make_deposit(10).make_deposit(10).make_withdrawal(15).display_user_balance()

O.make_deposit(50).make_deposit(50).make_withdrawal(20).make_withdrawal(20).display_user_balance()

P.make_deposit(1000).make_withdrawal(50).make_withdrawal(20).make_withdrawal(20).display_user_balance()

Revel.transfer_money(P, 10).display_user_balance()
P.display_user_balance()