# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 22:41:08 2022

@author: User
"""

import DLinkedList as D
import CDLinkedList as C
import Node as N

a = N.Node('a')
b = N.Node('b')
c = N.Node('c')

d = D.DLinkedList()
d.insert(a)
d.insert(b)
d.insert(c)

cir = C.CDLinkedList()
cir.insert(a)
cir.insert(b)
cir.insert(c)

cir.printlist()
