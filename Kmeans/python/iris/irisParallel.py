import os
import numpy as np
import pandas as pd
from mpi4py import MPI
import matplotlib.pyplot as plt

def load_data(file_path):
    iris = pd.read_csv(file_path)
    X = iris.iloc[:, :-1].values 
    return X

def assign_clusters(data, centroids):
    # Distancia euclidiana
    distances = np.sqrt(((data - centroids[:, np.newaxis]) ** 2).sum(axis=2))
    return np.argmin(distances, axis=0)

def show_kmeans(data, labels, n_clusters, centroids):
    plt.figure(figsize=(8, 6))
    plt.gcf().canvas.manager.set_window_title("KMeans Clustering on Iris Dataset with MPI")
    
    for i in range(n_clusters):
        cluster_points = data[labels == i]
        plt.scatter(cluster_points[:, 0], cluster_points[:, 1], label=f'Cluster {i}')
    
    if centroids is not None:
        print(centroids)
        plt.scatter(centroids[:, 0], centroids[:, 1], c='black', marker='x', s=200, label='Centroides')

    plt.xlabel('Sepal Length')
    plt.ylabel('Sepal Width')
    plt.title('Clusters de KMeans')
    plt.legend()
    plt.show()

def main(file_path, n_clusters=3):
    data = load_data(file_path)
    iterations=2147483647 # Max int
    tolerance=1e-4 # Precisión en los centroides
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    
    if rank == 0:
        index = np.random.choice(data.shape[0], n_clusters, replace=False)
        centroids = data[index]
    else:
        centroids = np.empty((n_clusters, data.shape[1]), dtype=data.dtype)
    
    # Broadcast de los centroides
    comm.Bcast(centroids, root=0)

    for i in range(iterations):
        # Distribuir datos a cada proceso y asignar a los clusters
        data_split = np.array_split(data, size)[rank]
        local_labels = assign_clusters(data_split, centroids)
        
        # Recoger en 0
        labels = comm.gather(local_labels, root=0)

        # Calcular nuevos centroides y compararlos con los anteriores
        if rank == 0:
            labels = np.concatenate(labels)
            updated_centroids = np.array([data[labels == j].mean(axis=0) for j in range(n_clusters)])

            if np.all(np.abs(updated_centroids - centroids) < tolerance):
                break
            centroids = updated_centroids
        
        # Broadcast de los nuevos centroides
        comm.Bcast(centroids, root=0)
    
    if rank == 0:
        show_kmeans(data, labels, n_clusters, centroids)

if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_directory, "Iris.csv")
    main(file_path)