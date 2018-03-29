'''
Created on 21 Feb 2018

@author: adil
'''
from abc import ABC

class Application(ABC):
    '''
    Abstract class name containing the file names and some helper functions
    '''
    config_file_name , clients_file_name, transactions_file_name, companies_file_name = ('','','', '') 
    
    @staticmethod
    def setConfigFileName(config_fname) :
        Application.config_file_name = config_fname
    
    @staticmethod
    def setCompaniesFileName(companies_fname) :
        Application.companies_file_name = companies_fname
    
    
    @staticmethod
    def getCompaniesFileName() :
        return Application.companies_file_name
   
    @staticmethod
    def getConfigFileName() :
        return Application.config_file_name
    
    
    @staticmethod
    def setClientsFileName(clients_fname) :
        Application.clients_file_name = clients_fname
    
    
    @staticmethod
    def getClientsFileName() :
        return Application.clients_file_name
    
    
    @staticmethod
    def setTransactiosFileName(transactions_fname) :
        Application.transactions_file_name = transactions_fname
    
    
    @staticmethod
    def getTransactiosFileName() :
        return Application.transactions_file_name

    def __init__(self, params):
        '''
        Constructor
        '''
    
    def _promptForQuantity(self):
        return input("Please enter number of securities: ")
    
    
    def _promptForPrice(self):
        return input("Please enter price: ")
    
    
    def _promptForID(self):
        return input ("Please enter the client's id: ")
    
    
    def _promptForSymbol(self):
        return input("Please enter a securities symbol [Max 4 characters]: ")