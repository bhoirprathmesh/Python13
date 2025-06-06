import os
 
folders = os.listdir("data")

#List all the folders
for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))
    