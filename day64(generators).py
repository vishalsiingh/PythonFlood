# ye lsit type ka rehta h but list
# me pehle se values insert hota h but
# genertaor me usse samay generate hota h 
# it is the powerful tool for working with  large or complex data set

# value ke banane ke  samagri store hota h  na ki values 

def my_generator():
 for i in range(500):
     #complex computations 
     yield i #values on the fly gemeertae ho rha h 
gen=my_generator()
print(next(gen)) #values genertae hote jayega
print(next(gen))
print(next(gen))

for j in gen: # sequence me hote jayga 
    print(j)    