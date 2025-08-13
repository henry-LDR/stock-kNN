import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

class Clustering:
    #initializer
    def __init__(self,coverage):
        self.coverage = coverage

    #Using PCA to determine principal components of your coverage
    def pca(self):
        pass
    #using k-means clustering to determine natural clusters in your coverage
    def kmeans(self):
        pass