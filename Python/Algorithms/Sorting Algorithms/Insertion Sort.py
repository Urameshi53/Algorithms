# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 22:24:18 2022

@author: User
"""

l = [6,1,5,3,4,2]



# print(insertionSort(l))
# insertionSort(l)

def insertionsort(l):
    for j in range(1,len(l)):
        k = l[j] # Taking each element
        i = j - 1 
        while i >= 0 and l[i] > k:
            # print('k',k)
            # print('i',i)
            l[i+1] = l[i]
            i=i-1
        l[i+1] = k
    return l

print(insertionsort(l))
# insertionsort(l) 