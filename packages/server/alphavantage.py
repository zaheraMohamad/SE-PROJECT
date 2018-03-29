'''
Created on 25 Nov 2017

@author: adil
'''
import re
from pprint import pprint

from server.Server import MarketDataServer
from server.dataunavailable import DataUnavailableEx


class Alphavantage(MarketDataServer):
    '''
    A module representing a the Alphavantage Server class
    It builds the URL to point to Alphavantage domain.
    '''


    def __init__(self, config_fname):
        MarketDataServer.__init__(self, config_fname)
    
    
    def getURL (self):
        return self.path+"?function="+self.function+ \
            "&symbol="+self.symbol+ \
            "&interval="+self.interval+ \
            "&apikey="+self.apikey+ \
            "&datatype="+self.datatype
    
    def setFunction(self, function):
        self.function = function     
        
    def getPrices (self, market_data):
        for key in market_data:
            if key.startswith('Time Series') :
                return market_data[key]
        else :
            raise DataUnavailableEx
    
    def getLastRecordedDate(self, market_data):
        #pprint(market_data)
        if(market_data and 'Meta Data' in market_data) :
            last_refreshed = market_data['Meta Data']['3. Last Refreshed']
            
            #get the date part of the last refreshed dattime (first 10 characters)
            return last_refreshed[0:10]
        else :
            raise DataUnavailableEx("Price data not found")
