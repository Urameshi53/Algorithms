# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 22:37:39 2022

@author: User
"""

class Node(object):
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None