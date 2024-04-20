import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 
X=np.array([[1],[3],[5],[6]])
Y=np.array([1,2,3,4])
model=LinearRegression()
model.fit(X,Y)
c=model.coef_[0]
b=model.intercept_
pre=model.predict(X)
plt.scatter(X,Y,color="red",label="points")
plt.plot(X,pre,color="green",label="LR")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()