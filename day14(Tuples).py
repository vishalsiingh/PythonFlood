#orderd coll of data items stoes multiple items  single varibles
# and tuples can not be chaged as lissts
#not in square brackets onlly in ()
tup=(4,6,7,"Vishal","danger") #class tuple h 
print(type(tup),tup)
print(len(tup))
print(tup[0])
print(tup[1])
print(tup[2]) # -ve indexing same comcept hota h lists me dekh chuke h 
print(tup[4])

if 3 in tup:  # ye check Karega ki wo value hai ya nai tup me 
    print("Yes")
else:
    print("No")    
tup=(1) # class int h n a ki tuple  isiliye (1,) ke ke karenge to retun tuple karega 
print(type(tup),tup)

tup=(1,)
print(type(tup),tup)
# usse ek naya tuple create ho ke print hoga ek naya tuple .
tup2=tup[1:4]
print(tup2)


#OPERATUONS ON TUPLES
#Manipulation on tuples
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)
#concatenate
countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

#count
tup=(1,4,6,7,9,4)
res=tup.count(4)
print(res)

#index
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple.index(3)
print('First occurrence of 3 is', res)