Hierarchical Clustering

Clustering is an unsupervised machine learning technique used to group similar data points together. Hierarchical clustering is a specific type of clustering that builds a hierarchy of clusters, represented as a tree-like structure called a dendrogram.  This hierarchy allows for a visual representation of the relationships between clusters and helps in determining the optimal number of clusters.

There are two main types of hierarchical clustering:

* **Agglomerative (Bottom-up):**  Starts with each data point as its own cluster and iteratively merges the closest clusters until a single cluster remains.
* **Divisive (Top-down):** Starts with one cluster containing all data points and recursively splits the clusters until each data point is in its own cluster.

This repository focuses on **agglomerative hierarchical clustering**. The process typically involves:

1. **Calculating Distances:**  A distance metric (e.g., Euclidean distance) is used to measure the similarity or dissimilarity between data points.
2. **Linkage:** A linkage method (e.g., Ward's method, single linkage, complete linkage) determines how the distance between clusters is calculated.  Ward's method, for example, minimizes the variance within each cluster.
3. **Dendrogram Construction:** The hierarchical relationships between clusters are visualized in a dendrogram.
4. **Cluster Selection:**  The dendrogram is used to determine the appropriate number of clusters.  This often involves visually inspecting the dendrogram and identifying "gaps" or significant jumps in the distance between merged clusters.
5. **Cluster Assignment:** Once the number of clusters is chosen, data points are assigned to their respective clusters.

The code examples in this repository demonstrate how to perform agglomerative hierarchical clustering using Python libraries like `scikit-learn` and `scipy`.  They also show how to visualize the results using dendrograms, scatter plots (often with dimensionality reduction techniques like PCA or t-SNE), and other plotting methods.  Understanding the characteristics of each cluster is a crucial part of the analysis.

## Code Examples

* [**Iris**](https://github.com/khushi-sabarad/MachineLearning/blob/main/HierarchicalClusterAnalysis_Iris.py)
* [**Wholesale Customers**](https://github.com/khushi-sabarad/MachineLearning/blob/main/HierarchicalClustering_WholesalesCustomer.py)
