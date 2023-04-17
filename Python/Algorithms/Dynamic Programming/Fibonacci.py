# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 13:18:02 2022

@author: User
"""


# Dynamic Programming Top-Down Approach
l = {0:1,1:1}
def fib(n):
    if n not in l:
        l[n] = fib(n-1)+fib(n-2)
    return l[n]

# Bottom-Up Approach
def fib1(n):
    if n == 0:
        return 1
    else:
        p,c = 0,1
        for i in range(n):
            new = p+c
            p = c
            c = new
        return c
    
# for i in range(10000):
#     print(fib(i))
print(fib(100000))