class text:
    def f1(self):
        self.name=input("enter the name")
        self.age=int(input("enter the age"))
        self.sex=input("enter the sex")
    def f2(self):
        print("name",  self.name)
        print("age",   self.name)
        print("sex",   self.sex)
s1=text()
s1.f1()
s1.f2()
