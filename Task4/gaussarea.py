#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import scipy.integrate
from matplotlib import pyplot as plt
from math import pi


def gauss(x):
    return A*np.exp(-(x-x0)**2/(2*sig**2))+z0

A = float(input("input A: "))
x0 =  float(input("input x0: "))
sig =  float(input("input sig: "))
z0 =  float(input("input z0: "))

b = np.linspace(-10,10,200)
c = gauss(b)
x =  float(input("input lower boundary: "))
y =  float(input("input higher boundary: "))


plt.fill_between(b,c,alpha=0.3)

integinf, errorinf = scipy.integrate.quad(gauss, x, y) #does the integral
print("Integral is = ", integinf) 
plt.plot(b,c,label=f"area = {integinf}")
plt.legend()
plt.show()

# In[ ]:




