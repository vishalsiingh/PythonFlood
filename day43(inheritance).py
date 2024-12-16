class Employee:
    def __init__(self,name,id):
        self.name="name"
        self.id=id

    def show(self):
        print(f"The employee having {self.id} is {self.name}")
    
class  programmer(Employee):
        def showlang(self):
         print("h=my fav lang is Python")


e=Employee("vishal",420)
e=programmer ("vishal",420)
e.show()    
e.showlang()