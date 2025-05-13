#self is a reference to the current instance of the class
# It is used to access variables that belong to the class.

class person:
    name = "John Doe"
    occupation = "Software Engineer"
    networth = 1000000

    def info(self):
        print(f"{self.name} is a {self.occupation} with a net worth of {self.networth}.")

a = person()
b=person()

a.name = "Priyanka"
a.occupation = "Data Scientist"
# print(a.name)

b.name = "John"
b.occupation = "Software Engineer"

a.info()
b.info()