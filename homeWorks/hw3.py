'''step3'''
class Bank():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def moneyX(self):
        self.add_bal = float(input("Для пополнения счета введите сумму: "))
        self.balance += self.add_bal
        print(f'Bank("{self.name}", {self.balance})')

    def _kill(self):
        self.balance = 0
        print(f'Bank("{self.name}", {self.balance})')

    def __jackpot(self):
        self.balance *= 10
        print(f'Bank("{self.name}", {self.balance})')

    def _merge_balance(self, other):
        print(f'Bank("{self.name}", {self.balance + other.balance})')

b = Bank("Sergei", 100)
b1 = Bank("Beka", 200)

b.moneyX()
b._Bank__jackpot()
b1._merge_balance(b)
b._kill()