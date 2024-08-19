import numpy as np

# Step 1: Create a 5x5 identity matrix
identity_matrix = np.eye(5)
print("5x5 Identity Matrix:")
print(identity_matrix)

# Step 2: Create a 5x5 array with random floating-point numbers between 0 and 1
random_array = np.random.rand(5, 5)
print("\n5x5 Array with Random Floating-Point Numbers:")
print(random_array)

# Step 3: Replace all values > 0.5 with 1, and <= 0.5 with 0
modified_array = np.where(random_array > 0.5, 1, 0)
print("\nModified Array (0s and 1s):")
print(modified_array)

# Step 4: Find indices of elements equal to 1
indices_of_ones = np.argwhere(modified_array == 1)
print("\nIndices of elements equal to 1:")
print(indices_of_ones)

# Step 5: Stack the identity matrix and the modified array horizontally
stacked_array = np.hstack((identity_matrix, modified_array))
print("\nHorizontally Stacked Array:")
print(stacked_array)
