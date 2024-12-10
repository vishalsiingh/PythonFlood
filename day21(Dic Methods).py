ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}

# ep1.update(ep2)    isse ep1 jo hoga update kr lega ep2 ke datta ko 
# # ep1.clear()
# ep1.pop(122)
ep1.popitem() # isse last wla item khud hat jayega no need to mention 
del ep1[122] # us specific value ko remobe kr dega 
print(ep1) 

#print empty dic
emp={}
print(emp)