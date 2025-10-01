class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created. \nBalance: = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance: ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\nDeposit Complete.")
        self.getBalance()      
    
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nInsufficient funds in account, '{self.name}' only has ${self.balance:.2f} available.")
    
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print(f"\nWithdrawal Complete.")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw Failed: {error}')

    def transfer(self, amount, account):
        try: 
            print('\n**********\n\nBeggining Transfer...')     
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(f"\nTransfer Complete.\n\n**********")       
        except BalanceException as error:
            print(f'\nTransfer Failed: {error}\n\n**********')

class InterestRewardsAccount(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print(f"\nDeposit Complete with Interest Rewards!")
        self.getBalance()

class savingsAccount(InterestRewardsAccount):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 2.00
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print('\nWithdrawal Complete with $2.00 fee.')
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw Failed: {error}')
            
        