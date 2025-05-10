#custom errors

a = input("Enter any value between 1 and 10: ")

if a.lower() == 'quit':
    print("You have quit the program.")

else:
    try:
        a = int(a)
        if (a < 1 or a > 10):
            
            raise ValueError("Value out of range. Please enter a number between 1 and 10.") 
    except ValueError as e:
        print(e)