# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 12:47:08 2023

@author: User
"""


class Transaction:
    def __init__(self, date: str, details: str, amount: int) -> None:
        self.date = date 
        self.details = details
        self.amount = amount 
        
    def __str__(self) -> str:
        return self.date+' '+self.details+' '+str(self.amount)
    
class Account:
    def __init__(self, name: str):
        self.name = name
        self.dr = []
        self.cr = []
        
    def setName(self, name):
        self.name = name
        
    def debit(self, transaction: Transaction):
        self.dr.append(transaction)
        
    def credit(self, transaction: Transaction):
        self.cr.append(transaction)
        
    def print_account(self):
        print(f'Name: {self.name}')
        print()
        print('Debit Side')
        for i in self.dr:
            print(i)
        print()
        print('Credit Side')
        for j in self.cr:
            print(j)



    

if __name__=='__main__':
    # t1 = Transaction('02/07/17', 'Furniture', 1200)
    # t2 = Transaction('05/07/17', 'Van', 6010)
    # t3 = Transaction('15/07/17', 'Trees', 1400)
    # t4 = Transaction('01/07/17', 'Capital', 15000)
    
    # a1 = Account('Bank account')
    # a1.debit(t4)
    # a1.credit(t1)
    # a1.credit(t2)
    # a1.credit(t3)
    
    # a1.print_account()
    
    def getAmount(keywords):
        for i in keywords:
            if i.isdigit():
                amount = str(i)
                return amount
            
    def getName(keywords):
        pass
    
    accounts = []
    stop = 'no'
    while stop == 'no':
        date = input('Enter the date: ')
        event = input('Enter the event: ')
        keywords = event.split()
        # print(keywords)
        amount = getAmount(keywords)
        account = Account('')
        if 'started' in keywords:
            a_name = 'Bank'
            details = 'Capital'
            t = Transaction(date, details, amount)
            account.setName(a_name)
            account.debit(t)
            accounts.append(account)
        elif 'bought' in keywords:
            for i in range(len(keywords)):
                if keywords[i] == 'bought':
                    details = keywords[i+1]
                    break 
            t = Transaction(date, details, amount)
            if 'cheque' in keywords:
                
                for i in accounts:
                    if i.name == 'Bank':
                        i.credit(t)
            else:
                name = getName(keywords)
                accounts.add(Account(name))
                        
        
        stop = input('Do you want to quit: ')
        
        
    for i in accounts:
        i.print_account() 
    
    
    
    
    
    
    
    
    
    
    
    
    