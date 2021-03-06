# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 19:50:40 2018

@author: Nicho
"""

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from sklearn.cross_validation import train_test_split
from sklearn.cluster import KMeans

df= pd.read_csv("Breast-Cancer-Wisconsin.csv", na_values= ["?"])
df= df.apply(pd.to_numeric, errors='coerce')

#Fill in missing values with Mean
df= df.fillna(df.mean())


data_clean = df.fillna(df.mean())

## Simply cleaning the data not utilizing labels since they aren't needed per the phase 2 form
cluster = data_clean[['A2','A3','A4','A5','A6','A7',
'A8','A9','A10']]

#Print the clusters and describe the output
print(cluster.describe())


# Utilized to identify the k-means cluster analysis. Specifically looking at the range of 1-10 clusters
from scipy.spatial.distance import cdist
clusters=range(1,11)
meandist=[]

for k in clusters:
    model=KMeans(n_clusters=k)
    model.fit(clus_train)
    clusassign=model.predict(clus_train)
    meandist.append(sum(np.min(cdist(clus_train, model.cluster_centers_, 'euclidean'), axis=1)) / clus_train.shape[0])


##Plotting the average distance from observations from the cluster centroid. Here we are utilizing the Elbow method
##to identify number of clusters to choose. We were told to use 4 in the assignment. The model shows 4 is ideal as well

plt.figure()
plt.plot(clusters, meandist)
plt.xlabel('Number of clusters')
plt.ylabel('Average distance')
plt.title('Identifying k with the Elbow Method')
plt.show()

# Interpret 4 clusters for the Solution output
model3= KMeans(n_clusters=4)
model3.fit(clus_train)
clusassign= model3.predict(clus_train)


# plot the 4 clusters
from sklearn.decomposition import PCA
pca_2 = PCA(4)
plot_columns = pca_2.fit_transform(clus_train)
plt.scatter(x=plot_columns[:,0], y=plot_columns[:,1], c=model3.labels_,)
plt.xlabel('Variable 1')
plt.ylabel('Variable 2')
plt.title('Scatterplot of Cancer Variables using 4 Clusters')
plt.show()

