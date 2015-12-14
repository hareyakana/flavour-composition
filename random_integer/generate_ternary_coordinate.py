# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 20:09:16 2015

@author: hareyakana
"""
import csv

grid=100
b=[]
r=[]
l=[]

P1=[]
P2=[]
P3=[]
for i in range(grid+1):
    P1.append(i/grid)
    P2.append(i/grid)
    P3.append(i/grid)


x=[]
y=[]
z=[]

for i in range(grid+1):
    for j in range(grid+1):
        for k in range(grid+1):
            if P1[i]+P2[j]+P3[k]==1:
                x.append(P1[i])
                y.append(P2[j])
                z.append(P3[k])
            else:
                pass

with open('ternary_coordinate100.txt', 'w') as f:
    fieldnames = ['x', 'y','z']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(len(x)):
        writer.writerow({'x': x[i], 'y': y[i],'z':z[i]})