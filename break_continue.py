x=10

for i in range(1, x+1):
    if i != 7:
        print(i, i*5)
        continue

    if i == 8:
        break
    print("This will not be printed")