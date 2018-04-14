'''
Created on 13 Apr 2018

@author: Zahera
'''
from ui.abstractapp import Application
from trades.transaction import Transaction
from server.price import PriceServer
from server.alphavantage import Alphavantage


class Security(Application):
    '''
    classdocs
    '''
    
    instance = None
    symbol , name, sector, industry = ('','','', '') 
    

    @staticmethod
    def getInstance():
        if not Security.instance :
            config_file_name = Application.getConfigFileName()
            stocks_file_name = Application.getCompaniesFileName()
            Security.instance = Security(config_file_name, stocks_file_name)
        return Security.instance
    
    
    
    def __init__(self, config_file_name, stocks_file_name):
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
                self.securities[symbol] = {"SYMBOL": symbol, "NAME": name, "SECTOR": sector, "INDUSTRY": industry}
       
    


    def retrieveSecSymbol(self, companyName):
        #
        # A function retrieves a client the clients' dictionary based on client_id
        # raises an exception if client_id deos not exist
        #
        if companyName in self.securities :
            return self.securities[str(companyName)]
        else :
            print("company does not exist")
        
        
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
              
              
    ''' getters '''           
    @staticmethod
    def getSymbol() :
        return Security.symbol
    
    @staticmethod
    def getName() :
        return Security.name
    
    @staticmethod
    def getSector() :
        return Security.sector
    
    @staticmethod
    def getIndustry() :
        return Security.industry
    
    
    ''' Setters '''
    @staticmethod
    def setSymbol(newSymbol) :
        Security.symbol = newSymbol
    
    @staticmethod
    def setName(newName) :
        Security.name = newName 
           
    @staticmethod
    def setSector(newSector) :
        Security.sector = newSector    
        
    @staticmethod
    def setIndustry(newIndustry) :
        Security.industry = newIndustry
                
                
    
    
if __name__ == '__main__':
    pass
        