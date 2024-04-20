from sklearn.datasets  import load_digits
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
X,y=load_digits(return_X_y=True)
#X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
models={
    "LR":LinearRegression(),
    "RF":RandomForestRegressor(),
    "DC":DecisionTreeRegressor()
}
mse_result={}
for name, model in models.items():
    model.fit(X,y)
    y_pred=model.predict(X)
    mse_result[name]=mean_squared_error(y,y_pred)
    plt.scatter(y,y_pred,label=name)
for name,model in mse_result.items():
    print(f"{model}:{name}")

plt.xlabel("actusl")
plt.ylabel("pred")

plt.legend()
plt.show()    

