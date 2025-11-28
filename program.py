import numpy as np
from sklearn.linear_model import LinearRegression


hours = np.array([[1], [2], [3], [4], [5]])
marks = np.array([40, 50, 60, 65, 80])


model = LinearRegression()
model.fit(hours, marks)

h = 6  
pred = model.predict([[h]])

print(f"Predicted marks for {h} hours = {pred[0]:.2f}")

