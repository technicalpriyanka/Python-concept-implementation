import os

if(os.path.exists('test_dir')):  # check if the directory exists
    os.mkdir('test_dir')        #create a directory
for i in range(1, 100):
    os.mkdir(f"test_dir/day{i+1}")

for i in range(1, 100):
    os.rename(f"test_dir/day{i+1}", f"test_dir/day{i+1}1")  #rename the directory
#rename the file
# os.rename('test.txt', 'test1.txt')

folders= os.listdir('test_dir')  # list all the directories
for folder in folders:
    print(os.listdir(f'test_dir/{folder}'))  # list all the files in the directory

print(os.getcwd())  # print the current working directory