# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 23:56:48 2022

@author: User
"""

class Node(object):
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None 
        self.parent = None 
        
class BinaryTree(object):
    def __init__(self):
        self.root = None
       
    def inorder(self, x):
        if x!=None:
            self.inorder(x.left)
            print(x.key)
            self.inorder(x.right)
            
    def search(self, x, k):
        if x == None or k == x.key:
            return x
        if k < x.key:
            return self.search(x.left, k)
        else:
            return self.search(x.right, k)
        
    def itersearch(self, x, k):
        while x != None and x.key != k:
            if k<x.key:
                x = x.left 
            else:
                x = x.right 
        return x
    
    def minimum(self,x):
        while x.left != None:
            x = x.left 
        return x
    
    def maximum(self,x):
        while x.right != None:
            x = x.right 
        return x
        
    def successor(self, x):
        if x.right != None:
            return self.minimum(x.right)
        y = x.parent
        while y != None and x == y.right:
            x = y
            y = y.parent 
        return y
    
    def predecessor(self, x):
        if x.left != None:
            return self.maximum(x.left)
        y = x.parent
        while y != None and x == y.left:
            x = y 
            y = y.parent 
        return y
    
    def insert(self, z):
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
            
    def transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != None:
            v.parent = u.parent 
            
    def delete(self, z):
        if z.left == None:
            self.transplant(z, z.right) 
        elif z.right == None:
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left 
            y.left.parent = y
            
    def treeDelete(self, z):
        x = None
        y = None 
        if z.left==None or z.right==None:
            y = z 
        else:
            y = self.successor(z)
        if y.left != None:
            x = y.left
        else:
            x = y.right 
        if x != None:
            x.parent = y.parent 
        if y.parent == None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        if y != z:
            z.key = y.key 
        
B = BinaryTree()
a = Node(15)
b = Node(6)
c = Node(18)
d = Node(3)
e = Node(7)
f = Node(17)
g = Node(20)
h = Node(2)
i = Node(4)
j = Node(13)
k = Node(9)

B.insert(a)
B.insert(b)
B.insert(c)
B.insert(d)
B.insert(e)
B.insert(f)
B.insert(g)
B.insert(h)
B.insert(i)
B.insert(j)
B.insert(k)
B.inorder(a)
# B.transplant(a,c)
# B.treeDelete(d)
# print(B.root.key)
B.delete(d)
B.inorder(a)
# print(B.root.key)
# print(B.root.key)
# B.inorder(b)
# print(B.root.right.key)
# print(b.right.key)
# B.search(r,1)
       
        
        
        
# MIT Recitation for Binary Trees
class Binary_Node:
    def __init__(A, x): # O(1)
        A.item = x
        A.left = None
        A.right = None
        A.parent = None # A.subtree_update(
        
    def subtree_iter(A):
        if A.left:  
            yield from A.left.subtree_iter()
        yield A 
        if A.right: 
            yield from A.right.subtree_iter()
        
    def subtree_first(A):
        if A.left: 
            return A.left.subtree_first()
        else:
            return A 
    
    def subtree_last(A):
        if A.right:
            return A.right.subtree_last()
        else:
            return A 
        
    def successor(A):
        if A.right:
            return A.right.subtree_first()
        while A.parent and (A is A.parent.right):
            A = A.parent 
        return A.parent 

    def predecessor(A):
        if A.left:
            return A.left.subtree_last() 
        while A.parent and (A is A.parent.left):
            A = A.parent 
        return A.parent 

    def subtree_insert_before(A, B): # O(h)
         if A.left:
             A = A.left.subtree_last()
             A.right, B.parent = B, A
         else:
             A.left, B.parent = B, A
         # A.maintain() # wait for R07!

    def subtree_insert_after(A, B): # O(h)
         if A.right:
            A = A.right.subtree_first()
            A.left, B.parent = B, A
         else:
             A.right, B.parent = B, A
             
    def subtree_delete(A): # O(h)
         if A.left or A.right: # A is not a leaf
             if A.left: B = A.predecessor()
             else: B = A.successor()
             A.item, B.item = B.item, A.item
             return B.subtree_delete()
         if A.parent: # A is a leaf
             if A.parent.left is A: A.parent.left = None
             else: A.parent.right = None
             # A.parent.maintain() # wait for R07!
         return A

    