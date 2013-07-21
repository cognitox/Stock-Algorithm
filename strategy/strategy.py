from broker.broker import Broker
from strategy.logic.logic import Logic

'''
Created on Jul 20, 2013

@author: justin
'''

class Strategy(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._Broker = Broker()
        
        self._Logic = Logic()
         
        print 'Inside Strategy'
        
    def AnalyzeTickerSymbol(self, tickerSymbol):
        '''
        Runs All the analysis on the Ticker Symbol, of the implemented Strategy,
        This should document, the number of shares to buy, at the specific market price,
        and come up with a selling price in witch the algorithm will sell, and vice-versa,
        if the stock price drops off, then it also needs to come up with bounds to sell and 
        re-coup some of the losings
        '''
        
        numberOfShares = 100
        
        buyStock = False
        
        if buyStock:
            self.BuyStockAfterAnalysis(tickerSymbol, numberOfShares)
        
        
        return False
    
    def BuyStockAfterAnalysis(self, tickerSymbol, numberOfShares):
        '''
        This method calls the 
        '''
        self._Logic.VerifyThatTickerSymbolHasBeenAnalyzed(tickerSymbol, numberOfShares)
        self._Broker.BuyStockByTickerSymbolAndNumberOfShares(self, tickerSymbol, numberOfShares)
    
        
        
        
        
        
        
        
        
        
        
        