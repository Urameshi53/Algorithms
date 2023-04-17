# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 17:51:20 2022

@author: User
"""

class DAT(object):
    def __init__(self,size):
        self.items = [None] * size
        self.index = 0
        
    def search(self,k):
        return self.items[k]
    
    def insert(self,x):
        self.items[self.index] = x
        self.index += 1
        
    def delete(self, x):
        self.items[self.index] = None 
        self.index -= 1
        
D = DAT(5)
D.insert(10)
D.insert(23)
print(D.search(1))



