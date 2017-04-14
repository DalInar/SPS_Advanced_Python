# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 21:25:30 2017

@author: pakij
"""

import numpy
import matplotlib.pyplot as plt

def poly_me(x):
    return x**3 -0.5*x+2

x = numpy.linspace(-10,10,100)
y = poly_me(x)

coeffs = numpy.polyfit(x,y,3)
print(coeffs)

p_fit = numpy.poly1d(coeffs)

plt.figure()
plt.plot(x,y,"-o",label="Data")
plt.plot(x,p_fit(x),label="Fit")
plt.legend()
plt.show()