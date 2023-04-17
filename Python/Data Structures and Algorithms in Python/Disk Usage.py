# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 12:20:11 2023

@author: User
"""

import os 

def disk_usage(path) -> int:
    '''
    Return the number of bytes used by a file/folder and any descendants.

    Parameters
    ----------
    path : str
        string representing the location path of file/folder.

    Returns
    -------
    int.

    '''
    
    total = os.path.getsize(path)               # account for direct usage 
    if os.path.isdir(path):                     # if this is a directory
        for filename in os.listdir(path):       # then for each child
            childpath = os.path.join(path, filename)    # compose full path to child
            total += disk_usage(childpath)      # add child's usage to total 
            
    print('{0:<7}'.format(total), path)         # descriptive output (optional)
    gb = total/1000000000
    print(gb)
    return total                        # return the grand total

print(disk_usage('C:\\Users\\User\\Desktop'))