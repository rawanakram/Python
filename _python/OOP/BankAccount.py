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


Omar = BankAccount(0.01, 2000)
Emy = BankAccount(0.01, 1200)

#To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info  
Omar.deposit(1000).deposit(800).deposit(120).withdraw(1200).yield_interest().display_account_info()

#To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info
Emy.deposit(800).deposit(900).withdraw(120).withdraw(1000).withdraw(200).withdraw(150).yield_interest().display_account_info()
