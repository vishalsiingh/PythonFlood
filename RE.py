my_list = [1, 2, 3]
my_list.append(4)          # Adds an element
my_list.remove(2)          # Removes an element
my_list.pop()              # Removes and returns the last element
my_list.insert(1, 'a')     # Inserts 'a' at index 1
print(len(my_list))        # Length of the list



my_tuple = (1, 2, 3)
print(my_tuple[1])         # Access element at index 1
print(len(my_tuple))       # Length of the tuple


my_dict = {'a': 1, 'b': 2}
my_dict['c'] = 3           # Add new key-value pair
del my_dict['a']           # Remove key 'a'
print(my_dict.get('b'))    # Get value for key 'b'
print(my_dict.keys())      # Returns all keys
print(my_dict.values())    # Returns all values

