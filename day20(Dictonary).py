dic={
    "Vishal": "A good boy",
    "Raju":"A bad boy",
}
print(dic["Vishal"])

dic={
    12:"Vishal",
    34:"Robin",
    879:"Anvi",'Pass':True
}
print(dic[879])
print(dic.get(1234)) # if not found not guve error it returns none 
print(dic.keys()) #isse key milega 
print(dic.values()) # isse values milega
for keys in dic.keys():
    print(dic.keys())
 
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())
for key, value in info.items():
  print(f"The value corresponding to the key {key} is {value}") 