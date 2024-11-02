import numpy as np

# Take user input for the array elements
data = input("Enter the array elements separated by spaces: ")
data = np.array([int(x) for x in data.split()])

# Print the input array
print("\nInput Array: \n", data)

# Sort the array
sorted_data = np.sort(data)
print("\nSorted Array: \n", sorted_data)

# Take user input for the bin size
bin_size = int(input("\nEnter the bin size: "))
num_bins = len(sorted_data) // bin_size

# Create bins
bin1 = np.zeros((num_bins, bin_size))  # Bin mean
bin2 = np.zeros((num_bins, bin_size))  # Bin boundaries
bin3 = np.zeros((num_bins, bin_size))  # Bin median

# Print initial bins (subarrays)
print("\nInitial Bins (Subarrays):")
for i in range(0, len(sorted_data), bin_size):
    bin_data = sorted_data[i:i + bin_size]
    print(f"Bin {i // bin_size + 1}: {bin_data}")

# Bin mean
for i in range(0, len(sorted_data), bin_size):
    k = i // bin_size
    mean = np.mean(sorted_data[i:i + bin_size])
    bin1[k, :] = mean
print("\nBin Mean: \n", bin1)

# Bin boundaries
for i in range(0, len(sorted_data), bin_size):
    k = i // bin_size
    min_value = sorted_data[i]
    max_value = sorted_data[i + bin_size - 1]
    bin2[k, :] = [min_value] * (bin_size // 2) + [max_value] * (bin_size - bin_size // 2)
print("\nBin Boundaries: \n", bin2)

# Bin median
for i in range(0, len(sorted_data), bin_size):
    k = i // bin_size
    median = np.median(sorted_data[i:i + bin_size])
    bin3[k, :] = median
print("\nBin Median: \n", bin3)
