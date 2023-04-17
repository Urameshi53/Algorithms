# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 22:40:45 2023

@author: User
"""


class CreditCard:
    '''A consumer credit card.'''
    
    def __init__(self, customer: str, bank: str, acnt: str, limit: int):
        '''
        Creates a new credit card instance.

        Parameters
        ----------
        customer : str
            The name of the Customer (e.g. 'John Bowman')
        bank : str
            The name of the bank (e.g. 'Carlifornia Savings').
        acnt : str
            The account identifier (e.g '5391 0375 9387 5309').
        limit : int
            Credit limit (measured in dollars).

        Returns
        -------
        None.

        '''
        
        self._customer = customer 
        self._bank = bank 
        self._account = acnt 
        self._limit = limit 
        self._balance = 0 
        
    def get_customer(self) -> str:
        '''Return name of the customer.'''
        return self._customer 
        
    def get_bank(self) -> str:
        '''Return the bank's name.''' 
        return self._bank 
        
    def get_account(self) -> str:
        '''Return the card identifying number (typically stored as as string)'''
        return self._account 
    
    def get_limit(self) -> int:
        '''Return current credit limit.'''
        return self._limit 
        
    def get_balance(self) -> int:
        '''Return current balance.'''
        return self._balance 
        
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
        Return True if charges was processed; False if charges was denied.

        '''
        if price + self._balance > self._limit:     # if charge would exceed limit.
            return False 
        else:
            self._balance += price 
            return True 
            
    def make_payment(self, amount: int) -> None:
        '''Process customer payment that reduces balance.'''
        self._balance -= amount 
            
            
            
            
# emma = CreditCard('Zigah Emmanuel', 'ADB', '5000 0239 3845 2938', 1000)
# print(emma.get_account())
# emma.charge(500)
# print(emma.get_balance())

if __name__ == '__main__':
    # wallet = [] 
    # wallet.append(CreditCard('John Bowman', 'Carlifornia Savings', '5391 0375 5309 9387', 2500))
    # wallet.append(CreditCard('John Lennox', 'Carlifornia Federal', '3485 0399 3395 1954', 3500))
    # wallet.append(CreditCard('Lancelot Finch', 'Carlifornia Finance', '5391 0375 9387 5309', 5000))
    
    # for val in range(1,17):
    #     wallet[0].charge(val)
    #     wallet[1].charge(val*2)
    #     wallet[2].charge(val*3)
        
    # for c in range(3):
    #     print('Customer = ', wallet[c].get_customer())
    #     print('Bank = ', wallet[c].get_bank())
    #     print('Account = ', wallet[c].get_account())
    #     print('Limit = ', wallet[c].get_limit())
    #     print('Balance = ', wallet[c].get_balance())
    #     while wallet[c].get_balance() > 100:
    #         wallet[c].make_payment(100)
    #         print('New balance = ', wallet[c].get_balance())
    #     print()
    pass



 