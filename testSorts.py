from sorts import *
import random

def randomList(size, low, up):
    L = []
    for i in range(size):
        L = L + [random.randint(low,up)]
    return L

def isSorted(L):
    rt = True
    for i in range(len(L)-1):
        if L[i] <= L[i+1]:
            rt = True
        else:
            return False
    return rt

def testInsertionSort(low,up,rep):
    while(low<=up):
        for i in range(rep):
            L = randomList(low,0,100)
            print(L)
            insertionSort(L)
            rt = isSorted(L)
            if rt:
                print(L)
                print("TRUE: The list was sorted")
            else:
                print(L)
                print("FALSE: The list was NOT sorted")
        low = low + 1

def testMergeSort(low,up,rep):
    while(low<=up):
        for i in range(rep):
            L = randomList(low,0,100)
            print(L)
            mergeSort(L)
            rt = isSorted(L)
            if rt:
                print(L)
                print("TRUE: The list was sorted")
            else:
                print(L)
                print("FALSE: The list was NOT sorted")
        low = low + 1
