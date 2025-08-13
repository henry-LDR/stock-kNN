#Import modules
import pandas as pd
import yfinance as yf
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt

#Data
coverage = ['MGNI','CYTK','CI', 'GOGO','FIVN','ESTA']
universe = ['XYZ','PI','MS','MTCH','TMDX','TXRH','GMED','CRWV','CORZ','HALO','BMY','GSK','PLTR','RTX','S']
#Parameters
metrics=['beta','forwardPE','marketCap','volume','targetMeanPrice','revenueGrowth']

class Recommender:

    def __init__(self,coverage,universe,metrics):
        self.coverage = coverage
        self.universe = universe
        self.metrics = metrics

    #Helper functions
    def get_data(self,stocks,fields):
        '''
        :param stocks: a list of strings, which are tickers to get data from
        :param fields: a list of strings, which are different quantitative indicators
        :return: a pandas dataframe
        '''
        stock_array=[]
        for i in range(len(stocks)):
            stock_data = []
            stock = yf.Ticker(stocks[i])
            for k in range(len(fields)):
                stock_data.append(stock.info.get(fields[k]))
            stock_array.append(stock_data)
        array=pd.DataFrame(stock_array,columns=fields, index=stocks)
        print(array)
        return array

    def compute_kNN_score(self,stock):
        '''
        :param stock: a string, which is a ticker we want to compute the kNN score for
        :return: the kNN score (float)
        '''

test=Recommender(coverage,universe,metrics)
print(test.get_data(coverage,metrics))
#k-NN recommendation system
