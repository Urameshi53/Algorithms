# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 15:58:18 2022

@author: User
"""

def binarySearch(L, x, begin=0, end=0):
    begin=0
    end=len(L)-1
    mid = (begin+end)//2
    if x<L[begin] or x>L[end]:
        return False
    if L[mid] == x:
        return True
    if len(L)==0:
        return False
    else:
        if L[mid] > x:
            end = mid+1
            return binarySearch(L,x,begin,end)
        else:
            begin = mid-1
            return binarySearch(L,x,begin,end)
        
l = [4,6,7,18,20,22,25,27]
print(binarySearch(l,10))
        