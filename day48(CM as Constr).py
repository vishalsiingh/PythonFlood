# Class method ko as a constructor kasie use kr skte h 
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def fromStr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])
e=Employee("Rohit",50000)       
print(e.name)
print(e.salary) 
# if agar data string ke form me diya hoga then 
string="Vishal-12000"
# we use split(" ")[] to get 
# e2=Employee(string.split("-")[0],string.split("-")[1])
# print(e2.name)
# print(e2.salary)
e2=Employee.fromStr(string)
print(e2.name)
print(e2.salary)