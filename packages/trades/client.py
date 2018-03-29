'''
Created on 30 Nov 2017

@author: adil
'''
__all__ = ["Client", "ClientException"]
from trades.PositionException import PositionException

class ClientException (Exception) :
    """Client Error"""


class Client:
    '''
    A class representing a client holding a position
    '''


    def __init__(self, clientID, name, email) :
        '''
        Constructor
        '''
        self.name=name
        self.email=email
        self.clientID=clientID
        self.positions={}
    
    def getName(self) :
        return self.name
    
    def getID(self):
        return self.clientID
    
    def getPositions(self):
        return list(self.positions.values())
    
    def setName(self, name) :
        self.name = name
        
    def setEmail(self, email) :
        self.email = email
        

    def addPosition(self, position) :
        if self.hasPosition(position.getSymbol()) :
            currentPosition = self.positions[position.getSymbol()]
            currentPosition.quantity += position.getQuantity()
            currentPosition.setLastModificationDate(position.getLastModificationDate())
        else :
            self.positions[position.getSymbol()] = position
            
    def getPosition(self, symbol) :
        if self.hasPosition(symbol) :
            return self.positions[symbol]
        else :
            raise PositionException("Client does not hold position on this security")
        
    def hasPosition(self, symbol) :
        return True if symbol in self.positions else False
    
        
    def updatePositions(self, transacton):
        pass
        
    def __repr__(self):
        return str(self.__dict__)
    
    def __str__(self):
        positions = [ str(position) for position in self.positions.values() ]
        
        return "%d:%s:%s:%s" % (self.clientID, self.name, self.email, ",".join(positions)) 
    