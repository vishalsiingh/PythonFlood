a = None
b = None

print(a is b) # exact location of object in memory
print(a is None) # exact location of object in memory
print(a == b) # value

a = [1,3,4]
b = [1,3,4]
print(a is b) #ye uska exact location deta h  memory me 
print(a == b) #ye value ko check krta h 


a=(1,2,3)
b=(1,2,3)
print(a is b)   # ye dono true diye kiuki tuple h immutable h isiliye dono true return karegnge
print(a ==b)