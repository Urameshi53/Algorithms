# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 22:40:30 2022

@author: User
"""

class Node(object):
    def __init__(self, key):
        self.key = key
        self.next = None
        
class SLinkedList(object):
    def __init__(self):
        self.head = None 
        
    def insert(self, x):
        x.next = self.head
        self.head = x
        
    def printlist(self):
        x = self.head 
        while x != None:
            print(x.key)
            x = x.next
            
    def search(self, a):
        x = self.head 
        while x != None and x != a:
            x = x.next
        return x
            
    def delete(self, x):
        if x == self.head:
            self.head = x.next
            x.next = None
            return x
        p = None 
        r = self.head
        while r!=None and r != x:
            p = r
            r = r.next 
        p.next = r.next
        return r
            
s = SLinkedList()

a = Node('a')
b = Node('b')
c = Node('c')
s.insert(a)
s.insert(b)
s.insert(c)
s.delete(b)
s.printlist()

