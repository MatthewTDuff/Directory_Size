

import os
from directory import Directory

def getFolderSize(folder):

    total = 0
    tempTotal = 0
    for item in os.scandir(folder):
        if item.is_file():
            total+=item.stat().st_size
        elif item.is_dir():
            tempTotal+=getFolderSize(item.path)
            total+=tempTotal
            if "GB" in humanReading(tempTotal) or "MB" in humanReading(tempTotal):
                print(item.path + ": " + humanReading(tempTotal))
            tempTotal=0
    return total


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


print(getFolderSize("/home"))
