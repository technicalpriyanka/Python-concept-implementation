# f=open('\A\Concept\myfile.txt', 'rb')
# print(f.read())  # read the file
# f.close()  # close the file

f=open('myfile.txt', 'w')
f.write("Hello World")  # write to the file
f.close()  # close the file

with open('myfile.txt', 'a') as f:
    f.write("Hello World sasdtstyyfsyfstaf fyudsfugfsdgfh dsghdgfhdsgfhdsgfhsdgfhdsgfyegryiuqeyjnxzbchjdsv")  # write to the file

#readline method
f=open('myfile.txt', 'r')
while True:
    line = f.readline()  # read a line from the file
    m1 = line.split(",")[0]
    print("m1---", m1)
    if not line:  # if the line is empty, break the loop
        break
    print(line)  # print the line