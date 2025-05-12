x=4
print(x)

def hello():
    global a
    a = 10
    x=5
    y=1
    print(x)
    print("Hello World")
print(f"the global variable x is {x}")
hello()

print(a)
print(f"the global variable x is {x}")