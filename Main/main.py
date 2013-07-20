#uses the xml scripts and the log_database_files
from z_setup.setup import Setup
#data tools
from models.data.data import Data
from models.data.api_adapters.google_finance import GoogleFinance
from models.data.api_adapters.scrapers import Scrapers
from models.data.api_adapters.yahoo_finance import YahooFinance
#Analysis Tools
from models.analyze.analyze import Analyze
#Database Support
from models.database.database import Database
#strategy for trading uses logic
from strategy.strategy import Strategy
#all the logical decisions, made mostly boolean values
from strategy.logic.logic import Logic
#machine learning logic uses this
from strategy.logic.machine_learning import MachineLearning

# => reads the XML configuration file and returns a configuration object
Setup()
# Strategy
Strategy()
# Logic
Logic()
MachineLearning()
# => data
Data()
# => Data Tools
GoogleFinance()
Scrapers()
YahooFinance()
# => Analysis
Analyze()
# => Database
Database();


