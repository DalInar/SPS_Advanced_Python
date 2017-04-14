# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 20:35:59 2017

@author: pakij
"""
import numpy
import time

class MatrixMult:
    def __init__(self, L):
        self.A = numpy.random.random((L,L))
        self.B = numpy.random.random((L,L))
        self.L = L
        
    def manual_mult_time(self, trials):
        start = time.time()
        for trial in range(0,trials):
            C = numpy.zeros((self.L, self.L))
            for i in range(0,self.L):
                for j in range(0,self.L):
                     for k in range(0,self.L):
                         C[i,j] += self.A[i,k]*self.B[k,j]
        end = time.time()
        return 1.*(end-start)/trials
    
    def numpy_mult_time(self, trials):
        start = time.time()
        for trial in range(0,trials):
            C = numpy.dot(self.A, self.B)
        end = time.time()
        return 1.*(end-start)/trials