# child class ke andar jo parent class ka method 
# aaya usmo change krna

class Shape:
    def __init__(self,x,y):
        self.x= x
        self.y=y

    def area(self):
        return self.x*self.y

class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius
        super().__init__(radius,radius)

    def area(self):
        return 3.14*super().area()
# sq=Shape(5,5)
# print(sq.area())
# rec=Shape(5,5)
# print(rec.area())
c=Circle(5)
print(c.area())