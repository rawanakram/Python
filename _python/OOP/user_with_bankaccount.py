class BankAccount:
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
	
    def deposit(self, amount):
        self.balance+=amount
        return self

    def withdraw(self, amount):
        self.balance-=amount
        return self

    def display_account_info(self):
        print("Balance:",self.balance,"$")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
        return self

class User:
    def __init__ (self,name,email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"User:{self.name} Balance:{self.account.balance}$")
        return self

Omar = User("Omar Khaleel", "omar@python.com")
Emy = User("Emy Mike", "emy@python.com")

Omar.make_deposit(100).make_deposit(150).make_deposit(50).make_withdrawal(170).display_user_balance()