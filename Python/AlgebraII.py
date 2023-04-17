 # -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 00:11:30 2022

@author: User
"""



def bisectionSearch(n,a=1,b=2, epsilon=0.00001):
    ans = 1
    while abs(ans-b) > epsilon:
        ans = (a+b)/2
        a,b=b,ans
    return ans

print(4)
         