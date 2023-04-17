# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 23:35:49 2022

@author: User
"""

class PriorityQueue(object):
    def __init__(self, A=[]):
        self.A = self.buildHeap(A)
        
    @staticmethod
    def heapify(A, i):
        l = 2*i
        r = 2*i+1
        if l < len(A) and A[l] > A[i]:
            largest = l
        else:
            largest = i
        if r < len(A) and A[r] > A[largest]:
            largest = r 
        if largest != i:
            A[i],A[largest] = A[largest],A[i]
            PriorityQueue.heapify(A, largest)
        return A
    
    @staticmethod
    def buildHeap(A):
        n = len(A)
        i = (n//2)
        while i>=0:
            PriorityQueue.heapify(A,i)
            i -= 1
        return A

    def extractMax(self):
        if len(self.A) < 1:
            print("Error: Heap Overflow")
            return
        maximum = self.A[0]
        self.A[0] = self.A[len(self.A)]
        self.A.pop(0)
        self.heapify(self.A,0)
        return maximum
    
    def heapMaximum(self):
        return self.A[0]
    
    def heapIncreaseKey(self, old, key):
        i = self.A.index(old)
        p = (i//2)
        if key < self.A[i]:
            print("Error: Key is smaller than current key")
            return
        self.A[i] = key 
        while i > 0 and self.A[p] < self.A[i]:
            self.A[i], self.A[p] = self.A[p], self.A[i]
            i = p
            p=i//2
        return self.A
    
    def heapInsert(self, key):
        self.A.append(key)
        self.buildHeap(self.A)
        return self.A
    
    def heapAdd(self,key):
        self.A.append(-1)
        self.heapIncreaseKey(-1,key)
        return self.A
    
    def printQueue(self):
        for i in self.A:
            print(i)
           
    @staticmethod
    def heapSort(A):
        B = []
        A = PriorityQueue.buildHeap(A)
        n = len(A)
        i=n-1
        while i!=1:
            A[0],A[i] = A[i],A[0]
            B.append(A.pop(i))
            i -= 1
            PriorityQueue.heapify(A,0)
        B.append(A[0])
        B.append(A[1])
        return B

l = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
P = PriorityQueue(l)
print(P.heapMaximum())
P.printQueue()
# print(P.heapIncreaseKey(7,30))
# print(P.heapAdd(45))
# print(P.heapAdd(45))
# print(PriorityQueue.heapSort(l))
