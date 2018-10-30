

import os

def getFolderSize(folder):
    for item in os.scandir(folder):
        if item.is_file():
            print("FILE");
        elif item.is_dir():
            getFolderSize(item.path)
            print("DIR")

"""
def folder_size(path='.'):
    total = 0
    for entry in os.scandir(path):
        if entry.is_file():
            total += entry.stat().st_size
        elif entry.is_dir():
            total += folder_size(entry.path)
    return total
"""


getFolderSize("/home/matthew/Projects/CS537")
