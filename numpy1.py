import numpy as np

identity_matrix = np.eye(5)
print("5x5 Identity Matrix:")
print(identity_matrix)

random_array = np.random.rand(5, 5)
print("\n5x5 Array with Random Floating-Point Numbers:")
print(random_array)

modified_array = np.where(random_array > 0.5, 1, 0)
print("\nModified Array (0s and 1s):")
print(modified_array)

indices_of_ones = np.argwhere(modified_array == 1)
print("\nIndices of elements equal to 1:")
print(indices_of_ones)

stacked_array = np.hstack((identity_matrix, modified_array))
print("\nHorizontally Stacked Array:")
print(stacked_array)
