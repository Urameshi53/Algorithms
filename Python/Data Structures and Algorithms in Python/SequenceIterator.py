# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 11:04:32 2023

@author: User
"""


class SequenceIterator:
    '''An iterator for any of Python's sequence types.'''
    
    def __init__(self, sequence) -> None:
        '''Create an iterator for the given sequence.'''
        self._seq = sequence    # keep a reference to the underlying data
        self._k = -1            # will increment to 0 on first call to next
        
    def __next__(self) -> any:
        '''Return the next element, or else raise StopIteration error.'''
        self._k += 1            # advance to next index
        if self._k < len(self._seq):
            return (self._seq[self._k]) # return to next index
        else:
            raise StopIteration()       # there are not more elements.
            
    def rnext(self):
        self._k = len(self._seq)-1
        if self._k >= 0:
            yield self._seq[self._k]
        else:
            raise StopIteration
            
            
    def __iter__(self):
        '''By convention, an iterator must return itself as an iterator.'''
        return self 
        
        
if __name__ == "__main__":
    s = SequenceIterator([1,2,3,4,5])
    for i in range(5):
        print(s.rnext())
        
        
        
        