# basically ye help krta objects ko banane me 
class person():
    # name="Vishal"
    # roll=3215
    # cgpa=9.0
    def __init__(self,Name,roll):  #constructor baabne ka tarika 
        print("i m lazy coder")
        self.name="Name"
        self.roll="roll"

    def info(self):
        print(f"{self.name} have {self.roll}")
a=person("Vishal",9.0) #objects h 
b=person("alien",9.5)
a.info()
b.info()