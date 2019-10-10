class person :
    def __init__(self,name,age):
        self.name=name
        self.age=age
      
    def showdname(sellf):
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
    def showschoolname(self)
        print("schoolname=",self.schoolname)

s1=student(10,sbm inter college)
s1.rollno()
s1.schoolname()
s1.name()
s1.age()