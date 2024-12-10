#set methods
s1={1,5,8,9}
s2={4,1,2,9}
# print(s1.union(s2))
# s1.update(s2) #isse s1 ka value mtlb items update ho jayega 
# print(s1,s2)

print(s1.intersection(s2))
print(s1.symmetric_difference(s2)) # jo vlaues common nhu h wo print hoga 
print(s1.difference(s2))
print(s1.issuperset(s2))
print(s1.issubset(s2))
s1.add("Vishal")
print(s1)
s1.remove(8)
s1.discard(2)
#pop
I=s1.pop() #randomly pop the elements
print(I)
del s1 # delte the s1

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")
