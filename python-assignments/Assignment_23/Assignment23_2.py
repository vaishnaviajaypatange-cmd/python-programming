
class BankAccount:
    ROI = 10.5


    def __init__(self):
        self.name = input("enter name: ")
        self.amount = int(input("enter initial amount : "))

    def Display(self):
        print("Accont Holder name : ",self.name)
        print("Account Balance : ",self.amount)


    def Deposit(self):
        deposit = int(input("Enter deposit amount: "))
        self.amount = self.amount + deposit
        print("Balance after deposit:", self.amount)



    def Withdraw(self):
        withdraw = int(input("Enter withdraw amount: "))

        if withdraw <= self.amount:
            self.amount = self.amount - withdraw
            print("Balance after withdrawal:", self.amount)
        else:
            print("Insufficient balance. Current balance:", self.amount)



    def CalculateInterest(self):
        self.interest = (self.amount * self.ROI) / 100
        print("Interest amount : ",self.interest)


obj = BankAccount()
obj.Display()
obj.Deposit()
obj.Withdraw()
obj.CalculateInterest()





