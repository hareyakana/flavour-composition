# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 12:59:41 2016

@author: kkl2g12
"""
#mandelbrot set
from numpy import NaN #not-a-number
import numpy as np
import matplotlib.pyplot as plt

#N = 2.0 #the boundary
#max_iter=50
#
#def mandel(c):
#    "This function iterates the map"
#    z = 0 #initial complex value
#    for n in range(max_iter):
#        z = z*z + c
#        if abs(z) > N:
#            return n 
#            #the number of iterations before
#            #exclusion from the set
#    return NaN
#
#X = np.arange(-2,1,0.01)
#Y = np.arange(-1.5,1.5,0.01)
#Z = np.zeros((len(Y),len(X)))
#
#for iy,y in enumerate(Y):
#    for ix,x in enumerate(X):
#        Z[iy,ix] = mandel(x + 1j * y)
#
#plt.imshow(Z)
#plt.savefig("mandel.pdf")

"""
better approach than above (2 for nested loop not a good idea)
but need more memory
"""
nx=500
ny=500
max_iter=50
N = 2.0

x = np.linspace(-2,1,nx)
y = np.linspace(-1.5,1.5,ny)


xx, yy = np.meshgrid(x, y)


c = xx + 1j * yy

def prepare_array(xstep,ystep):
    fz = np.zeros((xstep,ystep), dtype = np.complex)
    famps = np.zeros((xstep,ystep), dtype = np.double)
    fmask = np.ones((xstep,ystep), dtype = np.bool)
    
    return fz,famps,fmask

z, amps, mask = prepare_array(nx,ny)


for i in range(max_iter):
    # increament of complex value using a mask
    z[mask] = z[mask] * z[mask] + c[mask]
    # update mask
    mask[:] = np.abs(z) < N
    #populate amplitude array
    amps[mask] = float(i)
    
#plt.imshow(amps)
#plt.colorbar()






    