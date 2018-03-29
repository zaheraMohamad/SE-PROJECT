'''
Created on 25 Nov 2017

@author: adil
'''
from server.Server import MarketDataServer

class YahooServer(MarketDataServer):
    '''
    A module representing a the Yahoo Server class
    It builds the URL to point to Yahoo domain.
    '''

    def __init__(self, config_fname):
        MarketDataServer.__init__(self, config_fname)
        
    def getURL (self):
        return self.path+self.symbol+"?interval="+self.interval
    
    def getLastRecordedDate(self, market_data):
        return ''
    
    def getPrices (self, market_data):
        mkt_data_fileds = market_data.keys()
        for field in mkt_data_fileds :
            if field.find('Time Series') :
                return market_data[field]