class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner      
        self.balance = balance  

    def deposit(self, amount):
        self.balance += amount               
        print("Balance now:", self.balance) #150 

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money!")
        else:
            self.balance -= amount
            print("Balance now:", self.balance)

acc = Account("Tomi", 100)   
acc.deposit(50)   
acc.withdraw(70)  
acc.withdraw(200) 
