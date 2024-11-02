import numpy as np
import matplotlib.pyplot as plt

# Step 1: User input for data or data generation
# You can accept user input or generate random data (for example using numpy)
try:
    user_input = input("Enter numbers separated by commas: ")
    data = list(map(float, user_input.split(',')))  # Convert input string to a list of floats
except ValueError:
    print("Invalid input. Please enter numbers separated by commas.")
    data = np.random.randn(1000)  # Fallback to generating random data if input is incorrect

# Step 2: Get number of bins from the user
try:
    bins = int(input("Enter the number of bins (e.g., 10): "))
except ValueError:
    print("Invalid input for bins. Using default value of 10.")
    bins = 10

# Step 3: Create the histogram
plt.figure(figsize=(8, 6))  # Set figure size
plt.hist(data, bins=bins, color='blue', alpha=0.7, edgecolor='black')

# Step 4: Customization
plt.title('Histogram of User Input Data')
plt.xlabel('Data Values')
plt.ylabel('Frequency')
plt.grid(True)
