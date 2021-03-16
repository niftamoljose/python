class account:
    def __init__(self):
        self.balance=0
        print ("balance is zero")
    def deposit(self):
        amount = float(input("enter amount to be deposited"))
        self.balance +=amount
        print ("amount deposited is", amount)
    def withdraw(self):
      amount= float(input("enter amount to be withdraw"))
      if self.balance >= amount:
          self.balance -= amount
          print("you withdraw",amount)
      else:
          print("not enough balance")

    def display(self):
        print("remaining balance is", self.balance)
        print("account_no:1234567890 name:xyz account type: savings"  ,"balance: ", self.balance)
a=account()
a.deposit()
a.withdraw()
a.display()