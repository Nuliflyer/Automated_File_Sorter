import os
import shutil

def sort(path, depth):
    files = os.listdir(path)
    for i in range(26):
        if os.path.exists(path + "\\" + chr(i + 97)):
            continue
        else:
            os.mkdir(path + "\\" + chr(i + 97))

    for i in files:
        if isLetter(i[depth:depth+1]) and "." in i:
            c = (i[depth:depth+1])
            shutil.move(path+"\\"+i, path+"\\"+c)

    maxlen = 0
    for i in os.listdir(path):
        if len(i) > maxlen:
            maxlen = len(i)

    if depth <= maxlen:
        for a in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
            sort(path + "\\" + a, depth + 1)


#os.mkdir()

def isLetter(letter):
    list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if letter in list:
        return True
    else: return False

base_path = "C:\Users\Nuliflyer's Account\Desktop\Testing_Folder"
sort(base_path, 0)
