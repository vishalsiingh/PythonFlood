import time
def usingWhile():
    i=0
    while i<50000:
        i=i+1
        print(i)

def usingFor():
    for i in range(50000):
        print(i)

init=time.time()
usingWhile()
t1=time.time()-init

init=time.time()
usingFor()

print(time.time()-init) #return the time in seconds
print(t1)

#time.sleep---

# print(4)
# time.sleep(3)
# print("this is printed after 3 seconds")


#strftime method---

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

print(formatted_time)
# Output: 2022-11-08 08:45:33
