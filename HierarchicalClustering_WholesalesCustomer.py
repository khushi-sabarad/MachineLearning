# Hierarchical Clustering, Wholesales customer data.csv
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize
import scipy.cluster.hierarchy as shc
from sklearn.cluster import AgglomerativeClustering
import seaborn as sns
from sklearn.decomposition import PCA

data = pd.read_csv(r"C:\Users\Khushi\OneDrive\Desktop\data+codes\datasets\Wholesale customers data.csv")
# Data Exploration (Before Clustering)
print(data.head()) 
print(data.describe())

# Normalize the data ( so the scale of each variable is same, if not done, model might become biased towards higher magnitude variables, like in this case:fresh or milk)
data_scaled = normalize(data)
data_scaled = pd.DataFrame(data_scaled, columns=data.columns)
print(data_scaled.head()) #similar scales

# Dendrogram
plt.figure(figsize=(5, 3))
plt.title("Dendrogram")
d = shc.dendrogram(shc.linkage(data_scaled, method='ward'))
#x=samples, y=distance between samples. threshold=6
plt.axhline(y=6, color='r', linestyle='--')  
plt.ylabel("Euclidean distances")
plt.show()
#line divides forming 2 clusters 

# Apply Hierarchical (Agglomerative) Clustering
cluster = AgglomerativeClustering(n_clusters=2, linkage='ward')
labels = cluster.fit_predict(data_scaled)
data_scaled['Cluster'] = labels  
#0=cluster 1, 1=cluster 2

# Cluster Visualization (Pair Plot)
sns.pairplot(data_scaled, hue='Cluster', diag_kind='kde') #kde plots in the diagonal
plt.suptitle("Pair Plot of Clustered Data", y=1.02) 
plt.show()

# PCA for 2D Visualization
pca = PCA(n_components=2)
pca_data = pca.fit_transform(data_scaled.drop('Cluster', axis=1))  # Fit PCA, excluding Cluster column
plt.figure(figsize=(5, 3))
plt.scatter(pca_data[:, 0], pca_data[:, 1], c=labels)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA Visualization of Clusters")
plt.show()

# Cluster Analysis
print("\nCluster Analysis:")
for i in range(2):
    print(f"\nCluster {i}:")
    cluster_data = data[labels == i]  # Use original data for analysis
    print(cluster_data.describe())  # Describe the data in each cluster

# Analyze the centroids (means) of each cluster
print("\nCluster Centroids (Means):")
print(data.groupby(labels).mean()) # Group by cluster labels and compute mean of each column
