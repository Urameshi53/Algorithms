# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 11:15:27 2023

@author: User
"""


class Range:
    '''A class that mimic's the built-in range class.'''
    
    def __init__(self, start: int, stop: int = None, step: int = 1) -> None:
        '''
        Initialize a Range instance.

        Parameters
        ----------
        start : TYPE
            Starting value or index.
        stop : TYPE, optional
            End value or index. The default is None.
        step : TYPE, optional
            Step value or amount. The default is 1.

        Returns
        -------
        None.

        '''
        if step == 0:
            raise ValueError('step cannot be 0')
            
        if stop is None:            # special case of range(n)
            start, stop = 0, start  # should be treated as if range(0,n)
            
        # calculate the effective length once 
        self._length = max(0, (stop - start + step - 1) // step)
        
        # need knowledge of start and step (but not stop) to support __getitem__ 
        self._start = start 
        self._step = step 
        
    def __len__(self) -> int:
        '''Return number of entries in the range'''
        return self._length 
    
    def __getitem__(self, k: int) -> int:
        '''Return entry at index k (using standard interpretation if negative).'''
        if k < 0:
            k += len(self)          # attempt to convert negative index 
            
        if not 0 <= k < self._length:
            raise IndexError('index out of range')
            
        return self._start + k * self._step 
    
if __name__=='__main__':
    pass
