
class Demo:
    Value = 0
    def __init__(self,no1,no2):
        self.Value1 = no1
        self.Value2 = no2

    def Fun(self):
        print("inside instance method fun",self.Value1,self.Value2)

    def Gun(self):
        print("inside instance method gun",self.Value1,self.Value2)

obj1 = Demo(11,21)
obj2 = Demo(51,101)

obj1.Fun()
obj2.Fun()

obj1.Gun()
obj2.Gun()
