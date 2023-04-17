# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 12:19:31 2023

@author: User
"""

import os
import shutil

os.stat('C:\\Users\\User\\Desktop\\Learning Materials\\Software Engineering by Somerville.pdf')

path = 'C:\\Users\\User\\Desktop'


def printfs(path):
    with os.scandir(path) as it:
        for entry in it:
            # if entry.name.endswith('.pdf'):
            if entry.is_file():
                print(entry.name)
            else:
                printfs(path+ '\\' +entry.name)

def printvfs(path, filetype):
    try:
        with os.scandir(path) as it:
            for entry in it:
                # if entry.name.endswith('.pdf'):
                if entry.name.endswith(filetype):
                    print(entry.name)
                elif entry.is_file():
                    pass
                else:
                    printvfs(path+ '\\' +entry.name, filetype)
    except PermissionError:
        pass
    
def copyfiles():
    environ = os.environ
    dst = environ['USERPROFILE']
    os.mkdir(dst)
    try:
        with os.scandir(path) as it:
            for entry in it:
                if entry.name.endswith('.pdf'):
                    shutil.copyfile(entry.path,dst)
                elif entry.is_file():
                    pass
                else:
                    copyfiles()
    except PermissionError:
        pass
    
    

environ = os.environ
user_profile = environ['USERPROFILE']
# print(user_profile)
printvfs(user_profile, '.pdf')








