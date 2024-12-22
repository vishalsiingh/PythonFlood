#parent class ko refer krrta h 
# child to parent classs
class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id

class Programmer(Employee):
  def __init__(self, name, id, lang):
    # self.name = name
    # self.id = id
    super().__init__( name, id)
    self.lang = lang

rohan = Employee("Rohan Das", "420")
vishal = Programmer("vishal", "2345", "Python")
print(vishal.name)
print(vishal.id)
print(vishal.lang)