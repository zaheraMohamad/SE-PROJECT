'''
Created on 16 Apr 2018

@author: Zahera
'''
from packages.ui.abstractapp import Application
from packages.server.price import PriceServer
from packages.server.alphavantage import Alphavantage
from packages.trades.security import Security
from packages.trades.transaction import Transaction
from packages.trades.security import SecurityException

class SecurityManager(Application):
    '''
    classdocs
    '''
    instance = None    

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
            securities_file.readline()
            for line in securities_file :
                line = line.rstrip()
                stocks_symbol, stocks_name, stocks_sector, stocks_industry = line.split("\t")
                self.securities[stocks_symbol] = {Security(stocks_symbol, stocks_name, stocks_sector, stocks_industry)}
               
    
    def retrieveSecSymbol(self, companyName):
        #
        # A function retrieves a client the clients' dictionary based on client_id
        # raises an exception if client_id deos not exist
        #
        if companyName in self.securities :
            return self.securities[str(companyName)]
        else :
            raise SecurityException("company does not exist")
        
        
    def queryPrice(self, symbol) :
        #
        # A function querying a security's price from Price Server
        # An Data_Unavailable_Ex may be thrown
        #
        price = self.price_srvr.getLastRecordedPriceBySymbol(symbol.upper())
        return price

     
     
    def getCurrentMarketValue(self):
        
        symbol = self._promptForSymbol()   
        sec_price = self.queryPrice(symbol)
           
        print("Last recorded price for security %s is %s" %(symbol, sec_price))
        
        
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
        for securityList in self.securities.values() :
            print(str(securityList))
          
          
    def executeOrder(self, order):
        transaction = Transaction(order) 
        return transaction      
    
if __name__ == '__main__':
    pass
        