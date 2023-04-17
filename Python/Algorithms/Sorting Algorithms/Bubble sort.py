# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 13:15:02 2022

@author: User
"""

def bubble_sort(L):
    swap = False
    while not swap:
        print('bubble sort: ' + str(L))
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp

testList = [1,3,5,7,2,6,25,18,13]
l = [6,1,5,3,4,2]

def bubbleSort(l):
    for i in range(1,len(l)):
        for j in range(i):
            # print(l)
            if l[i] < l[j]:
                print(l)
                t = l[j]
                l[j] = l[i]
                l[i] = t    
    return l

# print('')
# print(bubble_sort(testList))
# print(testList)
print(bubbleSort(l))