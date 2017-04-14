# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy

def sine(x):
    return numpy.sin(x)

class Car:
    def __init__(self, mass, speed):
        self.speed = speed
        self.mass = mass
        
    def momentum(self):
        return self.speed*self.mass
    
    def kinetic_energy(self):
        p = self.momentum()
        return p**2/(2*self.mass)

print("Hello!")
print(sine(numpy.pi))

f = lambda x: x**2
print(f(4))

foo = numpy.arange(0,5,0.5)
print(foo)
print(list(filter(lambda x: x % 2==0, foo)))
print(list(map(lambda x: x+1, foo)))
new_foo = [x**3 for x in foo]
print(new_foo)

my_car = Car(1000, 50)
print(my_car.momentum())
print(my_car.kinetic_energy())