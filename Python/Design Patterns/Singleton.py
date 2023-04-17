# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 15:07:43 2023

@author: User
"""

'''
// The Database class defines the `getInstance` method that lets
// clients access the same instance of a database connection
// throughout the program.
class Database is
    // The field for storing the singleton instance should be
    // declared static.
    private static field instance: Database

    // The singleton's constructor should always be private to
    // prevent direct construction calls with the `new`
    // operator.
    private constructor Database() is
        // Some initialization code, such as the actual
        // connection to a database server.
        // ...

    // The static method that controls access to the singleton
    // instance.
    public static method getInstance() is
        if (Database.instance == null) then
            acquireThreadLock() and then
                // Ensure that the instance hasn't yet been
                // initialized by another thread while this one
                // has been waiting for the lock's release.
                if (Database.instance == null) then
                    Database.instance = new Database()
        return Database.instance

    // Finally, any singleton should define some business logic
    // which can be executed on its instance.
    public method query(sql) is
        // For instance, all database queries of an app go
        // through this method. Therefore, you can place
        // throttling or caching logic here.
        // ...

class Application is
    method main() is
        Database foo = Database.getInstance()
        foo.query("SELECT ...")
        // ...
        Database bar = Database.getInstance()
        bar.query("SELECT ...")
        // The variable `bar` will contain the same object as
        // the variable `foo`.
'''

'''---Naive Singleton---'''
# class SingletonMeta(type):
#     '''
#     The Singleton class can be implemented in different ways in Python. Some
#     possible methods include: base class, decorator, metaclass. We will use 
#     the metaclass because it is best suited for this purpose.
#     '''
    
#     _instances = {}
    
#     def __call__(cls, *args, **kwargs):
#         '''
#         Possible changes to the value of the `__init__` argument do not affect
#         the returned instance.
#         '''
#         if cls not in cls._instances:
#             instance = super().__call__(*args, **kwargs)
#             cls._instances[cls] = instance 
#         return cls._instances[cls] 
    
# class Singleton(metaclass=SingletonMeta):
#     def some_business_logic(self):
#         '''
#         Finally, any singleton should define some business logic, which can be 
#         executed on its instance.
#         '''
        
#         # ...
        
        
# if __name__=='__main__':
#     # The client code.
    
#     s1 = Singleton()
#     s2 = Singleton()
    
#     if id(s1) == id(s2):
#         print('Singleton works, both variables contain the same instance.')
#     else:
#         print('Singleton failed, variables contain different instances.')
    
    
'''---Thread-Sage Singleton---'''
from threading import Lock, Thread 


class SingletonMeta(type):
    '''This is a thread-safe implementation of Singleton.'''
    
    _instances = {}
    
    _lock: Lock = Lock()
    
    '''
    We now have a look object that will be used to synchronize threads 
    during first access to the Singleton.
    '''
    
    def __call__(cls, *args, **kwargs):
        ''' 
        Possible changes to the value of the `__init__` argument do not 
        affect the returned instance.
        '''
        
        '''
        Now, imagine that the program has just been launched. Since 
        there's no Singleton instance yet, multiple threads can 
        simultaneously pass the previous conditional and reach this 
        point almost at the same time. The first of them will acquire
        lock and will proceed further, while the rest will wait here.
        '''
        with cls._lock: 
            ''' 
            The first thread to acquire the lock, reaches this conditional, 
            goes inside and creates the Singleton instance. Once it leaves 
            the lock block, a thread that might have been waiting for the 
            lock realease may then enter this section. But since the 
            Singleton field is already initialized, the thread won't create
            a new object.
            '''
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance 
        return cls._instances[cls] 
    
    
class Singleton(metaclass=SingletonMeta):
    value: str = None 
    '''We'll use this property to prove that our Singleton really works.'''
    
    def __init__(self, value: str) -> None:
        self.value = value 
        
    def some_business_logic(self):
        ''' 
        Finally, any singleton should define some business logic, which can 
        be executed on its instance.
        '''
        
        
def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)
    
    
if __name__ == '__main__':
    # The client code 
    
    print("If you see the same value, then Singleton was reused (yay!) \n"
          "If you see different values, then 2 singletons were created (boo!)\n\n"
          "RESULT:\n")
    
    process1 = Thread(target=test_singleton, args=("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))
    process1.start()
    process2.start()


