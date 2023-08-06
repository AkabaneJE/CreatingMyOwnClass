class BankAccount:
    def __init__(self,id,balance,company):
        self.id = id
        self.company = company
        self.balance = balance

    def withdraw(self,amount):
        if(amount > self.balance):
            print("Insuffient balance")
        else:
            self.balance -= amount
            print(f"You have withdraw {amount}.\nBalance left: {self.balance}")
    def deposit(self,amount):
        self.balance += amount
        print(f"You have deposited {amount}.\nBalance now: {self.balance}")
    def transfer(self,amount,payee_account):
        self.balance -= amount
        payee_account.balance += amount
        print(f"Transferred {amount} to {payee_account.company}. Account Balance : {self.balance}")
# my_account = BankAccount(213,1500,"DBS")
# my_account.withdraw(2500)
# my_account.deposit(2500)


my_account = BankAccount(id="12345", balance=300, company="OCBC")
my_2nd_account = BankAccount(id="23451", balance=500, company="DBS")
my_account.transfer(200,my_2nd_account)
