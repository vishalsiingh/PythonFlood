# LISTS
l=[2,4,6,"Vishal","10Aug"]
print(l)
print(type(l))
print(l[3])
print(l[-2]) #this means ----- marks(l[len(l)-2])

#[:] mtlb [0:len(l)]
print(l[:])    # issee pura cheez print hoga isko STRING SLICING  bolte h and [[1:]] to 1 se shuru hoga nd n-1 tk jayega 
print(l[1:4:2]) # last wla JUMP WLA H  2 2 jump karega
if 0 in l:   #agar yhi pr "0" aise 0 ko likhenge to result no aayega coz wo int h na ki string
    print("yes present")
else:
    print("No absent")    

if "ug" in "10Aug":   #simpe if __in__: same chhez appply for string🚀
    print("Yes")
else:
    print("NO")   
    
#LIST COMPRESHENSION

lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==1]
print(lst)

#LIST METHOD
L=[23,45,87,32,0,65]
print(L)
L.append(98)
print(L)
L.sort()# defalut ascending orer me hoga
print(L)
L.sort(reverse=True) # desc me order me print kar dega
print(L)
L.reverse()
print(L) #reverse kr deta h 
print(L.index(65)) #index dega 
print(L.count(65)) #count karega 
m=l.copy() #m=l v kr skte the but we r beginners so use copy method as shown
m[0]=2
print(L)
L.insert(1,899) # ye us inderx pe ja ke wo valuve inset kr dega 
print(L)
m = [900, 1000, 1100] # koi aur m naam ka list h 
l.extend(m) # iska mtlb l ko kholo nd ye m  list ka vlaue enter kra do 


k=l+m #  naya list hi bna do do lsit ko concatenate kr ke       
print(k)