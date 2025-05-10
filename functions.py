def my_val(val):
    a = 5
    list = []
    for i in range(1, val+1):
        i*=a
        list.append(i)
    return list


val = 10
ans=my_val(val)
print("The value is:", ans)
# print("The value is:", my_val(val))