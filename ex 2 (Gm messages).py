#Good morning message

import time
t=time.strftime('%H:%M:%S')
print(t)
Hour=int(time.strftime('%H'))
Hour=int(input("Enter the hour:"))
print(Hour)
if (Hour>=0 and Hour<12): 
    print("Good mornings python")
elif(Hour>=12 and Hour<17):
    print("Good Afternoon sir!") 
elif(Hour>=17 and Hour<0):
    print("Good Night")   


