"""K-Means clustering on Mall Customers — segment customers by income & spending."""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 1. Load data
dataset = pd.read_csv("Mall_Customers.csv")

# 2. Select features: Annual Income (col 3) + Spending Score (col 4)
#    .to_numpy() -> plain array, needed for the [rows, cols] indexing later
X = dataset.iloc[:, [3, 4]].to_numpy()

# 3. Elbow method: try k = 1..10, record WCSS (inertia_) each time
wcss = []
for k in range(1, 11):
    kmeans = KMeans(
        n_clusters=k,
        init="k-means++",   # smart, spread-out centroid seeding
        n_init=10,          # run 10 times, keep best (explicit = version-safe)
        random_state=42,    # reproducible
    )
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

# 4. Plot the elbow to choose k
plt.plot(range(1, 11), wcss, marker="o")
plt.title("The Elbow Method")
plt.xlabel("Number of clusters (k)")
plt.ylabel("WCSS")
plt.show()

# 5. Final model with the chosen k (elbow -> 5)
N_CLUSTERS = 5
kmeans = KMeans(n_clusters=N_CLUSTERS, init="k-means++", n_init=10, random_state=42)
y_kmeans = kmeans.fit_predict(X)   # learn clusters AND label each row in one step

# 6. Visualize clusters (loop beats 5 copy-pasted scatter lines)
colors = ["red", "blue", "green", "cyan", "magenta"]
for cluster in range(N_CLUSTERS):
    plt.scatter(
        X[y_kmeans == cluster, 0],            # incomes of this cluster
        X[y_kmeans == cluster, 1],            # spending of this cluster
        s=100, c=colors[cluster], label=f"Cluster {cluster + 1}",
    )
plt.scatter(
    kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
    s=300, c="yellow", label="Centroids",
)
plt.title("Clusters of customers")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.legend()
plt.show()

# 7. Save cluster labels back onto the original data
dataset["cluster"] = y_kmeans