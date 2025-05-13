
def greet(func):
    def mfx(*args, **kwargs):
        print("Good Morning")
        func(*args, **kwargs)
        print("Thanks for the function")
    return mfx

@greet
def hello():

    print("Hello, World!")

@greet
def add(x, y):
    print(x+y)



# greet(hello)() #no need to @greet above

hello()
add(10, 20)