class account:
    def detail(self):
        self.name=input("enter the name")
        self.accno=int(input("enter the account number"))
        self.balance=int(input("enter the balance"))
    def show (self):
        print("name" ,self.name)
        print("accounct number",self.accno)
        print("balanced",self.balance)
acc1=account()
acc1.detail()
acc1.show()
