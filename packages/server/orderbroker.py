'''
Created on 19 Apr 2018

@author: Zahera
'''
from trades.transaction import Transaction

class OrderBroker(object):
    '''
    classdocs
    '''

    def executeOrder(self, order):
        transaction = Transaction(order) 
        
        return transaction
    