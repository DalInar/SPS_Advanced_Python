# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 19:59:57 2017

@author: pakij
"""

import numpy
import time
import matplotlib.pyplot as plt

def manual_multiply(A,B,C,L):
    for i in range(0,L):
        for j in range(0,L):
            C[i,j]=0.
            for k in range(0,L):
                C[i,j] += A[i,k]*B[k,j]
    return C

def numpy_dot_multiply(A,B,C):
    C = numpy.dot(A,B)
    return C
    
L=30
A= numpy.random.random((L,L))
B= numpy.random.random((L,L))
C= numpy.zeros((L,L))

trials = 100

start = time.time()
for i in range(0,trials):
    C=manual_multiply(A,B,C,L)
end = time.time()
manual_time = end-start

start = time.time()
for i in range(0,trials):
    C=numpy_dot_multiply(A,B,C)
end = time.time()
numpy_time = end-start

print("Manual Time =", 1.*manual_time/trials)
print("Numpy Time =", 1.*numpy_time/trials)
print("Manual/Numpy = ",1.*manual_time/numpy_time)

