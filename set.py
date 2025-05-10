# #set 

# 1. Sets are collection of well defined data type.
# 2. Set in python is made by { }
# 3. all functions of list are applicable to sets
# 4. sets and lists are different in only that a set does not allow repetition of same entry while in list you can repeat the same item.
# 5. Empty set is made by Emptyset= ( ) instead of { }
# 6. There is no guaranttee of order being maintained by Python within a set so output can change every time. (bummer)
# 7. To get items you can use for loop just like a list.
s={1,2,3,4,2,5}
print(s) #output: {1, 2, 3, 4, 5}

#creating empty set

s=set()
print(type(s)) #output: <class 'set'>

info = {'priyanka', 1.3, 2, False, 5}
print(info) #output: {False, 1.3, 2, 5, 'priyanka'}

for i in info:
    print(i) #output: False 1.3 2 5 priyanka

s={1,2,3,4,5}
#set methods
# 1. add() - adds an element to the set
s.add(6)
print(s) #output: {1, 2, 3, 4, 5, 6}

s1={1,2,3,4,5}
s2={6,7,8,9,10}
print(s1.union(s2))
print(s1 | s2) 
print(s1.intersection(s2))


cities1 = {'delhi', 'mumbai', 'banglore', 'chennai'}
print(cities1) #output: {'banglore', 'mumbai', 'delhi', 'chennai'}

print(cities1.add('kolkata')) #output: None
print(cities1) #output: {'banglore', 'kolkata', 'mumbai', 'delhi', 'chennai'}

cities2 = {'delhi', 'mumbai', 'banglore', 'chennai'}
print(cities2) #output: {'banglore', 'mumbai', 'delhi', 'chennai'}

print(cities1.isdisjoint(cities2)) #output: False

print(cities1.issubset(cities2)) #output: False

print(cities1.issuperset(cities2)) #output: False

cities1.remove('kolkata')
print(cities1) #output: {'banglore', 'mumbai', 'delhi', 'chennai'}

cities1.discard('kolkata')
print(cities1) #output: {'banglore', 'mumbai', 'delhi', 'chennai'}


item = cities1.pop()
print(item) #output: banglore

cities1.clear()
print(cities1) #output: set()  #remove all items from the set