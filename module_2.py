import os
import shutil
import send2trash


new_file = open('new_1.txt' , "w")
new_file.write("hey")
new_file.close()


print(os.getcwd())
# print(os.listdir())

# to dlt file
send2trash.send2trash('new_1.txt')


# to move the file
# shutil.move('new_1.txt' , '/home/aladeen/Documents/p_env')   #if we use tthis twice o more time then it will throw an error




# exmaple 1
print(os.listdir('/home/aladeen/Documents/p_env'))

# by using this we can see all the files in the foldder
file_deesti = '/home/aladeen/Downloads/school stuff'

for folder,sub_folder,file in os.walk(file_deesti):
    print(f"currently looking at {folder}")
    print('/n')
    print("the subfolders are :")
    for subfold in sub_folder:
        print(f'subFolder : {subfold}')
    print("the files are: ")
    for f in file:
        print(f"files : {f}")

# example 2
# from this we can check how many are ther in the folder and its subfolder
file_deest = '/home/aladeen/Documents/GitHub cloned files/python'

for folder,sub_folder,file in os.walk(file_deest):
    print(f'looking at {folder}')
    print('------------')
    print('subFolders :')
    for sf in sub_folder:
        print(f'subfolders : {sf}')
        # print(len(sf))
    print('------------')
    print('files :')
    for fil in file:
        print(f'files ; {fil}')
        # print(len(file))
    print("-----------")




# to make a multiple files in directry
# os.mkdir("new_2")
for i in range(1,100):
    os.mkdir(f"new_2/day{i + 1}")