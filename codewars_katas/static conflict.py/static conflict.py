class base:
    x=12
    def __init__(self):
        base.x=20
        self.a=10
    def showbase(self):
        print("base a=",self.a)
class derived(base):
    x=11
    def __init__(self):
        self.a=20
        super().__init__()
    def show():
        print(derived.x,base.x)
    def showderived(self):
        print("derived a=",self.a)
obj=derived()
print(derived.x)
derived.show()