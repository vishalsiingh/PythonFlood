marks=[10,23,27,98,100]

# index=0
# for mark in marks:
#     print(mark)

#     if(index==3):
#         print("Vishal is a Avg student")
#         index+=1      

#enumerate use in for
for index, mark in enumerate(marks,start=1): #start=1 mtlb ki we decide where to start basically ye uska  indexing
    print(mark)
    print(index,marks)

    if(index==3):
        print("Vishal is a Avg student")
               #lists
marks=[10,23,27,98,100]
for  index,mark in enumerate(marks):
    print(index,marks)
# Loop over a tuple and print the index and value of each element
colors = ('red', 'green', 'blue')
for index, color in enumerate(colors):       #      for  color in colours:
    print(index, color)
# And here's an example with a string:

# Loop over a string and print the index and value of each character
s = 'hello'
for index, c in enumerate(s):
    print(index, c)

fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(f'{index+1}: {fruit}')
# The enumerate function is often used when you need to loop over a sequence and
# perform some action with both the index and value of each element. For example-
#  you might use it to loop over a list of strings and print the index and 
#  value of each string 