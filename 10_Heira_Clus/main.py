"""
Customer segmentation using Agglomerative (Hierarchical) Clustering.
Dataset: Mall_Customers.csv  |  Features: Annual Income, Spending Score
"""

import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

# --- Config (keep magic values in one place) ---
DATA_PATH = "Mall_Customers.csv"   # use a relative path; avoid hard-coded absolute paths
FEATURE_COLS = ["Annual Income (k$)", "Spending Score (1-100)"]
N_CLUSTERS = 5
CLUSTER_COLORS = ["red", "blue", "green", "cyan", "magenta"]


def load_features(path, columns):
    """Read the CSV and return (full_dataframe, feature_matrix)."""
    df = pd.read_csv(path)
    X = df[columns].to_numpy()        # select by NAME (robust) + modern .to_numpy()
    return df, X


def plot_dendrogram(X):
    """Show the dendrogram so the cluster count can be justified visually."""
    plt.figure(figsize=(10, 6))
    sch.dendrogram(sch.linkage(X, method="ward"))
    plt.title("Dendrogram")
    plt.xlabel("Customers")
    plt.ylabel("Euclidean distance")
    plt.show()


def run_clustering(X, n_clusters):
    """Fit Agglomerative clustering and return a label per row."""
    model = AgglomerativeClustering(
        n_clusters=n_clusters,
        metric="euclidean",           # 'ward' REQUIRES euclidean
        linkage="ward",
    )
    return model.fit_predict(X)       # no separate predict() exists for new points


def plot_clusters(X, labels, colors):
    """Scatter each cluster in its own color (DRY loop, not 5 copy-pasted lines)."""
    plt.figure(figsize=(8, 6))
    for cluster_id, color in enumerate(colors):
        mask = labels == cluster_id   # boolean mask: True where row is in this cluster
        plt.scatter(X[mask, 0], X[mask, 1], s=100, c=color,
                    label=f"Cluster {cluster_id + 1}")   # +1 = human-friendly name
    plt.title("Clusters of customers")
    plt.xlabel("Annual Income (k$)")
    plt.ylabel("Spending Score (1-100)")
    plt.legend()
    plt.show()


def main():
    df, X = load_features(DATA_PATH, FEATURE_COLS)
    plot_dendrogram(X)                       # decide N_CLUSTERS from this
    labels = run_clustering(X, N_CLUSTERS)
    plot_clusters(X, labels, CLUSTER_COLORS)

    df["cluster"] = labels                   # attach segment back to each customer
    df.to_csv("Mall_Customers_segmented.csv", index=False)  # client-ready deliverable
    print(df["cluster"].value_counts())      # quick sanity check of segment sizes


if __name__ == "__main__":
    main()