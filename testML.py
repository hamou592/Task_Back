import numpy as np

# Sample data matrix
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

x = data[:, 2][:, np.newaxis]
print(x)