'''
Created on 20 Feb 2018

@author: adil
'''

import sys
import re

from ui.abstractapp import Application
from ui.clientmanager import ClientManager
from ui.tradingappl import TradingApplication
from trades.client import ClientException
from trades.PositionException import PositionException
from server.dataunavailable import DataUnavailableEx
from ui.Security import Security

class ProgArgumentsErr(Exception):
    """
        An error of number of arguments passed to program 
    """
    def __init__(self, prog_name):
        super().__init__("Usage: %s <config_file_name> <clients_file_name> <transactions_file_name>" % prog_name)
    
 
class MainMenu(Application) :
    """ 
    A class that displays the main menu to enter either 
        Client's Manager or Trades Application
    """    
    
    def __init__(self, args):
        """
        Constructor checks that the program is run with the correct number of arguments
        """
        if len(args) < 5:
            raise ProgArgumentsErr(args[0])
        else:
            (config_file_name, clients_file_name, transactions_file_name, compnies_file_name)  = args[1:5]
           
            Application.setConfigFileName(config_file_name)
            Application.setClientsFileName(clients_file_name)
            Application.setTransactiosFileName(transactions_file_name)
            Application.setCompaniesFileName(compnies_file_name)
            
            self.clientMgr = ClientManager.getInstance()
            self.tradesAppl = TradingApplication.getInstance()
            self.security = Security.getInstance()
    
    def menu(self):
        print("""System's Main Menu
            Please choose an option: 
            1:    Manage Clients.
            2:    Trading Application

            9:    Quit without saving.
            0:    Save and Exit.
            """)
        try :
            return int(input("Enter your choice: "))
        except ValueError :
            return ""        
        
    def run(self):
        while(True) :
            try:
                choice = self.menu()
                if choice == 1:
                    self.clientMgr.run()
                elif choice == 2:
                    self.tradesAppl.run()
                    
                elif choice == 0:
                    self.clientMgr.saveClients()
                    self.tradesAppl.saveTransactions()
                    break
                
                elif choice == 9:
                    response = input("Are you sure, you want to quit the system; all changes will be discarded [y/n]? ")
                    if re.search(r"^[Yy]", response):
                        break
                    
                else :
                    print ("Error: Undefined input ", file=sys.stderr)
                    
            except (ClientException, PositionException, DataUnavailableEx) as ex :
                print("Exception: ", ex, file=sys.stderr)
            
            finally:
                input ("Please press RETURN:")
                print("\n\n")

######### main program starts here ###########

#Create and run the application main menu      
    #    argv[1] is the price server config file
    #    argv[2] is the clients' data file; one line per client. Each line contains the client's information and
    #        all positons held by that client.
    #    argv[3] is the transactions data file. Each line contains one buy or sell transaction
    #    argv[4] is the companies file containing information about the companies 
    
if __name__ == '__main__' :
    try:
        main_appl = MainMenu(sys.argv)
        main_appl.run()
    except ProgArgumentsErr as ex :
        print("Exception: ", ex.__doc__, file=sys.stderr)
        print(ex, file=sys.stderr)

