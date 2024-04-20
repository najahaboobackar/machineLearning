
import numpy as np 
import matplotlib.pyplot as plt
x=np.array([1,2,3,4,5])
y=np.array([2,3,4,5,6])
mx=np.mean(x)
my=np.mean(y)
N=np.sum((x-mx)*(y-my))
D=np.sum((x-mx)**2)
m=N/D
b=my-m*mx
reg=m*x+b
plt.scatter(x,y,color="red",label="points")
plt.plot(x,reg,color="green", label="LR")
plt.legend()
plt.xlabel("xaxis")
plt.ylabel("yaxix")
plt.show()