a=input("Enter a  number :")
print("multiplication of table {a} is :")
try:
 for i in range (1,11):
    print(f"{int(a)}*{i}={int(a)*i}")
except :
  print("Invalid input!")


print("some ipmp line")
print("End of the code")


try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
    
except IndexError:
  print("Index Error")