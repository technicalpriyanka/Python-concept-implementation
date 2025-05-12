from collections import Counter
data = [1, 2, 3, 2, 4, 1, 5]
res=[]
for i in data:
    if i > 1:
        res.append(data[i])

print(res)
