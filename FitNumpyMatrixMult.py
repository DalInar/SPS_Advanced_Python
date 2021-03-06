# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 21:18:45 2017

@author: pakij
"""

import MatrixMult as MM
import numpy
import matplotlib.pyplot as plt


trials = 100
Ls = range(30,1000,50)
Man_Times = []

for l in Ls:
    print("L=",l)
    matmult = MM.MatrixMult(l)
    man_time = matmult.numpy_mult_time(trials)
    Man_Times.append(man_time)
    
coeffs = numpy.polyfit(Ls,Man_Times,4)
p_fit = numpy.poly1d(coeffs)

print(coeffs)
plt.figure()
plt.plot(Ls, Man_Times, label="Manual")
plt.plot(Ls, p_fit(Ls), label="Fit")
plt.legend()
plt.xlabel('L')
plt.ylabel("Seconds")
plt.show()