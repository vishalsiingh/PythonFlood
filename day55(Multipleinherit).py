#ek se jayda class mila ke ek class banaya jata h =multiple inheritance

class Employee:
    def __init__(self, name):
        self.name = name   
    def show(self):
        print(f"the name is {self.name}")


class Dancer:
    def __init__(self, dance):
        self.dance = dance
    def show(self):
        print(f"the dance is {self.dance}")

class EmployeeDancer(Dancer,Employee):
    def __init__(self, name,dance):
        self.dance = dance
        self.name = name

o= EmployeeDancer("Vishal","Kathak")
print(o.name)
print(o.dance)
o.show()
print(EmployeeDancer.mro()) #mro-Method Resolution Order

