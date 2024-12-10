                      # Write a python program to translate a message into secret code language. 
                      # Use the rules below to translate normal English into secret code language
# Coding:
 # if the word contains atleast 3 characters, remove the first letter and append it at the end
 #    now append three random characters at the starting and the end
 # else:
 #   simply reverse the string
# Decoding:
 # if the word contains less than 3 characters, reverse it
 # else:
 #   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
 # Your program should ask whether you want to code or decode

                                   #short method
# def encode(word):
#     return word[::-1] if len(word) < 3 else "abc" + word[1:] + word[0] + "xyz"

# def decode(word):
#     return word[::-1] if len(word) < 3 else word[-4] + word[3:-4]

# mode = input("Choose 'encode' or 'decode': ").strip().lower()
# message = input("Enter your message: ").strip()
# result = ' '.join((encode if mode == "encode" else decode)(word) for word in message.split())
# print("Result:", result)

def encode(word):
    if len(word) < 3:
        return word[::-1]  # Reverse the word but -1 HELLO   _1,-1 krte krte o,l,l,e,h
    else:
        return "abc" + word[1:] + word[0] + "xyz"  # Modify the word

def decode(word):
    if len(word) < 3:
        return word[::-1]  # Reverse the word
    else:
        return word[-4] + word[3:-4] 
    
mode = input("Enter 'code' to encode or 'decode' to decode: ")
message = input("Enter the message: ")

words = message.split()  #convert kr dega list me  "hello world"-----["hello", "world"]
result = []
for word in words:
    if mode == "encode":
        result.append(encode(word))
    elif mode == "decode":
        result.append(decode(word))
    else:
        print("Invalid mode. Please choose 'encode' or 'decode'.")
        break
print("Result:", ' '.join(result)) #Joins words in the result list into a single string, with a space (' ') between each word.
