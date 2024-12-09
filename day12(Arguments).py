# Default Arguments 
# Keyword Arguments
# Variable length Arguments
# Required Arguments

# def Average(a,b):
#     print("Avergae of two numbers",(a+b)/2)
# Average(2,5)  

def average(*numbers):
  # print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
  # print("Average is: ", sum / len(numbers))
  # return 7
  return sum / len(numbers)


# average(4, 6)
# average(b=9)

c = average(5, 6, 7, 1)
print(c)