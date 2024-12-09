letter=("My name is {} and i live in {}")
name="Vishal"
place="BBS"
print(letter.format(name,place)) # this is called string formatting 
#string.format(__,__)
#print(string name.format(_,_))
print(f"My name is {name} and i live in {place}") # f-strings  dono {}iska vlaue in ho ke print hoga
print(f"My name is {{name}} and i live in {{place}}") # f-strings but isme {{}} to smae as it is print ho jayega 


txt = ("For only {price:.2f} dollars!")
print(txt)
print(txt.format(price=89.0983438))

price=45.567
txt = (f"For only {price:.2f} dollars!")
print(txt)

print(f"{2*80}") #f-string
print(f"{2*6}")