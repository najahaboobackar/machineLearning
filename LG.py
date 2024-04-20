from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
X,y=load_iris(return_X_y=True)
X=X[:,0:1]
y=(y==0).astype(int)
model=LogisticRegression().fit(X,y)
X_train, X_test,y_train,y_test=train_test_split(X,y,train_size=0.2,random_state=42)
plt.scatter(X_test,y_test,c="g",label="Test")
plt.scatter(X_train,y_train,c="g",label="Train")

X_value=np.linspace(X.min(),X.max(),100)
y_value = model.predict_proba(X_value.reshape(-1, 1))[:, 1]
#plt.scatter(X_value,y_value,c="g",label="pints")
plt.plot(X_value,y_value ,c="r",label="logistic")
plt.axhline(y=0.5,c="k",linestyle="--",label="Threashold")
plt.legend()
plt.show()