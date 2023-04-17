# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 12:44:06 2023

@author: User
"""

import urllib3
http = urllib3.PoolManager()
r = http.request('GET', 'http://httpbin.org/robots.txt')
print(r.status)
print(r.data)

import requests 
r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
print(r.status_code)
print(r.headers['content-type'])
print(r.text)
print(r.json())