class person :
    def __init__(self,name,age):
        self.name=name
        self.age=age
      
    def showname(self):
        print("name=",self.name)
    def showage(self):
        print("age=",self.age)
class student(person):
    def __init__(self,rollno,schoolname):
        self.rollno=rollno
        self.schoolname=schoolname
        person.__init__(self,"ravindra",18)
    def showrollno(self):
        print("rollno=",self.rollno)
    def showschoolname(self):
        print("schoolname=",self.schoolname)

s1=student("sbm inter college",24)
s1.showrollno()
s1.showschoolname()
s1.showname()
s1.showage()
