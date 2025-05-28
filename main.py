import yfinance as yf
import bs4
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import numpy as np

#TODO: Create a screener that generates a list of preliminary candidates-these will get k-NN


#Set up the PCA:
#Array with stocks that made good pitches
winners=['MGNI','CYTK','CI', 'TMDX']
#Then generate a numpy matrix with row[i] containing all of the metrics for stock[i]
#For instance, P/E, EV/EBITDA, etc.
winnerattributes=[]
for i in range(len(winners)):
    lis=[]
    stock=yf.Ticker(winners[i])
    lis.append(stock.recommendations)
    winnerattributes.append(lis)

print(winnerattributes)

stockmatrix=np.array(winnerattributes)
print(stockmatrix)
#PCA pipeline: prepare the data
PCApipe=Pipeline([

])

print('works')
#TODO: Use k-Nearest Neighbors to compare the candidates against winners
#TODO: What are some good metrics to compare? We need them to do the PCA.
##TODO: We need to see which metrics are clustered for winning stock pitches? Use PCA to do so and weigh them.
#TODO: After we get the PCA matrix and loading, we can apply it to new stocks and get k-NN scores
