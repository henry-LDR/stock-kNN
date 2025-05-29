#Import modules
import yfinance as yf
import bs4
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Helper functions
metrics=['beta','forwardPE','marketCap','volume','targetMeanPrice','revenueGrowth']
def data(stocks,metrics):
    stockmetrics=[]
    for i in range(len(stocks)):
        lis = []
        stock = yf.Ticker(stocks[i])
        for k in range(len(metrics)):
            lis.append(stock.info.get(metrics[k]))
        stockmetrics.append(lis)
    array=np.array(stockmetrics)
    return array

#TODO: Create a screener that generates a list of preliminary candidates-these will get k-NN

#Set up the PCA:
#Array with stocks that made good pitches
winners=['MGNI','CYTK','CI', 'GOGO','FIVN','ESTA']
#Then generate a numpy matrix with row[i] containing all of the metrics for stock[i]
#For instance, P/E, EV/EBITDA, etc.
#Important: How to deal with negative or nonexistent multiples? Cannot just have them in.
#Otherwise k-NN falls apart since we need to do PCA and a distance on them
winnerattributes=data(winners,metrics)
print(winnerattributes)

stockmatrix=np.array(winnerattributes)
print(stockmatrix)
#prepare the data
scalar = StandardScaler(copy=False)
scalar.fit(stockmatrix)
scaledsm=scalar.transform(stockmatrix)

pca=PCA(copy=False,n_components=3)
pca.fit(scaledsm)
pcasm=pca.transform(scaledsm)

print(scaledsm)
print('pca')
print(pcasm)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter3D(pcasm[:,0], pcasm[:,1], pcasm[:,2])


#TODO: Use k-Nearest Neighbors to compare the candidates against winners
#TODO: What are some good metrics to compare? We need them to do the PCA.
##TODO: We need to see which metrics are clustered for winning stock pitches? Use PCA to do so and weigh them.
#TODO: After we get the PCA matrix and loading, we can apply it to new stocks and get k-NN scores

#Initialize an array of candidates
candidates=['XYZ','PI','MS','MTCH','TMDX','TXRH']
#Collect the same data
candidatematrix=data(candidates,metrics)
#Now standardize:
scalar.fit(candidatematrix)
scalar.transform(candidatematrix)
proj=pca.transform(candidatematrix)

ax.scatter3D(proj[:,0], proj[:,1], proj[:,2],'r')
plt.show()

print('works')