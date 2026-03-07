#!/usr/bin/env python
# coding: utf-8

# In[1]:


from numpy import sin, cos, exp, pi
import numpy as np
import scipy.integrate

def f(x,fun):
    return eval(fun)

try:
    fun = input("function: ")
    a = float(input("lower boundary: "))
    b = float(input("lower boundary: "))

    integ, error = scipy.integrate.quad(lambda x: f(x,fun), a, b) #does the integral
    print(integ)

    n=1000
    x = np.random.uniform(a, b, n) 
    y = fun(x)

    y = np.array(y)

    i = ((b-a)/len(y))*sum(y)

    print(i)

except NameError:
    print("error: unknown function or variable")
    print("avalable functions: sin, cos, exp, pi")
except SyntaxError:
    print("erroe: syntax error, invalid input")
except ValueError:
    print("error: integration bounderies must be numbers")
except Exception:
    print("unexpected error")


# In[ ]:




