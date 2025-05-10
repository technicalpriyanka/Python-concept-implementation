def func1():

    try:
        a = [1, 2, 3]
        i = int(input("Enter an index: "))
        print(a[i])


    except IndexError:
        print("Index out of range. Please check your list or string.")
    
        return 0
    
    finally:
        print("This block always executes, regardless of exceptions.")
    # print("This block will always execute")

x=func1()
print(x)