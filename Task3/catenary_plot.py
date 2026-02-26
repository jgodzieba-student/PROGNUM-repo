#!/usr/bin/env python

import matplotlib.pyplot as plt
import math

xarray = []
yarray = []

for x in range(-5,6,1):
    y = cosh((math.exp(x)+math.exp(-x))/2)
    yarray.append(y)
    xarray.append(x)

plt.scatter(xarray, yarray, marker='o', color='r', label="label")
plt.ylabel("y-axis", fontsize = 13)
plt.xlabel("x-axis", fontsize = 13)
plt.grid()
plt.legend(fontsize = 13)
plt.show()