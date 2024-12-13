#LAMBDA is anonymous function 
# def double(x):
#     return x*2
double=lambda x:x*2  
print(double(5))

# def cube(x):
#     return x*x*x
cube=lambda x:x*x*x
print(cube(4))

avg=lambda x,y:(x+y)/2
print(avg(4,5))

def appl(fx,value):
    return 6 +fx(value)
print(appl(cube,2))
print(appl(lambda x:x*x*x,2))
print(appl(lambda x:x*x,2))
