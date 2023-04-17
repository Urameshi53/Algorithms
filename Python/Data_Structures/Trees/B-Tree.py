# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 12:00:54 2022

@author: User
"""


class Node(object):
    def __init__(self, *args):
        self.keys = list(args)
        self.children = []
        self.leaf = True 
        
class BTree(object):
    def __init__(self):
        self.root = None 
        
    def search(self,key):
        x = self.root
        if x.keys[0] == key:
            return True
        if x.leaf == True:
            return False
        if k < x.children[0]:
            while x != None and x.key != key:
                x = x.
        