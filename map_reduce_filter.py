#map, filter, reduce

#map
def cube(x):
    return x**3

print(cube(3))  # 27

l = [1, 2, 3, 4, 5]
# ans=[]
# for item in l:
#     ans.append(cube(item))
# print(ans)  # [1, 8, 27, 64, 125]

print(list(map(cube, l)))

##filter

def filter_function(x):
    return x>2

newl = list(filter(filter_function, l))
print(list(newl))  # [5]

#reduce
from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x,y:x+y, numbers)

print(sum)  # 15

def my_sum(x,y):
    return x+y
sum = reduce(my_sum, numbers)
print(sum)  # 15