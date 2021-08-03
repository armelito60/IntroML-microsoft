import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, model_selection

X, y = datasets.load_diabetes(return_X_y=True)
print(X.shape)
print(X[0])