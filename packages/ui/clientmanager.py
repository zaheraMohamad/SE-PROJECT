'''
Created on 18 Feb 2018

@author: adil
'''
import sys
import re
from datetime import datetime

from ui.abstractapp import Application

from trades.client import Client
from trades.position import Position

from trades.PositionException import PositionException
from server.dataunavailable import DataUnavailableEx
from trades.client import ClientException
import pandas as pd
from unittest.mock import inplace
from pandas.tests.io.parser import skiprows



class ClientManager(Application):
    '''
    A singleton Class simulating a menu-driven client application 
    '''
    
    instance = None
    

    @staticmethod
    def getInstance():
        if not ClientManager.instance :
            ClientManager.instance = ClientManager(Application.getClientsFileName())
        return ClientManager.instance
    
    def __init__(self, clients_file_name):
        '''
        Constructor
        '''
        
        self.clients_file_name = clients_file_name 
        
        self.clients = {}
        
        self.last_client_id = 0;
        
        with open(self.clients_file_name, "r") as clients_file :
            self.last_client_id = int(clients_file.readline())
            for line in clients_file :
                line = line.rstrip()
                
                (clt_id, clt_name, clt_email, clt_pos) = line.split(":")
                client = Client(int(clt_id), clt_name, clt_email)
                if len(clt_pos) > 0 :
                    positions = clt_pos.split(",")
                    for position in positions :
                        (symbol, qty, acq_date, mod_date) = position.split("|")
                        client.addPosition(Position(symbol, int(qty),
                                                    datetime.strptime(acq_date, Position.DATE_FORMAT).date(),
                                                    datetime.strptime(mod_date, Position.DATE_FORMAT).date()
                                                    )
                                            )
                    
                self.clients[clt_id] = client
                #The next line was removed because last id is now saved in the file
                #self.last_client_id = (client.getID() if client.getID() > self.last_client_id else self.last_client_id)
    
    #===========================================================================
    # def queryPrice(self, symbol) :
    #     #
    #     # A function querying a security's price from Price Server
    #     # An Data_Unavailable_Ex may be thrown
    #     #
    #     price = self.price_srvr.getLastRecordedPriceBySymbol(symbol.upper())
    #     return price
    #===========================================================================
     
    def newClient(self):
        client_name = input ("Please enter the client's name: ")
        client_email = input ("Please enter the client's email address: ")
         
        if client_email.find("@") >= 0 :
            self.last_client_id += 1
            my_client = Client(self.last_client_id, client_name, client_email)
            self.clients[str(my_client.getID())] = my_client
            return my_client
        else :
            raise ClientException ("Client cannot be created; invalid email address")

    def listClients(self):
        #represent of data frames stretch across page
        pd.set_option('expand_frame_repr',False)
        clientDataset= pd.read_csv(self.clients_file_name,skiprows=1,delimiter=":",header=None,
                    names=["ID","Name","Email","Symbol"],index_col="ID",na_filter=False)
        print(clientDataset)
       
        
        
            
    def saveClients(self):
        with open(self.clients_file_name, "w") as clients_file :
            clients_file.write("%d\n" % self.last_client_id)
            for clt_id in sorted(self.clients.keys()) :
                clients_file.write(str(self.clients[clt_id]) + "\n")
                
    def retrieveClient(self, client_id):
        #
        # A function retrieves a client the clients' dictionary based on client_id
        # raises an exception if client_id deos not exist
        #
        if client_id in self.clients :
            return self.clients[str(client_id)]
        else :
            raise ClientException("Client does not exist")
        
    def removeClient(self, client_id):
        client = self.retrieveClient(client_id)
        return self.clients.pop(str(client.getID()))


    def modifyClient(self, client_id):
        client = self.retrieveClient(client_id)
        print ("You have asked to change the details of the client: ", client)
        response = input ("Do you want to change the name [y,n]? ")
        if re.search(r"^[yY]", response) :
            name = input ("Please enter a new name: ")
            client.setName(name)
            
        response = input ("Do you want to change the email [y,n]? ")
        if re.search(r"^[yY]", response) :
            email = input ("Please enter a new email: ")
            client.setEmail(email)
                
        return client
     
        
    def queryClientPosition(self, client_id, symbol):
        #
        # For a retrieved client return the position held for a specific security (symbol)
        # It may raise the PositionException
        #
        client = self.retrieveClient(client_id)
        return client.getPosition(symbol)
    
    
    def listAllClientPositions(self, client_id):
        #
        # For a retrieved client return the position held for a specific security
        #
        client = self.retrieveClient(client_id)
        positions = client.getPositions()
        if not positions :
            print ("Client %s holds no positions!" % client.getName())
        else :
            print ("Client %s holds the following positions:" % client.getName())
            for position in positions :
                print ("%d stocks of %s" % (position.getQuantity(), position.getSymbol()))
                
    
    def _menu(self):
        print("""Client's Manager Menu
            Please choose an option: 
            1:    List all clients.
            2:    Create a new client.
            3:    Remove a client.
            4:    Modify a client.
            5:    Query a client's position.
            6:    List all client's positions
            0:    Return to Main Menu
            """)
        try :
            return int(input("Enter your choice: "))
        except ValueError :
            return ""
        
        
    def _menu0(self):
        pass
    
    
    def _menu1(self):
        self.listClients()
 
    
    def _menu2(self):
        client = self.newClient()
        print("Added to the database the client:\n%s" % client)
  
    
    def _menu3(self):
        client_id = self._promptForID()
        removed_client = self.removeClient(client_id)
        print ("The client %s has been removed from the database." % removed_client.getName())

    
    def _menu4(self):
        client_id = self._promptForID()
        client = self.modifyClient(client_id)
        print("Client's details updated:\n%s" % client)   
        
    def _menu5(self):
        client_id = self._promptForID()
        symbol = self._promptForSymbol()
        position = self.queryClientPosition(client_id, symbol)
        print("The client holds a position of %d stocks on security %s" % (position.getQuantity(), position.getSymbol()))
    def _menu6(self):
        client_id = self._promptForID()
        self.listAllClientPositions(client_id)
                              
    def run(self):
            menu_items = [self._menu0, self._menu1, self._menu2, self._menu3, self._menu4, self._menu5, self._menu6]
            try:
                choice = self._menu()
                if choice in range(0,7) :
                    menu_item = menu_items[choice]
                    menu_item()
                else :
                    print ("Error: Undefined input ", file=sys.stderr)
                    
            except (ClientException, PositionException, DataUnavailableEx) as ex :
                print("Exception: ", ex, file=sys.stderr)

if __name__ == '__main__':
    pass
        
