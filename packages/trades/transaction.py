'''
Created on 30 Nov 2017

@author: adil
'''
from datetime import datetime

from packages.trades.order import Order, OrderStatus, TransType
from packages.ui.clientmanager import ClientManager
from packages.trades.position import Position


class TransactionError(Exception):
    """
    Transaction Error; buy or sell order cannot be completed
    """

class Transaction:
    '''
    classdocs
    '''
    DATE_FORMAT = '%Y-%m-%d %H:%M:%S.%f'    #2018-02-22 15:17:24.617547

    def __init__(self, order = ""):
        '''
        Constructor
        '''
        if order == "" :
            return
        
        elif order.getStatus() == OrderStatus.OPEN :
            self.__clientID = int(order.getClientID())
            self.__symbol = order.getSymbol()
            self.__trans_type = order.getTrans_type()
            self.__quantity = int(order.getQuantity())
            self.__price = float(order.getAsk_price())
            self.__date = datetime.now()
            
            # change the status of order to reflect that is has been submitted
            order.setStatus(OrderStatus.SUBMITTED)
        else :
            raise TransactionError ("Order is not valid")

    def get_quantity(self):
        return self.__quantity


    def set_quantity(self, value):
        self.__quantity = value


    
    def commit(self):
        client = ClientManager.getInstance().retrieveClient(str(self.clientID))
        
        if self.trans_type == TransType.BUY :
            new_position = Position(self.symbol, int(self.quantity), datetime.now())
            
        elif self.trans_type == TransType.SELL :
            new_position = Position(self.symbol, -int(self.quantity), datetime.now())
            
        else :
            raise TransactionError("Some thing weird happened, UNKNOWN order type")
            
        client.addPosition(new_position)
        
 
    def get_client_id(self):
        return self.__clientID


    def set_client_id(self, value):
        self.__clientID = value

    def get_symbol(self):
        return self.__symbol


    def get_trans_type(self):
        return self.__trans_type



    def get_price(self):
        return self.__price


    def get_date(self):
        return self.__date

    def set_symbol(self, value):
        self.__symbol = value


    def set_trans_type(self, value):
        self.__trans_type = value


    def set_price(self, value):
        self.__price = value


    def set_date(self, value):
        self.__date = value
    
    
    def __repr__(self):
        return str(self.__dict__)
    
    def __str__(self):        
        return "%s|%d|%d|%s|%.4f|%d" % (self.date, self.clientID, self.trans_type, self.symbol, self.price, self.quantity) 
    
    #===========================================================================
    # Properties definition
    #===========================================================================
    symbol = property(get_symbol, set_symbol, None, None)
    trans_type = property(get_trans_type, set_trans_type, None, None)
    quantity = property(get_quantity, set_quantity, None, None)
    price = property(get_price, set_price, None, None)
    date = property(get_date, set_date, None, None)
    clientID = property(get_client_id, set_client_id, None, None)
    quantity = property(get_quantity, set_quantity, None, None)
    
 
def go():
    (client, symbol, trans_type, quantity, ask_price) = (1, 'GOOG', TransType.BUY, 20, 99.999)
    order = Order(client, symbol, trans_type, quantity, ask_price)   
    
    trx = Transaction(order)
    
    print(trx)
    
if __name__ == '__main__' :
    go()
    
    