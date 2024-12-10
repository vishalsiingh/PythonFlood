 # entering quit does not give error else error 

a=input("Enter the string of 4 char:")
print(a)
if a != "quiz":
    raise ValueError("The string is invalid")