import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def linearData(n=100, m=2, c=5):
	x = np.arange(n)
	
	y = randomArray(n,0.9,1.1)*(x*m + c)
	y = y + randomArray(n, -10, 10)

	f = lambda x: x*m+c

	return x,y,f

def linearFunction(x, m=2, c=5):
	return x*m +c

def quadraticData(n=100, a=1,b=0,c=0):
	x = np.arange(n)
	
	y = a*x**2 + b*x + c
	y = randomArray(n,0.8,1.2)*y
	
	y = y + randomArray(n, -10, 10)

	f = lambda x: a*x**2 + b*x + c

	return x,y,f

def quadraticFunction(x, a=1,b=0,c=0):
	return a*x**2 + b*x + c

def sinData(n=100, a=1, b=1, c=0):
	x = np.linspace(-4, 10, n)

	y = a*np.sin(b*x + c)

	y = randomArray(n,0.8,1.2)*y
	y = y + randomArray(n, -10, 10)

	f = lambda x: a*np.sin(b*x + c)

	return x,y,f

def sinFunction(x, a=1, b=1, c=0):
	return a*np.sin(a*x + c)

def generateNoiseyData(x, f):
	y = f(x)
	y = randomArray(n,0.8,1.2)*y
	y = y + randomArray(n, -10, 10)

	return x,y,f

def randomArray(n=100, lower=0, upper=1):
	x = np.random.rand(n)
	x = x*(upper-lower) + lower
	return x