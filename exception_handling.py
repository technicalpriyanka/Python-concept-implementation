#try excetion handling

try:
    num = int(input("Enter a number: "))
    a = [6,3]
    print(a[num])

except ValueError:
    print("Please enter a valid number.")

except IndexError:
    print("Index out of range. Please check your list or string.")  


# a =int(input("enter a number :"))

# print(f"the number is : ,{a}")

# try:
#     for i in range(1, 11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# except Exception as e:
#     print("An error occurred:", e)