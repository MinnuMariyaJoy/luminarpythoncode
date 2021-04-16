#account creation
#deposit
#withdrawal

class Bank():
    bname="sbi"
    def accountcreat(self,acno,name):
        self.name=name
        self.acno=acno
        self.minimumbal=5000
        self.balances=self.minimumbal

    def deposit(self,amnt):
        self.balances+=amnt
        print("your",Bank.bname," account has been credited with ",amnt)
        print("your account balance is ",self.balances)

    def withdraw(self,amnt):
        if amnt>self.balances:
            print("insuffeint balance")
        else:
            print("account debited with ",amnt)
            self.balances -= amnt
            print("available balance is, ",self.balances)
obj=Bank()
obj.accountcreat(1234,"Minnu")
obj.deposit(10000)
obj.withdraw(2000)

#instance variables.....using self, related to objects
#static variables
            