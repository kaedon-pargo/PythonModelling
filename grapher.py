import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

def linearData(n=100, m=2, c=5):
	x = np.arange(n)
	
	y = randomArray(n,0.8,1.2)*(x*m + c)
	y = y + randomArray(n, -5, 5)

	f = lambda x: x*m+c

	return x,y,f

def linearFunction(m=2, c=5):
	return lambda x: x*m +c

def quadraticData(n=100, a=1,b=0,c=0):
	x = np.arange(n)
	
	y = a*x**2 + b*x + c
	y = randomArray(n,0.8,1.2)*y
	y = y + randomArray(n, -5, 5)

	f = lambda x: a*x**2 + b*x + c

	return x,y,f

def quadraticFunction(a=1,b=0,c=0):
	return lambda x:a*x**2 + b*x + c

def randomArray(n=100, lower=0, upper=1):
	x = np.random.rand(n)
	x = x*(upper-lower) + lower
	return x