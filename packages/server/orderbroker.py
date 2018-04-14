'''
Created on 20 Feb 2018

@author: adil
'''

from trades.transaction import Transaction
from ui.Security import Security



    
class OrderBroker(object):
    '''
    A singleton class representing an order broker system
    '''

    instance = None
    

    @staticmethod
    def getInstance():
        return Security.getInstance()
    
    def __init__(self):
        '''
        Uses the (tab delimited) stocks file to retrieve securities details
        '''
        OrderBroker.getInstance()
    

        
    def executeOrder(self, order):
        transaction = Transaction(order) 
        
        return transaction
    
    
if __name__ == '__main__' :
    pass
    