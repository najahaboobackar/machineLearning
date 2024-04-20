from sklearn.datasets import load_wine
from sklearn.tree import plot_tree, DecisionTreeRegressor
import matplotlib.pyplot  as plt
iris=load_wine()
x=iris.data[:,5:6]
y=iris.target
model=DecisionTreeRegressor(max_depth=2)
model.fit(x,y)
plt.figure(figsize=(10,6))
plot_tree(model,feature_names=iris.feature_names[5:6],class_names=iris.target_names, filled=True, rounded=True)

plt.show()
