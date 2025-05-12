# lambda : anonymous function
# lambda function : a function that is defined without a name

# def double(x):
#     return x*2

# double = lambda x: x*2

cube = lambda x:x**3
print(cube(3))  # 27
# print(double(5))  # 10


# avg = lambda x, y:(x+y)/2
# print(avg(2, 9))

# avg = lambda x, y,z: (x+y+z)/3
# print(avg(2, 9, 3))

def appl(fx, value):
    return 6+fx(value)
print(appl(cube, 2))

print(appl(lambda x:x**2, 4))