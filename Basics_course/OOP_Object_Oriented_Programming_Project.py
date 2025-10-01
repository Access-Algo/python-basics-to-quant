from bank_accounts import * 

Dave = BankAccount(1000, "Dave")
John = BankAccount(2000, "John")

Dave.getBalance()
John.getBalance()   

John.deposit(500)
Dave.withdraw(200)

Dave.transfer(500000, John)
Dave.transfer(100, John)

Jim = InterestRewardsAccount(1000, "Jim")
Jim.getBalance()
Jim.deposit(100)
Jim.transfer(100, Dave)

Blaze = savingsAccount(1000, "Blaze")
Blaze.getBalance()
Blaze.deposit(100)
Blaze.transfer(1000, Jim)