class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account = acc


    # debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance = ", self.get_balance())

    # credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was crebited")
        print("total balance = ", self.get_balance())


    # show balance
    def get_balance(self):
        return self.balance

acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)