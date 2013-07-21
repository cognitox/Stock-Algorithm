'''
Created on Jul 20, 2013

@author: justin
'''
import unittest
from broker import Broker


class Test(unittest.TestCase):


    def setUp(self):
        print 'Running broker tests'
        self.Broker = Broker()
        pass


    def tearDown(self):
        pass

    
    '''
    Testing Public Accessor Methods
    
    '''
    def BuyStockByTickerAndNumberOfShares(self):
        pass
    
    #
    '''
    Strong Normal Testing 
    '''
    def BuyASingleShareOfStock(self):
        '''
        Buys a single share of stock
        '''
        tickerSymbol = 'DOW'
        numberOfShares = 1
        self.Broker.BuyStockByTickerSymbolAndNumberOfShares(tickerSymbol, numberOfShares)
        
        pass
    
    def BuyMultipleSharesOfStock(self):
        '''
        Buys multiple shares of stock 
        '''
        tickerSymbol = 'DOW'
        numberOfShares = 100
        self.Broker.BuyStockByTickerSymbolAndNumberOfShares(tickerSymbol, numberOfShares)
        
        pass
    
    def SellAllStockByTickerSymbol(self):
        '''
        sells all stock bought by a ticker symbol
        '''
        
        tickerSymbol = 'DOW'
        numberOfShares = 100
        self.Broker.BuyStockByTickerSymbolAndNumberOfShares(tickerSymbol, numberOfShares)
        
        
        tickerSymbol = 'DOW'
        self.Broker.SellAllSharesOfStockByTickerSymbol(tickerSymbol)
        
        pass
    
    def BuyStockThatHasBeenPreviouslyPurchasedAndHasBeenClosed(self):
        '''
        Buys stock, closes it, and buys the same stock again and closes it
        '''
        '''
        Recreates a stock that has been purchased and closed and purchases it again
        '''
        tickerSymbol = 'DOW'
        numberOfShares = 100
        self.Broker.BuyStockByTickerSymbolAndNumberOfShares(tickerSymbol, numberOfShares)
        
        #sells all the tickerSymbol shares
        self.Broker.SellAllSharesOfStockByTickerSymbol(tickerSymbol)
        
        tickerSymbol = 'DOW'
        numberOfShares = 100
        self.Broker.BuyStockByTickerSymbolAndNumberOfShares(tickerSymbol, numberOfShares)
            
        pass
    
    '''
    Strong Robustness Testing
    '''
    def BuyStockByNonExistantTickerSymbol(self):
        '''
        Trys to buy a stock with a non-existant ticker symbol
        '''
        tickerSymbol = 'NonExistant'
        numberOfShares = 100
        self.Broker.BuyStockByTickerSymbolAndNumberOfShares(tickerSymbol, numberOfShares)    
        pass
    
    def BuyStockByInvalidTickerSymbolFormat(self):
        '''
        Trys to buy with a ticker symbol that is not in the proper type expected
        function expects a string, try numbers, unicode characters ... and other invalid types
        '''
        tickerSymbol = 1
        numberOfShares = 100
        self.Broker.BuyStockByTickerSymbolAndNumberOfShares(tickerSymbol, numberOfShares)    
        
        tickerSymbol = '⌘ ⌛ ☘'
        numberOfShares = 100
        self.Broker.BuyStockByTickerSymbolAndNumberOfShares(tickerSymbol, numberOfShares)    
        
        tickerSymbol = '12345'
        numberOfShares = 100
        self.Broker.BuyStockByTickerSymbolAndNumberOfShares(tickerSymbol, numberOfShares)    
        
        tickerSymbol = '987'
        numberOfShares = 100
        self.Broker.BuyStockByTickerSymbolAndNumberOfShares(tickerSymbol, numberOfShares)    
        
        tickerSymbol = 1.2
        numberOfShares = 100
        self.Broker.BuyStockByTickerSymbolAndNumberOfShares(tickerSymbol, numberOfShares)    
        
        pass
    
    def BuyStockThatIsCurrentlyActiveAndOpenAndHasNotClosedAndSold(self):
        '''
        Trys to buy a stock that was already purchased, without the proper locks, and procedures that 
        have taken place, currently not supported.....
        '''
        pass
    
    
    def SellAllStockForStockThatHasntBeenPurchase(self):
        '''
        Trys to Sell All Stock For Stock that hasn't been purchased
        '''
    
        
        
        
    '''
    Testing Private Methods
    '''
        
        
        
        
        
        
        
        
        '''
    def BuyAShareOfStock(self):
        
        
        self.Broker.BuyStockByTickerSymbolAndNumberOfShares(tickerSymbol, numberOfShares)
        
        self.Broker.SellAllSharesOfStockByTickerSymbol(tickerSymbol)
        
        self.Broker.SellStockByTickerSymbolAndNumberOfShares(tickerSymbol, numberOfShares)
        
        self.Broker._BuyStockByTickerAndNumberOfSharesAndVerifyIndividualShareAsk(tickerSymbol, numberOfShares, individualShareAsk)
        
        self.Broker._SellAllSharesOfStockByTickerSymbol(tickerSymbol, numberOfShares, individualShareAsk, individualShareActualPrice, individualShareBid)
        
        self.Broker._SellStockByTickerSymbolAndAmountOfSharesAndVerifyIndividualShareBid(tickerSymbol, numberOfShares, individualShareAsk, individualShareActualPricePaid, individualShareBid)
        
        pass
        '''




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()