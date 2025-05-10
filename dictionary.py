#dictionary

dic = {
    "Priyanka" : "Human being",
    "spoon" : "object"
}

print(dic["Priyanka"])

dic = {
    465 : "Human being",
    454 : "object",
    152 : "neha"
}

print(dic[152])

print(dic)

print(dic.get(465))
#.get will get None if the key is not present in the dictionary

print(dic.keys())

for key in dic.keys():
    # print(dic[key])
    print(f"the value of {key} is {dic[key]}")


print(dic.items())

for key, value in dic.items():
    print(f"the value of {key} is {value}")




#dictionary methods
print(dic.update({1: "object"}))

print(dic)

print(dic.pop(1))
print(dic)

# dic.clear()
print(dic)

dic.popitem()
print(dic)


dic1=dic.copy()
print(dic1)

del dic1[465]

print(dic1)
