# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 09:11:12 2022

@author: User
"""

class Node(object):
    def __init__(self, key):
        self.key = key 
        self.parent = None 
        self.left = None 
        self.right = None 
        self.color = 'BLACK'
        
class RBTree(object):
    def __init__(self):
        self.root = None
        
        
    def inorder(self,x):
        if x != None:
            self.inorder(x.left)
            print(x.key)
            self.inorder(x.right)
            
    def preorder(self, x):
        if x != None:
            print(x.key)
            self.preorder(x.left)
            self.preorder(x.right)
        
    def leftRotate(self, x):
        y = x.right 
        x.right = y.left 
        if y.left != None:
            y.left.parent = x 
        y.parent = x.parent 
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y 
        else:
            x.parent.right = y
        y.left = x
        x.parent = y 
        
    def rightRotate(self, x):
        y = x.left 
        x.left = y.right 
        if y.right != None:
            y.right.parent = x
        y.parent = x.parent 
        if x.parent == None:
            self.root = y 
        elif x == x.parent.left:
            x.parent.left = y 
        else:
            x.parent.right = y 
        y.right = x
        x.parent = y
        
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
        z.color = 'RED'
        self.insertFixup(z)
        
    def insertFixup(self, z):
        while z.parent and z.parent.color == 'RED':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right 
                if y.color == 'RED':
                    z.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent 
                elif z == z.parent.right:
                    z = z.parent 
                    self.leftRotate(z)
                    z.parent.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    self.rightRotate(z.parent.parent)
            else:
                z.parent.color = 'BLACK'
                z.parent.parent.color = 'RED'
                self.rightRotate(z.parent.parent)
        self.root.color = 'BLACK'
        
    def transplant(self,u,v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v 
        else:
            u.parent.right = v 
        v.parent = u.parent 
        
        
        
R = RBTree()
a = Node(11)
b = Node(14)
c = Node(2)
d = Node(1)
e = Node(7)
f = Node(15)
g = Node(5)
h = Node(8)
# i = Node(4)

R.insert(a)
R.insert(b)
R.insert(c)
R.insert(d)
R.insert(e)
R.insert(f)
R.insert(g)
R.insert(h)
# R.insert(i)
# R.preorder(a)
print(R.root.left.right.key)
print(R.root.left.color)