# inbuilt functionss

#dir
x=[1,2,3]
x=(1,2,3)
print(dir(x)) #ye returns all the attributes and methods
print(x.__add__)


#__dict__
class Person:
    def __init__(self,name,age):
        self.name=name
        self.salary=age
p=Person("john",35)
print(p.__dict__)

#help
print(help(Person))