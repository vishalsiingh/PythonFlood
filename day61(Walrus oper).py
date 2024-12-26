# Walrus Opertaor(:=)
# introduced in pyyhton 3.8
# assigns values to variables as part of a larger expression
# assignment opertaors aka walrus opertaor
# a=True
# print(a:=False)

numbers=[1,2,3,4,5]
while(n:=len(numbers)>0):
    print(numbers.pop())

happy=True
print(happy)
print(happy:=True)

foods=list()
while True:
    food=input("Enter a food:")
    if food=="quit":
        break   
    foods.append(food)


#walrus
food=list()
while (food:=input("Enter a food:"))!='quit':
    food.append(food)

    