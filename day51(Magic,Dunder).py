# purpose ki ye special kaam krte h (Random Methods)
class Employee:
    def __init__(self,name):
        self.name= name
        
    # name="Vishal"
    def __len__(self):
        i=0
        # return len(self.name)
        for c in self.name:
            i=i+1
        return i
    def __str__(self):
        return f" the name of the employee is {self.name} str"
    def __repr__(self):
        return f" Emplopyee'{self.name} '"
    def __call__(self):
        print("Hey i m good")


e=Employee("vishal")
# print(e.name)
# print(len(e)) #hmlog __len__ na kr ke direct len se call kie this is magic
# print(e)
print(str(e))
print(repr(e))
e()