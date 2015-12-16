# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 20:09:16 2015

@author: hareyakana
"""
import csv
import itertools

grid=400
P1=[i/grid for i in range(grid+1)]
epsilon = 0.001

x=[]
y=[]
z=[]
coords = [x,y,z]

for vals in itertools.product(P1, P1, P1):
    if abs(sum(vals)-1) >= epsilon: continue  # this epsilon value will correct for the variations due to floating point arithmetic
    for L,v in zip(coords, vals): L.append(v)
print(len(z))            

with open('ternary_coordinate%s.txt' %int(grid), 'w') as f:
    fieldnames = ['x', 'y','z']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(len(x)):
        writer.writerow({'x': x[i], 'y': y[i],'z':z[i]})