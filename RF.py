import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import plot_tree
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data[:, 2:]
Y = iris.target

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, Y)

# Access the first decision tree estimator in the random forest
plot_tree(model.estimators_[0], feature_names=iris.feature_names[:2], filled=True, rounded=True)
plt.figure(figsize=(10, 6))
plt.show()
