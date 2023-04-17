# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 13:14:09 2022

@author: User
"""

# import math

def merge(left, right):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    print('merge: ' + str(left) + '&' + str(right) + ' to ' +str(result))
    return result

def merge_sort(L):
    print('merge sort: ' + str(L))
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)
    
# def merge(A, p, q, r):
#     n1 = q-p+1
#     n2 = r-1
#     left = []
#     right = []
#     for i in range(n1):
#         left[i] = A[p+i-1]
#     for j in range(n2):
#         right[j] = A[q+j]
#     left[n1+1] = 100
#     right[n2+1] = 100
#     i = 1 
#     j = 1
#     for k in range(p,r):
#         if left[i] <= right[j]:
#             A[k] = left[i]
#             i = i + 1
#         else:
#             A[k] = right[j]
#             j = j + 1 
            
# def mergeSort(A,p,r):
#     if p < r:
#         q = math.floor(((p+r)/2))
#         mergeSort(A,p,q)
#         mergeSort(A,q+1,r)
#         merge1(A,p,q,r)
    
l = [1,3,2,5,6,4]
# print(mergeSort(l,1,len(l)))

# def mymerge(left, right):
#     l = []
#     t = len(left)+len(right)
#     for i in range(len(left)):
#         if left[i] < right[i]:
#             l.append(left[i])
#         else:
#             l.append(right[i])
#     l = l + right[len(left)+1:]
#     return l

# print(mymerge(l,r))

# def merge(left, right):
#     if len(left) <= len(right):
#         n = len(left)
#     else:
#         n = len(right)
#     i,j = 0,0
#     A = []
#     for k in range(n):
#         if left[i] <= right[j]:
#             A.append(left[i])
#             i += 1
#         else:
#             A.append(right[j])
#             j += 1
#     A = A+left[i:]
#     A = A+right[j:]
#     return A

j=[4,1,3,2,16,9,10,14,8,7]

# def mergeSort(l):
#     print(l)
#     if len(l) < 2:
#         return l
#     else:
#         mid = len(l)//2
#         left = mergeSort(l[:mid])
#         right = mergeSort(l[mid:])
#         # print(left,right)
#         return merge(left, right)
    
# l = [1,2,4]
# r = [6,8,9,11,12]
# print(merge(l,r))  
print(merge_sort(j))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    