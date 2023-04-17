# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 10:38:47 2023

@author: User
"""

'''
Coding interview - Binary Search Successor
'''

class Node:
    def __init__(self, key: int):
        self.key = key 
        self.parent = None 
        self.right = None 
        self.left = None 
        

class BST:
    root: Node = None 
    
    def inorder_print(self,x=None) -> None:
        if x is not None:
            self.inorder_print(x.left)
            print(x.key)
            self.inorder_print(x.right)
    
    def search(self, key: int) -> bool:
        x = self.root 
        if x == None or key == x.key:
            return True
        if key < x.key:
            return self.search(x.left.key)
        else:
            return self.search(x.right.key)
        
    def search_iterative(self, k: int) -> Node:
        x = self.root
        while x != None and k != x.key:
            if k < x.key:
                x = x.left 
            else:
                x = x.right
        return x
    
    def insert(self, z: Node) -> None:
        y = None 
        x = self.root 
        while x != None:
            y = x 
            if z.key < x.key:
                x = x.left 
            else:
                x = x.right 
        z.parent = y 
        if y == None:
            self.root = z 
        elif z.key < y.key:
            y.left = z 
        else:
            y.right = z
        
        
    def minimum(self) -> Node:
        x = self.root 
        while x.left != None:
            x = x.left 
        return x
            
    def successor(self) -> Node:
        x = self.root 
        if x.right != None:
            return self.minimum(x.right)
        y = x.parent 
        while y != None and x == y.right:
            x = y 
            y = y.parent 
        return y
    
            
B = BST()
B.insert(Node(1))
B.insert(Node(2))
B.insert(Node(3))

# print(B.search(1))
B.inorder_print(Node(1))
