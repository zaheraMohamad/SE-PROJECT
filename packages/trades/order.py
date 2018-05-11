'''
Created on 30 Nov 2017

@author: adil
'''
import enum

class OrderStatus(enum.IntEnum):
    OPEN = 0
    SUBMITTED = 1
    FULFILLED = 2
    PARTIAL = 3
    KILLED = 4
    O = OPEN
    S = SUBMITTED
    F = FULFILLED
    P = PARTIAL
    K = KILLED
globals().update(OrderStatus.__members__)

class TransType(enum.IntEnum):
    BUY = 0
    SELL = 1
globals().update(TransType.__members__)

class Order:
    '''
    A class representing a client order to be executed; 
    when it is executed it will be turned into a transaction.
    An order could be in one of statuses 
    (open, submitted, fulfilled, partially fulfilled, or killed)
    '''


    def __init__(self, client_id, symbol, trans_type, quantity, ask_price):
        '''
        Constructor
        '''
        self.__client_id = client_id
        self.__symbol = symbol
        self.__trans_type = trans_type
        self.__quantity = quantity
        self.__ask_price = ask_price
        self.__status = OrderStatus.OPEN

    def getClientID(self):
        return self.__client_id


    def getSymbol(self):
        return self.__symbol

    def getTrans_type(self):
        return self.__trans_type


    def getQuantity(self):
        return self.__quantity


    def getAsk_price(self):
        return self.__ask_price


    def getStatus(self):
        return self.__status

    def setStatus(self, status):
        self.__status = status
        
    def setQuantity(self, value):
        self.__quantity = value


    def setAsk_price(self, value):
        self.__ask_price = value  
    