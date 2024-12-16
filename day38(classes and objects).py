class person:
    name="Vishal"
    roll=3215
    cgpa=9.0
    def info(self):
        print(f"{self.name} have {self.cgpa}")
a=person() #objects h 
b=person()
a.name="Kashyap"
a.cgpa=9.01
# print(a.name)
b.name="ALien"
b.cgpa=8
a.info() # method call kra rhe h 
b.info()