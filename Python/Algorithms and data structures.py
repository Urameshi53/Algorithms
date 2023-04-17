# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 11:33:06 2021

@author: User
"""

# INSERTION SORT
m = [10,51,2,18,4,31,13,5,23,64,29]
def selection_sort(l):
    p = 0
    for i in range(len(l)):
        print(l, i)
        m = l[i]
        for j in range(i, len(l)):
            if l[j] <= m:
                m = l[j]
                p = j
        if p != i:
            l[p], l[i] = l[i], l[p]
    
    return l
# print("Selection sort")
# print(selection_sort(m))
# print()

def selection_sort2(l):
    s = 0
    while s != len(l):
        print(l, s)
        for i in range(s,len(l)):
            if l[i] < l[s]:
                l[i], l[s] = l[s], l[i]
        s += 1
        
    return l
        
m = [10,51,2,18,4,31,13,5,23,64,29]
# print("Selection sort 2")
# print(selection_sort2(m))

# BUBBLE SORT
k = [6,3,2,4,1,5,10,8,7,9]
def bubble_sort(l):
    for i in range(len(l)):
        print(l, i)
        for j in range(len(l)-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                
    return l
# print("\nBubble sort")
# print(bubble_sort(k))

n= ['emma', 'kojo', 'zigah', 'joe', 'james', 'john']
# print(insertion_sort(n))


# MERGE SORT
# def fib(n):
#     d = {}
#     if n == 0 or n==1:
#         return 1
#     elif n in d:
#         return d[n]
#     else:
#         a = fib(n-1)+fib(n-2)
#         d[n] = a
#         print(d)
#         return d[n]
    
    
# dic = {}
# for i in range(6):
#     dic[i] = n[i]
# print(dic)
m = [10,51,2,18,4,31,13,5,23,64,29]
def insertion_sort(l):
    n = len(l)
    for i in range(1,n):
        print(l, i)
        v = l[i]
        p = i
        while p > 0 and v < l[p-1]:
            l[p] = l[p-1]
            p-=1
        l[p] = v
        
    return l

# print("\nInsertion sort")
# print(insertion_sort(m))

n = [2, 4, 5, 10, 13, 23, 29, 31, 51, 64, 18]
def proper(l,n):
    print(l)
    p = l.index(n)
    while p > 0 and n < l[p-1]:
        l[p] = l[p-1]
        print(l)
        p-=1
    l[p]=n
    return l
    
# print()
# print(proper(n,18))

# Merge sort
def merge(left, right):
    result = []
    i,j = 0,0
    while i<len(left) and j<len(right):
        
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i<len(left):
        result.append(left[i])
        i += 1
    while j<len(right):
        result.append(right[j])
        j += 1
    print('merge: ' + str(left) + ' & ' + str(right) + ' to ')
    return result

left = [2, 4, 5, 10, 13, 18]
right = [6, 7, 8, 9, 11]
# print(merge(left, right))

def merge_sort(l):
    print('merge sort: ' + str(l))
    if len(l) < 2:
        return l[:]
    else:
        mid = len(l)//2
        left = merge_sort(l[:mid])
        right = merge_sort(l[mid:])
        return merge(left, right)

m = [10,51,2,18,4,31,13,5,23,64,29]

# print(merge_sort(m))


# Linked Structures
# Linked List
# Node
class Node():
    def __init__(self, data):
        self.data = data
        self.nest = None
        
c = Node(12)
b = Node(11)
a = Node(10)

a.nest = b
b.nest = c

# print(a.data)
# print(a.nest.data)
# print(a.nest.nest.data)

class LinkedList():
    def __init__(self):
        self.head = None
        
    def traversal(self,head):
        curNode = head
        while curNode is not None:
            print(curNode.data)
            curNode = curNode.nest
        
# def genSubsets(L):
#     res = []
#     if len(L) == 0:
#         return [[]] #list of empty list
#     smaller = genSubsets(L[:-1]) # all subsets without last element    
#     extra = L[-1:] # create a list of just last element
#     # print(smaller,'s')
#     # print(extra,'e')
#     new = []
#     for small in smaller:
#         new.append(small+extra)  # for all smaller solutions, add one with last element
#     return smaller+new  # combine those with last element and those without


testSet = [1,2,3]
# print(testSet[:-1])
# print(testSet[-1:])
# print(genSubsets(testSet))
# print(len(genSubsets(testSet)))