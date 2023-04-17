# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 16:30:24 2022

@author: lancelot
"""


def maxSubarray(l,low,mid,high):
    left_sum = -100
    s,max_left,max_right = 0,0,0
    i = mid
    while i > low:
        s = s + l[i]
        if s > left_sum:
            left_sum = s
            max_left = i
        i -= 1
    right_sum = -100
    s = 0
    for j in range(mid+1,high):
        s = s + l[j]
        if s > right_sum:
            right_sum = s
            max_right = j
    return (max_left,max_right,left_sum+right_sum)

l = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
# print(maxSubarray(l, 0, len(l)//2, len(l)))

def find_max_sub(l,low,high):
    if high == low:
        return (low,high,l[low])
    else:
        mid = (low+high)//2
        # max_right,max_left = 0,0
        (left_low,left_high,left_sum) = find_max_sub(l,low,mid)
        (right_low,right_high,right_sum) = find_max_sub(l,mid+1,high)
        (cross_low,cross_high,cross_sum) = maxSubarray(l,low,mid,high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low,left_high,left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)
        
# print(find_max_sub(l,0,len(l)-1))

def bruteforce(L):
    s,l=0,0
    start,end = 0,0
    for i in range(len(L)):
        for j in range(len(L)):
            s = 0
            for k in L[i:j]:
                s+=k
            if s >= l:
                l = s
                start,end = i,j
    return (start,end,l)

# print(bruteforce(l))

def square_matrix_multiplication(A,B):
    n = len(A)
    C = n*[len(A[0])*[0]]
    for i in range(n):
        for j in range(n):
            C[i][j] = 0
            for k in range(n):
                C[i][j] = C[i][j]+A[i][k]*B[k][j]
                
    return C

def square_matrix_multiplication_recursive(A,B):
    n = len(A)
    C = n*[len(A[0])*[0]]
    if n == 1:
        C[0][0]=A[0][0]*B[0][0]
    else:
        C[0][0] = square_matrix_multiplication_recursive(A[0][0],B[0][0]) + square_matrix_multiplication_recursive(A[0][1], B[1][0])
        C[0][1] = square_matrix_multiplication_recursive(A[0][0],B[0][1]) + square_matrix_multiplication_recursive(A[0][1],B[1][1])
        C[1][0] = square_matrix_multiplication_recursive(A[1][0],B[0][0]) + square_matrix_multiplication_recursive(A[1][1],B[1][0])
        C[1][1] = square_matrix_multiplication_recursive(A[1][0],B[0][1]) + square_matrix_multiplication_recursive(A[1][1],B[1][1])
        

# def merge(L,p,q,r):
#     # mid = len(L)//2
#     left = L[:q]
#     right = L[q:]
#     i,j=0,0
#     left.append(100)
#     right.append(100)
#     for k in range(p,r):
#         if left[i] <= right[j]:
#             L[k] = left[i]
#             i += 1 
#         else:
#             L[k] = right[j]
#             j += 1 
#     print(left,right)
        
# def merge_sort(L,p,r):
#     if p < r:
#         q = (p+r)//2
#         merge_sort(L,p,q)
#         merge_sort(L,q+1,r)
#         merge(L,p,q,r)
#     return L
# l = [2,5,3,1,4]
# print(merge_sort(l,0,len(l)))

def merge(left,right):
    l,r = 0,0
    res = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    
    while l < len(left):
        res.append(left[l])
        l += 1
    
    while r < len(right):
        res.append(right[r])
        r += 1
    print('res: ',res)
    return res
        

def merge_sort(l):
    if len(l) <= 1:
        return l
    else:
        mid = len(l)//2
        left = merge_sort(l[:mid])
        right = merge_sort(l[mid:])
        print('init: ',left,right)
        return merge(left,right)
        
l = [85,24,63,45,17,31,96,50,50]
# print(merge_sort(l))

def quicksort(L):
    if len(L) <2:
        return L
    else:
        s,e,l = [],[],[]
        res = []
        p = L[-1]
        for i in L:
            if i < p:
                s.append(i)
            elif i == p:
                e.append(i)
            else:
                l.append(i)
        
        smaller = quicksort(s)
        larger = quicksort(l)
        
        for i in smaller:
            res.append(i)
        
        for i in e:
            res.append(i)
        
        for i in larger:
            res.append(i)
        
        return res

print(quicksort(l))

        
        