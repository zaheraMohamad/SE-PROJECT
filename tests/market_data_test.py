'''
Created on 25 Nov 2017

@author: adil
'''
import sys
from test.test_deque import fail
sys.path.append("../packages")

from server.YahooServer import YahooServer
from server.alphavantage import Alphavantage
from server.price import PriceServer
from server.Price_Unavailable_Ex import PriceUnavailableEx

from trades.client import Client
from trades.position import Position
from trades.PositionException import PositionException

import datetime

import unittest
import re
from re import  RegexFlag
import ServerMock

class MarketDataTest(unittest.TestCase):
    def setUp(self):
        self.yahoo = YahooServer('../trades.conf')
        self.alpha = Alphavantage('../alpha.conf')
        mock = ServerMock.MockAlphaServer()
        self.price_server=PriceServer(mock)
        
        self.json_regex=re.compile(r"^\{.*\}$", RegexFlag.DOTALL)
        self.url_regex=re.compile(r"https://.*/.*?", RegexFlag.DOTALL)
        
        self.client = Client(1, "Adil", "a.al-yasiri@salford.ac.uk")
    def test_connect_to_Yahoo_server(self):
        url=self.yahoo.getURL()
        self.assertRegex(url, self.url_regex, 'URL of server should match a REGEX')
    
    @unittest.skip("skipping yahoo json test")
    def test_get_Yahoo_data_as_json(self):
        self.assertTrue('chart' in self.yahoo.getDataAsJSON(), 'Data from server looks like a json object')
    
    @unittest.skip("skipping yahoo text test")
    def test_get_Yahoo_data_as_text(self):
        self.assertRegex(self.yahoo.getDataAsText(), self.json_regex, 'Text from server looks like a json object')
        
    def test_connect_to_Alphavantage_server(self):
        url = self.alpha.getURL()
        self.assertRegex(url, 'https://.*/.*?', 'URL of server should match a REGEX')
        
    @unittest.skip("skipping alpha json test")
    def test_get_Alphavantage_data_as_json(self):
        self.assertTrue('Meta Data' in self.alpha.getDataAsJSON(), 'Data from server looks like a json object')
    
    @unittest.skip("skipping alpha text test")
    def test_get_Alphavantage_data_as_text(self):
        self.assertRegex(self.alpha.getDataAsText(), self.json_regex, 'Text from server looks like a json object')
        
    #@unittest.skip("skipping today's price  test")
    @unittest.expectedFailure(PriceUnavailableEx)
    def test_tody_price_by_symbol(self):
        self.assertEqual(self.price_server.getTodaySecurityPriceBySymbol("MSFT"), '83.8700', 'todays price')   
    
    #@unittest.skip("skipping last recorded price  test")
    #@unittest.expectedFailure
    def test_last_recorded_price_by_symbol(self):
        self.assertEqual(self.price_server.getLastRecordedPriceBySymbol("MSFT"), '83.8700', 'todays price')     
    
    #@unittest.skip("skipping creating a client test")
    #@unittest.expectedFailure
    def test_create_client(self):
        client = Client(1, "Adil", "a.al-yasiri@salford.ac.uk")
        self.assertEqual("Adil", client.getName(), "Clent created successfully")
    
    #@unittest.skip("skipping adding a position")
    #@unittest.expectedFailure
    def test_add_position(self):
        self.client.addPosition(Position("GOOG", 100, datetime.datetime.now()))
        self.assertEqual(100, self.client.getPosition("GOOG").getQuantity())
        self.client.addPosition(Position("GOOG", 100, datetime.datetime.now()))
        self.assertEqual(200, self.client.getPosition("GOOG").getQuantity())
        
        
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()