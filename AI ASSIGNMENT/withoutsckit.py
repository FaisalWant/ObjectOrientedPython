import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def computeCost(X, y, theta):
	inner = np.power(((np.asmatrix(X)* np.asmatrix(theta.T)) - y), 2)             
	return np.sum(inner) / (2 * len(X))

def gradientDescent(X, y, theta, alpha, iters):
	for i in range(iters):
		theta = theta - (alpha/len(X)) * np.sum((np.asmatrix(X)* np.asmatrix(theta.T) - y) * X, axis=0)
		cost = computeCost(X, y, theta)
		# if i % 10 == 0: # just look at cost every ten loops for debugging
		#     print(cost)
	return (theta, cost)


dfx = pd.read_csv('linearX.csv', names=['x'])
df_normx = (dfx - dfx.mean()) / (dfx.max() - dfx.min())

dfy= pd.read_csv('linearY.csv',names=['y'])
df_normy = (dfy - dfy.mean()) / (dfy.max() - dfy.min())

#converting pandas to numpy
my_datax=df_normx.values 
my_datay=df_normy.values



X = my_datax[:, 0].reshape(-1,1)			# -1 tells numpy to figure out the dimension by itself
ones = np.ones([X.shape[0], 1]) 							  # create a array containing only ones 
X = np.concatenate([ones, X],1) 							  # cocatenate the ones to X matrix
print(X.shape())
y = my_datay[:, 0].reshape(-1,1)					  # create the y matrix

print(np.asmatrix(X))

# plt.scatter(X[:,1].reshape(-1,1), y)
# plt.show()



alpha = 0.0001
iters = 1000

# theta is a row vector
theta = np.array([[1.0, 1.0]])

g, cost = gradientDescent(X, y, theta, alpha, iters)  
print(g, cost)