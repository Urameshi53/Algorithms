# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 23:14:36 2021

@author: User
"""



class Year(object):
    def __init__(self, year,start):
        self.year = year
        self.d = {'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30,
     'July':31, 'August':31, 'September':30, 'October':31, 'November':30, 'December':31}
        self.start = start
        
    def print_days(self,m,n=0):
        print('Mon\tTue\tWed\tThu\tFri\tSat\tSun')
        for i in range(1,m+1+n):
            if i-n <1:
                print('\t', end='')
            elif i%7!=0:
                print(i-n,'\t',end='')
            else:
                print(i-n)
            
        return ''
    
    def print_mdays(self, m,num):
        print('Mon\tTue\tWed\tThu\tFri\tSat\tSun')
        num=num.lower()
        if num == 'mon':
            n=0
        elif num == 'tue':
            n=1
        elif num == 'wed':
            n=2
        elif num == 'thur':
            n=3
        elif num == 'fri':
            n=4
        elif num == 'sat':
            n=5
        else:
            n=6
        for i in range(1,m+1+n):
            if i-n <1:
                print('\t', end='')
            elif i%7!=0:
                print(i-n,'\t',end='')
            else:
                print(i-n)
            
        return ''
    
    def print_month(self,month):
        d1=list(self.d)
        # print(d1)
        
        a,b=0,0
        b = self.start
        a=b
        if self.year%4==0:
            self.d['February']=29
        # print(self.year)
        for i in range(len(d1)):
            if d1[i]==month:
                print('\n\t\t'+d1[i])            
                print(self.print_days(self.d[d1[i]],b))
            a+=self.d[d1[i]]
            b=a%7
            
        return ''
        
    
    def print_year(self):
        d1=list(self.d)
        # print(d1)
        
        a,b=0,0
        b = self.start
        a=b
        if self.year%4==0:
            self.d['February']=29
        # print(self.year)
        for i in range(len(d1)):
            print('\n\t\t'+d1[i])            
            print(self.print_days(self.d[d1[i]],b))
            a+=self.d[d1[i]]
            b=a%7
        
        
        
    # print('\n\t\t'+d1[0])    
    # print(print_days_1(d['January'],'Sun'))
    # print('\n\t\t'+d1[1])
    # print(print_days_1(d['February'],'Wed'))
    # print('\n\t\t'+d1[2])
    # print(print_days_1(d['March'],'wed'))
this_year = Year(2023,6)
print(this_year.print_year())
# print(this_year.print_month('June'))