# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 12:11:33 2023

@author: User
"""

from CreditCard import CreditCard 

class PredatoryCreditCard(CreditCard):
    '''An extension to CreditCard that compounds interest and fees.'''
    
    def __init__(self, customer, bank, acnt, limit, apr):
        '''
        Creates a new Predatory Credit Card instance.

        Parameters
        ----------
        customer : str
            the name of the customer (e.g. 'John Bowman')
        bank : str
            the name of the bank (e.g. 'Carlifornia Savings')
        acnt : str
            the account identifier (e.g. '5392 0236 8437 2935')
        limit : int
            credit limit (measured in dollars)
        apr : int
            annual percentage rate (e.g. 0.0825 for 8.25% APR)

        Returns
        -------
        None.

        '''
        
        super().__init__(customer, bank, acnt, limit)   # call super constructor 
        self._apr = apr 
        
    def charge(self, price: int) -> bool:
        '''
        Charge given price to the card, assuming sufficient credit limit.

        Parameters
        ----------
        price : int
            DESCRIPTION.

        Returns
        -------
        bool
            Return True if charge was processed.
            Return False and assess $5 fee if charge is denied.

        '''
        
        success = super().charge(price)         # call inherited method 
        if not success:
            self._balance += 5                  # assess penalty
        return success                          # caller expects return value
    
    def process_month(self):
        '''Assess monthly interest on outstanding balance.'''
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor.
            monthly_factor = pow(1+self._apr, 1,12) 
            self._balance *= monthly_factor 

















# c = CreditCard('John Bowman', 'Carlifornia Savings', '5391 0375 5309 9387', 2500)
# print(c.get_account())
# c.charge(2000)
# c.make_payment(100)
# print(c.get_balance())