import os
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

def load_data(file_path):
    iris = pd.read_csv(file_path)
    X = iris.iloc[:, :-1].values 
    return X

def train_and_predict_kmeans(X, n_clusters=3, random_state=0):
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    y_pred = kmeans.fit_predict(X)
    return kmeans, y_pred


def plot_clusters(X, y_pred, centroids):
    plt.figure(figsize=(8, 6))
    plt.gcf().canvas.manager.set_window_title("KMeans Clustering on Iris Dataset") 
    plt.scatter(X[:, 0], X[:, 1], c=y_pred, s=50, cmap='viridis', label="Data points")
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200, alpha=0.7, marker='X', label="Centroids")
    plt.xlabel('Sepal Length')
    plt.ylabel('Sepal Width')
    plt.title('KMeans Clusters')
    plt.legend()
    plt.show()
    
def main(file_path):
    # Load and process data
    X_scaled = load_data(file_path)
    
    # Train KMeans model and predict clusters
    kmeans, y_pred = train_and_predict_kmeans(X_scaled)
        
    # Plot clusters and centroids
    plot_clusters(X_scaled, y_pred, kmeans.cluster_centers_)

if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_directory, "Iris.csv")
    main(file_path)