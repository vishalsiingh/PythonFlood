class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Getter method for getting the name attribute
    def get_name(self):
        return self._name

    # Setter method for setting the name attribute
    def set_name(self, name):
        self._name = name

    # Getter method for getting the age attribute
    def get_age(self):
        return self._age

    # Setter method for setting the age attribute
    def set_age(self, age):
        if age > 0:
            self._age = age
        else:
            print("Age must be a positive number.")

# Creating an instance of the Person class
person = Person("Alice", 30)

# Using the getter method to get the name attribute
print(person.get_name())  # Output: Alice

# Using the setter method to set the name attribute
person.set_name("Bob")
print(person.get_name())  # Output: Bob

# Using the setter method to set the age attribute with an invalid value (negative number)
person.set_age(-5)  # Output: Age must be a positive number.

# Using the setter method to set the age attribute with a valid value
person.set_age(35)
print(person.get_age())  # Output: 35