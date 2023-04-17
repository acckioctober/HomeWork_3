class Savings_account():
    def __init__(self, name):
        self.name = name

class Checking_account():
    def __init__(self, age):
        super().__init__()
        self.age = age

class Bank_account():
    ID = 0
    def __init__(self):
        super().__init__()
        Bank_account.ID += 1
        self.id = Bank_account.ID
    def set_account (self):
        print(f'Номер счета № {self.id}')

class Real_estate():
    def __init__(self):
        super().__init__()
    def hello(self):
        print(f'Hello!')

class Insurance(Savings_account, Checking_account, Bank_account, Real_estate):
    def __init__(self, name, age):
        Savings_account.__init__(self, name)
        Checking_account.__init__(self, age)
        # super().__init__()
        self.__age = age
        self.__name = name
    @property
    def get_age(self):
        return self.__age
    @get_age.setter
    def get_age(self, age):
        self.__age = age
    @property
    def get_name(self):
        return self.__name
    @get_name.setter
    def get_name(self, name):
        self.__name = name

    def __str__(self):
        return f'{self.__name} {self.__age}'

ins = Insurance('qwe', 44)

ins.get_age = 55
ins.get_name = 'astra'

print(ins)
ins.set_account()
ins.hello()
