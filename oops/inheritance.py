#inheritance
# Inheritance is a way to form new classes using classes that have already been defined.
# The new classes are called derived classes, and the classes that we derive from are called base classes.

# Inheritance allows us to reuse code and create a hierarchy of classes.

class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")

#inheritance
# The derived class (child class) inherits the properties and methods of the base class (parent class).
class manager(employee):
    def showlanguage(self):
        print("The default language is Python")

e1 = employee("Priyanka", 101)
e1.showDetails()

e2 = manager("Divya", 102)
e2.showDetails()
e2.showlanguage()

