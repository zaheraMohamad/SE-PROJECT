'''
Created on 16 Apr 2018

@author: Zahera --
'''

from ui.abstractapp import Application

from server.price import PriceServer
from server.alphavantage import Alphavantage
from trades.security import Security
from trades.transaction import Transaction
from trades.security import SecurityException

class SecurityManager(Application):
    '''
    classdocs
    '''
    instance = None    
    symbol , name, sector, industry = (Security.getSymbol(),Security.getName(),Security.getSector(), Security.getIndustry()) 

    @staticmethod
    def getInstance():
        if not SecurityManager.instance :
            config_file_name = Application.getConfigFileName()
            stocks_file_name = Application.getCompaniesFileName()
            SecurityManager.instance = SecurityManager(config_file_name, stocks_file_name)
        return SecurityManager.instance

    def __init__(self,  config_file_name, stocks_file_name):
        '''
        Uses the (tab delimited) stocks file to retrieve securities details
        '''
        
        self.price_srvr = PriceServer(Alphavantage(config_file_name))        
  
        self.securities = {}

        with open(stocks_file_name, "r") as securities_file :
            #First read the line containing the header
            securities_file.readline()
            for line in securities_file :
                line = line.rstrip()
                symbol, name, sector, industry = line.split("\t")
                sec = Security(symbol, name, sector, industry)
                self.securities[symbol] = sec
       
                
               
    
    def retrieveSecSymbol(self, companyName):
        #
        # A function retrieves a client the clients' dictionary based on client_id
        # raises an exception if client_id deos not exist
        #
        if companyName in self.securities :
            return self.securities[str(companyName)]
        else :
            raise SecurityException("company does not exist")
        
        
     
    def getCurrentMarketValue(self,symbol): 
        # A function return current market value
        
        current_value = self.price_srvr.getLastRecordedPriceBySymbol(symbol.upper())  
        return current_value
       

    def checkSecurityBySymbol(self, symbol):
        """Returns true f symbol exists"""
        
        return True if symbol in self.securities else False
    
    
    def checkSymbolBySecurity(self, companyName):
        """Returns true f symbol exists"""
        
        return True if companyName in self.securities else False
    
    def getSecurityInfoBySymbol(self, symbol):
        """Returns a dictionary of security details containing "SYMBOL", "NAME", "SECTOR" and "INDUSTRY" """
        
        return self.securities[symbol] if symbol in self.securities else None
    
    
    def listSecurities(self):
        for secList in self.securities.values() :
            print(str(secList))
            
   
  
if __name__ == '__main__':
    pass
        