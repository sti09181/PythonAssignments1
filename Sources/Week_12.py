######################
##### Week_12.py #####
######################


import math
import datetime
import inspect
import subprocess
import webbrowser
import os
import queue


import matplotlib.pyplot as plt
import numpy as np


def Solution1():
    print(f"PI = {math.pi}")
    print(f"e = {math.e}")
    print(f"sin(PI/2) = {math.sin(math.pi / 2)}")
    print(f"cos(PI) = {math.cos(math.pi)}")
    print(dir(math))
    print(inspect.getfile(datetime))


def Solution2():
    subprocess.call("cmd")


def Solution3():
    webbrowser.open("https://cs.kookmin.ac.kr")


def Solution4():
    print(os.listdir("."))


def Solution5():
    path = "C:/"
    dirFiles = os.listdir(path)
    dirNames = []
    fileNames = []

    for each in dirFiles:
        fullName = path + each

        if os.path.isdir(fullName):
            dirNames.append(fullName + "/")
        else:
            fileNames.append(fullName)

    print("dirNames : ")
    print(dirNames)
    print("fileNames : ")
    print(fileNames)


#####################
##### Homeworks #####
#####################


def Homework1():
    def GetSubDir(path):
        try:
            dirFiles = os.listdir(path)
        except PermissionError:
            return []

        subdirList = []

        for eachFile in dirFiles:
            fullName = path + eachFile
            if os.path.isdir(fullName):
                subdirList.append(fullName + "/")
        return subdirList

    dirQueue = queue.Queue()
    dirQueue.put("./")

    allDirs = []

    while not dirQueue.empty():
        dirName = dirQueue.get()
        allDirs.append(dirName)

        subdirNames = GetSubDir(dirName)

        for eachSubdir in subdirNames:
            dirQueue.put(eachSubdir)

    print(allDirs)


def Homework2():
    file = open("Input_File.txt", "r")
    words = file.read().split()
    file.close()

    needsToBeDeleted = "~ ` ! @ # $ % ^ & * ( ) { } : \" < > ? [ ] ; \' , . / 1 2 3 4 5 6 7 8 9 0 _ - + = \t \n"
    needsToBeDeleted = needsToBeDeleted.split()
    needsToBeDeleted.append(" ")

    result = {}

    for i in range(len(words)):
        words[i] = words[i].upper()

        for j in range(len(needsToBeDeleted)):
            words[i] = words[i].replace(needsToBeDeleted[j], "")

        if words[i] not in result:
            result[words[i]] = 1
        else:
            result[words[i]] += 1

    result = {key: value for key, value in sorted(result.items(), key=lambda item: item[1], reverse=True)}

    fig, ax = plt.subplots(1, 1)

    counts = np.array(list(result.values()))

    ax.hist(counts, bins=range(0, 2001, 50))
    ax.set_title("Les Miserables Histogram")
    ax.set_xticks(range(0, 2001, 200))
    ax.set_yticks(range(0, 101, 10))
    ax.set_ylim(0, 100)
    ax.set_xlabel("Bin/Interval")
    ax.set_ylabel("Count/Frequency")
    plt.show()
