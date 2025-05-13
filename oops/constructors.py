#constructors.py
# This file contains the constructors for the classes in the oops module.

class person:
    # name = "Priyanka"
    # occupation = "Software Engineer"
    def __init__(self, name, occupation):
        print("Constructor called")
        self.name = name
        self.occupation = occupation

    def info(self):
        print(f"Name: {self.name}")
        print(f"Occupation: {self.occupation}")

a = person("Priyanka", "Software Engineer")
b = person("Divya", "Data Scientist")
# c = person(1,2, 3) #person.__init__() takes 3 positional arguments but 4 were given 
# a = person()
# a.name = "Divya"
# a.occupation = "Data Scientist"
a.info()
b.info()
# The above code defines a class called `person` with two attributes: `name` and `occupation`.