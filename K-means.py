import random
import math

# Function to calculate Euclidean distance between two points
def euclidean_distance(x1, x2):
    return math.sqrt((x1 - x2) ** 2)

# Function to calculate the new cluster centers (means)
def calculate_centroids(clusters, arr):
    centroids = []
    for cluster in clusters:
        if cluster:
            centroid = sum(arr[i] for i in cluster) / len(cluster)  # Mean of the cluster
            centroids.append(centroid)
        else:
            centroids.append(random.choice(arr))  # Handle empty clusters
    return centroids

# Function to assign points to the nearest cluster center
def assign_clusters(arr, centroids):
    clusters = [[] for _ in centroids]
    for i, point in enumerate(arr):
        distances = [euclidean_distance(point, centroid) for centroid in centroids]
        closest_index = distances.index(min(distances))
        clusters[closest_index].append(i)
    return clusters

# K-means clustering algorithm
def kmeans_clustering(arr, n_clusters, max_iterations=100):
    # Randomly initialize centroids from the array
    centroids = random.sample(arr, n_clusters)

    for _ in range(max_iterations):
        # Assign each point to the nearest centroid
        clusters = assign_clusters(arr, centroids)

        # Calculate new centroids
        new_centroids = calculate_centroids(clusters, arr)

        # Check for convergence (if centroids do not change)
        if new_centroids == centroids:
            break

        centroids = new_centroids

    return clusters, centroids

# Input: Number of clusters and array from the user
n_clusters = int(input("Enter the number of clusters: "))
array_input = list(map(float, input("Enter the elements of the array separated by spaces: ").split()))

# Perform K-means clustering
clusters, centroids = kmeans_clustering(array_input, n_clusters)

# Print the cluster centers and the points in each cluster
print("\nCluster Centers:", centroids)
for i, cluster in enumerate(clusters):
    print(f"\nCluster {i + 1} points:", [array_input[j] for j in cluster])
