import numpy as np

numbers = np.random.uniform(-3 + 1e-15, 3, (5, 5))
numbers.transpose()
determinant = np.linalg.det(numbers)

print(determinant)