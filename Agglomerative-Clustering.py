import numpy as np
import pandas as pd
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

# Data points and labels
points = np.array([18, 22, 25, 27, 42, 43])
full_dist = np.abs(points[:, None] - points)
cond_dist = squareform(full_dist)
labels = ['18', '22', '25', '27', '42', '43']

# Function to print distance matrix
def print_mat(mat, step, labels):
    df = pd.DataFrame(mat, columns=labels, index=labels)
    print(f"Distance Matrix at step {step} :\n", df)

# Single-linkage clustering function
def s_link_cluster(dist_mat):
    global labels
    step = 1
    n = 6
    curr_mat = dist_mat.copy()

    while n > 1:
        min_dist = np.inf
        for i in range(len(curr_mat)):
            for j in range(i + 1, len(curr_mat)):
                if curr_mat[i, j] < min_dist:
                    min_dist = curr_mat[i, j]
                    cl_a, cl_b = i, j

        print_mat(curr_mat, step, labels)
        
        new_cl = np.minimum(curr_mat[cl_a], curr_mat[cl_b])
        inds = [x for x in range(len(curr_mat)) if x != cl_a and x != cl_b]

        new_mat = np.zeros((n - 1, n - 1))
        new_mat[:-1, :-1] = curr_mat[np.ix_(inds, inds)]
        new_mat[-1, :-1] = new_mat[:-1, -1] = new_cl[inds]

        curr_mat = new_mat

        new_lbl = f"({labels[cl_a]},{labels[cl_b]})"
        labels = [labels[i] for i in inds] + [new_lbl]

        n -= 1
        step += 1

    print_mat(curr_mat, step, labels)

# Run the single-linkage clustering and plot the dendrogram
s_link_cluster(full_dist)
z = linkage(cond_dist, method='single')

dendrogram(z, labels=['18', '22', '25', '27', '42', '43'])
plt.title('Single Linkage Dendrogram')
plt.xlabel('Cluster')
plt.ylabel('Distance')
plt.show()
