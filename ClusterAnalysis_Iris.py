# Cluster Analysis, Iris dataset
from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

data = load_iris()
df = data.data

z = linkage(df, method="ward")
dendro = dendrogram(z)
plt.title('Dendrogram')
plt.ylabel('Euclidean distance')
plt.show()

ac = AgglomerativeClustering(n_clusters=3, linkage="ward") 

labels = ac.fit_predict(df)
plt.figure(figsize=(8, 5))
plt.scatter(df[labels == 0, 0], df[labels == 0, 1], c="red")
plt.scatter(df[labels == 1, 0], df[labels == 1, 1], c="blue")
plt.scatter(df[labels == 2, 0], df[labels == 2, 1], c="green")
plt.show()
