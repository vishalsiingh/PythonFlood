#FINAL keyword ke andar jo rahega wo print hoga hi hoga chahe error aaye ya nhi 
def fun():
 try:
  l=[1,4,6,7]
  i= int (input("enter the index:"))
  print(l[i])
 except:
  print("some error occured")
 finally:
  print("Always gives the result always print")
  
 x=fun()
 print(x)