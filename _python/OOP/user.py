class User:
    def __init__ (self,name,email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self,amount):
        self.account_balance+=amount
    
    def make_withdrawal(self, amount):
        self.account_balance-=amount

    def display_user_balance(self):
        print("User:",self.name,", Balance:",self.account_balance,"$")

    def transfer_money(self, second_account, amount):
        self.make_withdrawal(amount)
        second_account.make_deposit(amount)

    
#Create 3 instances of the User class
Ahmad = User("Ahmad Taha", "ahmad@python.com")
Omar = User("Omar Khaleel", "omar@python.com")
Emy = User("Emy Mike", "emy@python.com")

#the first user make 3 deposits and 1 withdrawal and then display their balance
Ahmad.make_deposit(100)
Ahmad.make_deposit(150)
Ahmad.make_deposit(50)
Ahmad.make_withdrawal(170)
Ahmad.display_user_balance()

# the second user make 2 deposits and 2 withdrawals and then display their balance
Omar.make_deposit(1000)
Omar.make_deposit(800)
Omar.make_withdrawal(120)
Omar.make_withdrawal(200)
Omar.display_user_balance()

#he third user make 1 deposits and 3 withdrawals and then display their balance
Emy.make_deposit(1200)
Emy.make_withdrawal(100)
Emy.make_withdrawal(250)
Emy.make_withdrawal(120)
Emy.display_user_balance()

#have the first user transfer money to the third user and then print both users' balances
Ahmad.transfer_money(Emy,100)
Ahmad.display_user_balance()
Emy.display_user_balance()