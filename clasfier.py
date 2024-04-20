from sklearn.tree import DecisionTreeClassifier ,plot_tree
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
iris=load_iris()
X=iris.data[:,2:]
Y=iris.target
model=DecisionTreeClassifier(criterion='entropy',max_depth=2)
model.fit(X,Y)
plot_tree(model,feature_names=iris.feature_names[2:],class_names=iris.target_names,filled=True,rounded=True)
plt.figure(figsize=(10,6))
plt.show()