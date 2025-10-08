class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

    def __hello(self):        # --> private method (__)
        print("hello person!")

    def welcome(self):
        self.__hello()

acc1 = Account("12345", "abcde")
acc1.reset_pass()
print(acc1.welcome())
# acc1.__hello
print(acc1.acc_no)
print(acc1.__acc_pass)
