# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 13:16:40 2022

@author: User
"""

# def quicksor1t(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]
#         greater = [i for i in array[1:] if i > pivot]
#         return quicksort(less) + [pivot] + quicksort(greater)
    
def partition(l,p,r):
    x = l[r]
    i = p-1
    for j in range(p,r):
        if l[j] <= x:
            i = i + 1
            l[i],l[j]=l[j],l[i]
            # print(l,i,j,l[i],l[j])
            
    l[i+1],l[r]=l[r],l[i+1]
    print('Ends',l)
    return i+1    
    
def quicksort(l,p,r):
    if p < r:
        q = partition(l,p,r)
        quicksort(l,p,q-1)
        quicksort(l,q+1,r)
    return l
        
l = [5,3,1,4,2]
k = [2,8,7,1,3,5,6,4]
m = [85,24,63,45,17,31,96,50]
# print(quicksort(k,0,len(k)-1))

def quick_sort(l):
    if len(l) <= 1:
        return l
    else:
        p = l[-1]
        f,s,t = [],[],[]
        res = []
        for i in l:
            if i < p:
                f.append(i)
            elif i == p:
                s.append(i)
            else:
                t.append(i)
                
        first = quick_sort(f)
        third = quick_sort(t)
        print(first,third)
        for i in first:
            res.append(i)
        for i in s:
            res.append(i)
        for i in third:
            res.append(i)
        return res 
    
print(quick_sort(m))
