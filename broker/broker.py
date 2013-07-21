'''
Created on Jul 20, 2013

@author: justin
'''

class Broker(object):
    '''
    The broker class, handles all of the buying and selling of a stock, and delegates out all of the functionality 
    that does the error checking in the ask amount and the bid amount of a stock. also records all transactions to the database. 
    '''

    def __init__(self):
        '''
        Constructor
        There should probably be a connection string to connect to the stock broker api, somewhere here.
        '''
        print 'Inside Broker'
    
    #public
    
    def BuyStockByTickerSymbolAndNumberOfShares(self, tickerSymbol, numberOfShares):
        '''
        wrapper method, for private [_BuyStockByTickerAndNumberOfSharesAndVerifyDollarAmount(self, tickerSymbol, numberOfShares, dollarAmount)]
        '''
        '''
        need to derive the share ask, and verify that it matches with the strategy share ask when analysis was taking place.
        '''
        individualShareAsk = 100
        
        return self._BuyStockByTickerAndNumberOfSharesAndVerifyIndividualShareAsk(tickerSymbol, numberOfShares, individualShareAsk)
    
    def SellStockByTickerSymbolAndNumberOfShares(self,tickerSymbol, numberOfShares):
        '''
        This is a wrapper function that calculates out the individual share ask, the individualShareActual price,
        '''
        '''
        '''
        individualShareAsk = 100
        individualShareActualPricePaid = 100
        individualShareBid = 100
        return self._SellStockByTickerSymbolAndAmountOfSharesAndVerify(tickerSymbol, numberOfShares, individualShareAsk, individualShareActualPricePaid, individualShareBid)
        
        
    def SellAllSharesOfStockByTickerSymbol(self, tickerSymbol):
        '''
        This is a wrapper function the Sells all shares that we own by the ticker symbol
        '''
        '''
        This function needs to calculate the number of shares in the database, the individual share ask, the individual share actual price,
        the individual share bid. and then return the function that it wraps.
        '''
        numberOfShares = 100
        individualShareAsk = 100
        individualShareActualPrice = 100
        individualShareBid = 100
        return self._SellAllSharesOfStockByTickerSymbol(tickerSymbol, numberOfShares, individualShareAsk, individualShareActualPrice, individualShareBid)
            
    #private functionality
        
    def _BuyStockByTickerAndNumberOfSharesAndVerifyIndividualShareAsk(self, tickerSymbol, numberOfShares, individualShareAsk):
        '''
        Buys the numberOfShares of a ticker symbol, and verify's that the dollarAmount this program thinks
        it is buying for is the actual amount
        '''
        
        '''
        needs to make sure that the ticker symbol is correct.
        This method needs to verify that the dollar amount is the correct amount that we are buying for within 
        a standard margin value. 
        also needs to track internally the shares bought and shares sold, along with the current metrics of 
        shares bought and sold.
        '''
        
        print 'implement a function that buys stock and checks a global debug variable'
        return False
    
    def _SellStockByTickerSymbolAndAmountOfSharesAndVerifyIndividualShareBid(self, tickerSymbol, numberOfShares, individualShareAsk, individualShareActualPricePaid, individualShareBid):
        '''
        Sells the numberOfShares of a ticker symbol
        '''
        '''
        Needs to check if the number of shares are equal to or less than the number of shares bought, else throw an error
        Needs to look up the ticker symbol, and check it to make sure that the ticker symbol is correct.
        double check the amountClosed, and pass both the amountPaid, and the estimatedClosingAmount.
        
        '''
        print 'implement a function that sells stock and checks a global debug variable'
        return False
    
    def _SellAllSharesOfStockByTickerSymbol(self, tickerSymbol, numberOfShares,  individualShareAsk, individualShareActualPrice, individualShareBid):
        '''
        This method sells the total number of owned shares in the database.
        '''
        '''
        
        '''
        print 'implement a function that sells all shares of a stock'
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        