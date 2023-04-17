# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 23:26:56 2022

@author: User
"""

def heapify(A,i):
    l = 2*i+1
    r = 2*i+2
    if l <= len(A)-1 and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= len(A)-1 and A[r] > A[largest]:
        largest = r 
    if largest != i:
        A[i],A[largest] = A[largest],A[i]
        heapify(A, largest)
    return A

def buildHeap(A):
    n = len(A)
    i = (n//2)
    while i>=0:
        heapify(A,i)
        i -= 1
    return A

def heapSort(A):
    B = []
    A = buildHeap(A)
    n = len(A)
    i=n-1
    while i!=1:
        A[0],A[i] = A[i],A[0]
        B.append(A.pop(i))
        i -= 1
        heapify(A,0)
    B.append(A[0])
    B.append(A[1])
    return B


j=[4,1,3,2,16,9,10,14,8,7]
l = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]

# print(buildHeap(j))
# l = heapify(j,s)
# print(l)
print(heapSort(j))
