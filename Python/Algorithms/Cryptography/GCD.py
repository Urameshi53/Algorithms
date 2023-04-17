# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 14:34:18 2022

@author: User
"""

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
    
print(gcd(3,11))