# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 20:42:12 2017

@author: pakij
"""

import MatrixMult as MM
import matplotlib.pyplot as plt


L = 25
trials = 100

matmult = MM.MatrixMult(L)

man_time = matmult.manual_mult_time(trials)
numpy_time = matmult.numpy_mult_time(trials)
print("Manual Time = ", man_time)
print("Numpy Time = ", numpy_time)
print("Manual/Numpy =", man_time/numpy_time)

Ls = range(2,28,5)
Man_Times = []
Numpy_Times = []
for l in Ls:
    print("L=",l)
    matmult = MM.MatrixMult(l)
    man_time = matmult.manual_mult_time(trials)
    numpy_time = matmult.numpy_mult_time(trials)
    Man_Times.append(man_time)
    Numpy_Times.append(numpy_time)
    
plt.figure()
plt.plot(Ls, Man_Times, label="Manual")
plt.plot(Ls, Numpy_Times, label="NumPy")
plt.legend()
plt.xlabel('L')
plt.ylabel("Seconds")
plt.show()
