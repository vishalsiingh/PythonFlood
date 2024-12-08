#Good morning message

import time
 
timestamp=time.strftime('%H:%M:%S')
print(timestamp)   
timestamp1=int(time.strftime('%H'))
print(timestamp1)
if  timestamp1 <12:
    print("Good mornings python")
else:
    print("mornings ends")    
