

import os
from directory import Directory

def getFolderSizeOld(folder):
    total = 0
    tempTotal = 0
    errorNum = 0
    try:
        for item in os.scandir(folder):
            if item.is_file():
                total+=item.stat().st_size
            elif item.is_dir():
                tempTotal+=getFolderSize(item.path)
                total+=tempTotal
                if "GB" in humanReading(tempTotal) or "MB" in humanReading(tempTotal):
                    print(item.path + ": " + humanReading(tempTotal))
                tempTotal=0
    except Exception as e:
        print("Access Denied")
    return total

def getFolderSize(folder, dirList):
    currDir = Directory(folder, 0)
    currDir.size+=getFolderSizeHelper(folder, dirList, currDir, 1)
    return currDir.size

def getFolderSizeHelper(folder, dirList, currDir, nested):
    for item in os.scandir(folder):
        if item.is_file():
            currDir.size+=item.stat().st_size
        elif item.is_dir():
            subDir = Directory(item.path[(item.path).rfind('/'):], (nested + 1))
            currDir.size += getFolderSizeHelper(item.path, dirList, subDir, subDir.size)

    dirList.append(currDir)
    return  currDir.size





def humanReading(num):
    label = ['B', 'KB', 'MB', 'GB', 'TB']
    formatStr = "%i %s"
    radix = 1024
    i = 0
    while i >= 0:
        if (num // radix) > 0:
            num = (num//radix)
            i+=1
        else:
            break
    return formatStr % (num, label[i])


#print(humanReading(getFolderSize("/home/matthew")))

directories = []
print(humanReading(getFolderSize("/home/matthew", directories)))
for dir in directories:
#    if "GB" in humanReading(dir.size) or "MB" in humanReading(dir.size):
    for i in range (0, dir.nested):
        print("-", end =" ")
    print(dir.name + ": " + humanReading(dir.size))
