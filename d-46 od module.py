# os module
import os

# to make directory 

if not os.path.exists("new"):
    os.mkdir("new")
for i in range(1, 10):
    os.mkdir(f"new/days{ i + 2}")


# to change then name of folders in directory 
for i in range(1 , 10 ):
    os.rename(f"new/days{i + 2}", f"new/numers {i + 2}")

# to check how many folders are  theere in directtory 
folders = os.listdir("new")
print(folders)


# or 

for folder in folders:
    print(folder)



