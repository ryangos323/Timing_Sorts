from testSorts import *

def insertionSort(L):
    for i in range(1,len(L)):
        temp = L[i]
        j = i - 1
        while j >= 0:
            if temp < L[j]:
                L[j+1] = L[j]
                L[j] = temp
                j = j - 1
            else:
                break
            
def mergeSort(L):
    if len(L) <= 1:
        return
    else:
        mid = len(L)//2
        a = L[:mid]
        b = L[mid:]
        for i in range(len(a)):
            a[i] = L[i]
        for i in range(len(b)):
            b[i] = L[len(a) + i]
        mergeSort(a)
        mergeSort(b)
        merge(a,b,L)

def merge(a, b, L):
    a_count = 0
    b_count = 0
    L_count = 0
    while a_count < len(a) and b_count < len(b):
        if a[a_count] < b[b_count]:
            L[L_count] = a[a_count]
            a_count = a_count + 1
        else:
            L[L_count] = b[b_count]
            b_count = b_count + 1
        L_count = L_count + 1
    while a_count < len(a):
        L[L_count] = a[a_count]
        a_count = a_count + 1
        L_count = L_count + 1
    while b_count < len(b):
        L[L_count] = b[b_count]
        b_count = b_count + 1
        L_count = L_count + 1
