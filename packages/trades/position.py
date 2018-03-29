'''
Created on 30 Nov 2017

@author: adil
'''
from datetime import datetime

class Position:
    '''
    A class representing the position a particular client has on a particular security
    '''
    
    DATE_FORMAT = '%Y/%m/%d'

    def __init__(self, symbol, quantity, acquisition_date, last_modification_date=""):
        '''
        Constructor
        '''
        self.symbol = symbol
        self.quantity = quantity
        self.acqisitionDate = acquisition_date
        self.lastModificationDate = ( acquisition_date if last_modification_date == "" else last_modification_date)
        
    def getSymbol(self):
        return self.symbol
    
    def getQuantity(self):
        return self.quantity
    
    def getLastModificationDate(self):
        return self.lastModificationDate
    
    def setLastModificationDate(self, value):
        self.lastModificationDate = value
    
    def getAcquisitionDate(self):
        return self.acqisitionDate
    
    def getCurrentValue(self):
        pass
    
    def __str__(self):
        return "%s|%d|%s|%s" % (self.symbol, self.quantity, 
                                datetime.strftime(self.acqisitionDate, Position.DATE_FORMAT), 
                                datetime.strftime(self.lastModificationDate, Position.DATE_FORMAT))