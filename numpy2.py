import numpy as np


array_3x3 = np.random.randint(1, 11, size=(3, 3))
print("3x3 Array:")
print(array_3x3)


sum_of_elements = np.sum(array_3x3)
print("\nSum of all elements:", sum_of_elements)


mean_value = np.mean(array_3x3)
print("\nMean value of elements:", mean_value)


min_value = np.min(array_3x3)
max_value = np.max(array_3x3)
print("\nMinimum value:", min_value)
print("Maximum value:", max_value)


array_1x9 = np.reshape(array_3x3, (1, 9))
print("\nReshaped Array (1x9):")
print(array_1x9)


sorted_array_1x9 = np.sort(array_1x9)
print("\nSorted Array (1x9):")
print(sorted_array_1x9)

# Find the index of the maximum value in the sorted array
index_of_max = np.argmax(sorted_array_1x9)
print("\nIndex of the maximum value in the sorted array:", index_of_max)
