'''
module server.Server
Created on 24 Nov 2017

@author: adil
'''
from abc import ABCMeta, abstractmethod

import requests
import sys

class MarketDataServer(metaclass=ABCMeta)  :
    """A ChartServer class
        to create an object use the code:
            from Server use ChartServer
            obj = MarketDataServer (configfile)
        where configfile is the name of the config file containing the server's
        path, symbol and interval specification
    """
    
    """    The constructor uses a config file to read the server's 
           fields and values (separated by a '=' char)
    """
    def __init__ (self, config_fname):
        self.conf_file = open (config_fname, "r")
        
        for line in self.conf_file :
            line=line.strip()
            (key, value) = line.split("=")
            self.__dict__[key] = value
        self.conf_file.close()
    
    def setSymbol(self, symbol):
        self.symbol = symbol
    
    def setInterval(self, interval):
        self.interval = interval
        
    @abstractmethod
    def getURL (self):
        pass
    
    @abstractmethod
    def getPrices (self, market_data):
        pass
    
    @abstractmethod
    def getLastRecordedDate(self, market_data):
        pass
        
    def getDataAsText(self):
        url = self.getURL()
        return requests.get(url).text
    
    def getDataAsJSON(self) :
        url = self.getURL()
        return requests.get(url).json()
    
        