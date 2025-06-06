import os

#create the new folder using mkdir function by importing OS package 

if(not os.path.exists("data")):
    os.mkdir("data")

for i in range(0, 100):
    os.mkdir(f"data/Day{i+1}")
    
