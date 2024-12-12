#READING A FILE

# f = open('myfile.txt','r') # r - read w-write a-append   
#                     # if w mode me aise file ko khol diya jo exist nhi krta then
#                                  # naya file bn ke aa jaeyga
# # # print(f)
# text = f.read()
# print(text)
# f.close()

# WRITING A FILE
f=open('myfile.txt', 'a') 
f.write('Hello, world!')
f.close() # yha pe close krna pdta g har samay buut using WITH no need to close

with open('myfile.txt','a') as f:
 f.write("hey i mm inside the environment")