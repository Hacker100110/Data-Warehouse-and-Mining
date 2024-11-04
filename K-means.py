import random
import math

# Function to calculate Euclidean distance between two points
def euclidean_distance(x1, x2):
    return math.sqrt((x1 - x2) ** 2)

# Function to calculate the new cluster centers (means)
def calculate_centroids(cls, arr):
    cen = []
    for cl in cls:
        if cl:
            c = sum(arr[i] for i in cl) / len(cl)  # Mean of the cluster
            cen.append(c)
        else:
            cen.append(random.choice(arr))  # Handle empty clusters
    return cen

# Function to assign points to the nearest cluster center
def assign_clusters(arr, cen):
    cls = [[] for _ in cen]
    for i, point in enumerate(arr):
        distances = [euclidean_distance(point, c) for c in cen]
        closest_index = distances.index(min(distances))
        cls[closest_index].append(i)
    return cls

# K-means clustering algorithm
def kmeans_clustering(arr, n_clusters, max_iterations=100):
    # Randomly initialize centroids from the array
    cen = random.sample(arr, n_clusters)

    for _ in range(max_iterations):
        # Assign each point to the nearest centroid
        cls = assign_clusters(arr, cen)

        # Calculate new centroids
        new_cen = calculate_centroids(cls, arr)

        # Check for convergence (if centroids do not change)
        if new_cen == cen:
            break

        cen = new_cen

    return cls, cen

# Input: Number of clusters and array from the user
n_clusters = int(input("Enter the number of clusters: "))
array_input = list(map(float, input("Enter the elements of the array separated by spaces: ").split()))

# Perform K-means clustering
cls, cen = kmeans_clustering(array_input, n_clusters)

# Print the cluster centers and the points in each cluster
print("\nCluster Centers:", cen)
for i, cl in enumerate(cls):
    print(f"\nCluster {i + 1} points:", [array_input[j] for j in cl])
