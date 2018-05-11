'''
Created on 16 Apr 2018

@author: Zahera
'''
__all__ = ["Security", "SecurityException"]


class SecurityException (Exception) :
    """Client Error"""
    
    
class Security:
    '''
    classdocs
    '''
    symbol , name, sector, industry = ('','','', '') 
        

    def __init__(self, symbol, name, sector, industry):
        '''
        Constructor
        '''
        self.symbol = symbol
        self.name = name
        self.sector = sector
        self.industry = industry
        
        
               
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
        
          
    def __repr__(self):
        return str(self.__dict__)
    
    def __str__(self):
        return "%s:%s:%s:%s" % ("SYMBOL= " + self.symbol, "  NAME= " + self.name, "  SECTOR= " + self.sector, "  INDUSTRY= " + self.industry) 
    
                
                
    