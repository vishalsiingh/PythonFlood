class Employee:
    company="Linit "  #ye claSSS se associated hai  # ye class variable h  
    noofemplyee=0
    def __init__(self,name):
        self.name=name
        self.income=2.0   # instance se relsted h 
        Employee.noofemplyee+=1 
    def showdetails(self):
        print(f"the name of the employee is {self.name} of  sized {self.noofemplyee} of {self.company},his salary is {self.income}")
emp1=Employee("vishal")
emp1.income=50 # ye jo h insatnce se related h 
emp1.company="Blinkit"
emp1.showdetails()
Employee.company="blinkeee"
print(Employee.company)
emp2=Employee("Vipul")
emp2.company="happy"
emp2.showdetails()
