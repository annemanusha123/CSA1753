import numpy as np

# Input, weights, bias
X = np.array([[1,0],[0,1]])
W = np.array([[0.5],[0.5]])
b = 0.1

# Feed Forward
Z = np.dot(X, W) + b
Y = 1 / (1 + np.exp(-Z))   # Sigmoid

print("Output:\n", Y)
