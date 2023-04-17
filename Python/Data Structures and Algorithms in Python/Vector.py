# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 10:46:24 2023

@author: User
"""

class Vector:
    '''Represent a vector in a multidimensional space.'''
    
    
    def __init__(self, d: int):
        '''Create d-dimensional vector of zeros.'''
        self._coords = [0] * d 
        
    def __len__(self) -> int:
        '''Return the dimension of the vector.'''
        return len(self._coords)
    
    def __getitem__(self, j: int) -> int:
        '''Return jth coordinate of vector.'''
        return self._coords[j]
    
    def __setitem__(self, j: int, val: int) -> None:
        '''Set jth coordinate of vector to given value.'''
        self._coords[j] = val 
        
    def __add__(self, other):
        '''Return sum of two vectors.'''
        if len(self) != len(other):     # Relies of __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __eq__(self, other):
        '''Return True if vector has same coordinates as other.'''
        return self._coords == other._coords
    
    def __ne__(self, other):
        '''Return True if vector differs from other.'''
        return not self == other 
    
    def __str__(self):
        '''Produce string representation of vector.'''
        return '<' + str(self._coords)[1:-1] + '>'      # adapt list representation
    
    
if __name__=='__main__':
    v = Vector(3)
    u = Vector(3)
    for i in range(1,len(v)+1):
        v[i-1] = i<<2
    for i in range(1,len(u)+1):
        u[i-1] = 3<<i
    print(v,u)
    print(v+u)
    
    
    
    
    
    