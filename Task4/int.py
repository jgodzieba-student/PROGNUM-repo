#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

fun = input("Enter a function f(x)=")
a = int(input("Enter 1st boundary"))
b = int(input("Enter 2nd boundary"))

n=1000
x = np.random.uniform(a, b, n) 
y = eval(fun)

y = np.array(y)

i = ((b-a)/len(y))*sum(y)

print(i)

