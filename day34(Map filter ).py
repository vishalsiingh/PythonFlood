
#MAP higher order function
# def cube(x):
#     return x*x*x
# print(cube(2))

l=[1,2,3,4,5]
newl=[]
# for item in l:
#     newl.append(cube(item))
# newl=list(map(cube,l)) # this is why map is used
newl=list(map(lambda x:x*x*x,l)) # this is why map is used
print(newl)

#FILTER higher order function

def filter_fun(a):
    return a>2
newnewl= list(filter(filter_fun,l))
print(newnewl)






9
