import numpy as np

# Create a 3x3 array with random integers between 1 and 10
array_3x3 = np.random.randint(1, 11, size=(3, 3))
print("3x3 Array:")
print(array_3x3)

# Find the sum of all elements
sum_of_elements = np.sum(array_3x3)
print("\nSum of all elements:", sum_of_elements)

# Calculate the mean value of the elements
mean_value = np.mean(array_3x3)
print("\nMean value of elements:", mean_value)

# Find the minimum and maximum values
min_value = np.min(array_3x3)
max_value = np.max(array_3x3)
print("\nMinimum value:", min_value)
print("Maximum value:", max_value)

# Reshape the array to 1x9
array_1x9 = np.reshape(array_3x3, (1, 9))
print("\nReshaped Array (1x9):")
print(array_1x9)

# Sort the reshaped array in ascending order
sorted_array_1x9 = np.sort(array_1x9)
print("\nSorted Array (1x9):")
print(sorted_array_1x9)

# Find the index of the maximum value in the sorted array
index_of_max = np.argmax(sorted_array_1x9)
print("\nIndex of the maximum value in the sorted array:", index_of_max)
