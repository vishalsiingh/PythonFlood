# a=int(input("Enter the age: "))
# if(a>18):
#     print("You can drive")
# else:
#     print("you cannot drive")  #the space before print is the indentataion 
      
# print("Wowwww this line always prints as it is not in loop")


num = int(input("Enter the value of num: "))
if (num < 0):
  print("Number is negative.")
elif (num == 0):
  print("Number is Zero.")
elif (num == 999):
  print("Number is Special.")
else:
  print("Number is positive.")

print("I am happy now")


num = int(input("enter the number:"))
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")