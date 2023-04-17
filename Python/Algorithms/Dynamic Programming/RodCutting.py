# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 01:10:52 2022

@author: User
"""

def cutRod(p,n):
    if n == 0:
        return 0
    q = -1
    for i in range(1,n):
        q = max(q, p[i]+cutRod(p,n-i))
        print(p[i])
    return q

p = [1,5,8,9,10,17,17,20,24,30]

# print(cutRod(p, 2))
# for i in range(10):
#     print(i,cutRod(p,i))

def helper(p,n,r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0 
    else:
        q = -1
        for i in range(1,n):
            q = max(q,p[i]+helper(p, n-i, r))
    r[n] = q
    return q
            
def mCutRod(p,n):
    r = [0]*(n+1)
    for i in range(1,n):
        r[i] = 0
    return helper(p,n,r)

print(mCutRod(p,4))