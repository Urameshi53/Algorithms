# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 13:19:13 2022

@author: User
"""

# Top-Down Method using factorial
d = {0:1,1:1}
def fact(n):
    if n not in d:
        d[n] = n*fact(n-1)
    return d[n]

print(fact(1000))

# Bottom-Up Method using factorial
def fact1(n):
    a = 1
    for i in range(2,n+1):
        a = a*i
    return a

# for i in range(5):
#     print(fact(i))
print(fact(10000))