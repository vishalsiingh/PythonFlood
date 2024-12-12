# with open('file.txt','w') as f:
#     print(f)   # use kiye naya text file crate krne ke liye 

    # NOW

with open('file.txt','r') as f:
    print(type(f))
    f.seek(11) #move 11 byte in the file 
    print(f.tell()) # ye current postion return kr dega 
    data =f.read(5) # wha se next 5 character read karega 
    print(data)


 
