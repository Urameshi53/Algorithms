# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 14:54:49 2022

@author: User
"""

def heapify(A,i):
    l = 2*i+1
    r = 2*i+2
    if l < len(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < len(A) and A[r] > A[largest]:
        largest = r 
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, largest)
    return A

def buildHeap(A):
    n = len(A)
    i = (n//2)
    while i>=0:
        # print(A,i)
        A = heapify(A,i)
        i -= 1
    return A
l = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
# print(heapify(l, 2))
k=[1,2,3,4,5,6,7,8,9,10]
print(buildHeap(k))
j=[4,1,3,2,16,9,10,14,8,7]

m = [10,27, 17, 10, 16, 13,2, 9, 1, 5, 7, 12, 4, 8, 3, 0]
# print(buildHeap(m))
# print(buildHeap(k))
# k = buildHeap(k)
m = heapify(m, 0)
# print(heapify(m,6))


class BinaryHeap(object):
    def __init__(self, L=[]):
        self.L = L
        
    def heapify(self,i):
        l = 2*i+1
        r = 2*i+2
        if l <= len(self.L)-1 and self.L[l] > self.L[i]:
            largest = l
        else:
            largest = i
        if r <= len(self.L)-1 and self.L[r] > self.L[largest]:
            largest = r 
        if largest != i:
            t = self.L[i]
            self.L[i] = self.L[largest]
            self.L[largest] = t 
            heapify(self.L, largest)
        return self.L

    def buildHeap(self):
        n = len(self.L)
        i = (n//2)
        while i>=0:
            self.L = heapify(self.L,i)
            i -= 1
        return self.L
    
    def insert(self, x):
        self.L = [x] + self.L 
        self.heapify(0)
        return self.L 
    
    def printHeap(self):
        for i in self.L:
            print(i)
            
    def parentOf(self,key):
        parentIndex = (self.L.index(key)//2)
        return self.L[parentIndex]
    
    def childrenOf(self,key):
        p = self.L.index(key)
        l = p*2+1
        r = p*2+2
        if l < len(self.L):
            print('LeftChild',self.L[l])
        if r < len(self.L):
            print('RightChild',self.L[r])
        return
        
    def maxValue(self):
        return self.L[0]
    
    def ascOrder(self):
        while len(self.L)!=0:
            print(self.L[0])
            self.L.pop(0)
            self.heapify(0)
    
B = BinaryHeap()
B.insert(10)
B.insert(27)
B.insert(17)
B.insert(25)
B.insert(12)
B.insert(30)
B.insert(32)
B.insert(45)
B.insert(3)
B.insert(9)
# print(B.parentOf(17))
# print(B.childrenOf(12))
# B.printHeap()
# B.ascOrder()
        
        
    
    
    
    
    
    
    