import os
import random

n = 100

base_path = "C:\Users\Nuliflyer's Account\Desktop\Testing_Folder"

for i1 in range(n):
    i = ""
    for i2 in range(3):
         i = i + chr(random.randint(0,25)+97)

    filename = os.path.join(base_path, i + ".txt")
    f = open(filename, "w")
    f.close()
