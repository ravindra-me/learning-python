class base:
    def __init__(self):
        self.a=10
    def showbase(self):
        print("base a=",self.a)
class derived(base):
    def __init__(self):
        self.a=20
        super().__init__()
    def showderived(self):
        print("derived a=",self.a)
obj=derived()
obj.showbase()
obj.showderived()
