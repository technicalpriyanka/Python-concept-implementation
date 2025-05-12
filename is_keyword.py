#difference between is and == 

# is checks for identity, == checks for equality
# is checks if two variables point to the same object in memory

# is - exact memory location
# == - value of the object

a = 4
b='4'
print(a is b)   #exact location object in memory
print(a==b)   #value of the object  

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)   #exact location object in memory
print(a==b)   #value of the object

# is - exact memory location
a=3
b=3
print(a is b)
print(a==b)

a = "string"
b= 'string'
print(a is b)
print(a==b)


a = None
b=None
print(a is b)
print(a is None)
print(a == b)