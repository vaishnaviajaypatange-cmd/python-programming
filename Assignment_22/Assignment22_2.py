class Circle:
    PI = 3.14

    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0

    def Accept(self):
        self.radius = float(input("enter radius : "))



    def CalculateArea(self):
        
        self.area =  self.PI * self.radius * self.radius


    def CalculateCircumference(self):
        self.circumference = 2 * self.PI * self.radius



    def Display(self):
        print("Radius : ",self.radius)
        print("Area : ",self.area)
        print("Circumference : ",self.circumference)

obj = Circle()
obj.Accept()
obj.CalculateArea()
obj.CalculateCircumference()
obj.Display()








        

    
        
