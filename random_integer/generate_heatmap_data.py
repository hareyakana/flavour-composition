# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 11:09:22 2015

@author: hareyakana
"""

import pylab as p
import ternary as t
import csv
"""THIS IS MEMORY INTENSIVE PROGRAM"""
"""THIS IS MEMORY INTENSIVE PROGRAM"""
"""THIS IS MEMORY INTENSIVE PROGRAM"""
"""THIS IS MEMORY INTENSIVE PROGRAM"""
###
###
"""ternary coordinates""" #this is usually larger
B=[] #bottom axis
R=[] #right axis
L=[] #left axis
with open('ternary_coordinate100.txt','r')as f:
    reader = csv.DictReader(f)
    for row in reader:
        B.append(float(row['x']))
        R.append(float(row['y']))
        L.append(float(row['z']))

grid=100

"""data obtained from the generated flavour compositions"""
E110=[]
M110=[]
T110=[]
    
with open('110.txt','r')as f:
    reader = csv.DictReader(f)
    for row in reader:
        E110.append(float("%.3f" % float(row['x'])))
        M110.append(float("%.3f" % float(row['y'])))
        T110.append(float("%.3f" % float(row['z'])))

E120=[]
M120=[]
T120=[]
    
with open('120.txt','r')as f:
    reader = csv.DictReader(f)
    for row in reader:
        E120.append(float("%.3f" % float(row['x'])))
        M120.append(float("%.3f" % float(row['y'])))
        T120.append(float("%.3f" % float(row['z'])))
        
E100=[]
M100=[]
T100=[]
    
with open('100.txt','r')as f:
    reader = csv.DictReader(f)
    for row in reader:
        E100.append(float("%.3f" % float(row['x'])))
        M100.append(float("%.3f" % float(row['y'])))
        T100.append(float("%.3f" % float(row['z'])))

E010=[]
M010=[]
T010=[]
    
with open('010.txt','r')as f:
    reader = csv.DictReader(f)
    for row in reader:
        E010.append(float("%.3f" % float(row['x'])))
        M010.append(float("%.3f" % float(row['y'])))
        T010.append(float("%.3f" % float(row['z'])))


value110=[]
value120=[]
value100=[]
value010=[]        
"""binning process of obtained data"""
Coor=len(B)
N=len(E110)

for i in range(Coor):
    value110.append(0)
    value120.append(0)
    value100.append(0)
    value010.append(0)

for i in range(Coor):
    for k in range(N):
        if B[i]==E110[k] and R[i]==M110[k] and L[i]==T110[k]:
            value110[i]=(value110[i]+1.0)
        if B[i]==E120[k] and R[i]==M120[k] and L[i]==T120[k]:
            value120[i]=(value120[i]+1.0)
        if B[i]==E100[k] and R[i]==M100[k] and L[i]==T100[k]:
            value100[i]=(value100[i]+1.0)
        if B[i]==E010[k] and R[i]==M010[k] and L[i]==T010[k]:
            value010[i]=(value010[i]+1.0)

v110=[]
v120=[]
v100=[]
v010=[]

for i in range(Coor):
    v110.append(float(value110[i]/N))
    v120.append(float(value120[i]/N))
    v100.append(float(value100[i]/N))
    v010.append(float(value010[i]/N))
    
"""ternary heatmap"""
with open('heatmap110.txt', 'w') as f:
    fieldnames = ['x', 'y','z','w']
    writer = csv.DictWriter(f,delimiter=' ', fieldnames=fieldnames)
    for i in range(len(B)):
        writer.writerow({'x': B[i], 'y': R[i],'z':L[i],'w':v110[i]})
with open('heatmap120.txt', 'w') as f:
    fieldnames = ['x', 'y','z','w']
    writer = csv.DictWriter(f,delimiter=' ', fieldnames=fieldnames)
    for i in range(len(B)):
        writer.writerow({'x': B[i], 'y': R[i],'z':L[i],'w':v120[i]})
with open('heatmap100.txt', 'w') as f:
    fieldnames = ['x', 'y','z','w']
    writer = csv.DictWriter(f,delimiter=' ', fieldnames=fieldnames)
    for i in range(len(B)):
        writer.writerow({'x': B[i], 'y': R[i],'z':L[i],'w':v100[i]})
with open('heatmap010.txt', 'w') as f:
    fieldnames = ['x', 'y','z','w']
    writer = csv.DictWriter(f,delimiter=' ', fieldnames=fieldnames)
    for i in range(len(B)):
        writer.writerow({'x': B[i], 'y': R[i],'z':L[i],'w':v010[i]})

#figure, d=t.figure(scale=1)
#d.boundary(linewidth=2)
#d.gridlines(multiple=0.1,color="blue",linewidth=0.8)
#d.set_title(r"source flavour composition $(\nu_e,\nu_\mu,\nu_\tau)=(\frac{1}{2},\frac{1}{2},0)$",fontsize=20)
#d.left_axis_label(r"$\nu_\tau$",fontsize=20,offset=0.12)
#d.right_axis_label(r"$\nu_\mu$",fontsize=20,offset=0.1)
#d.bottom_axis_label(r"$\nu_e$",fontsize=20,offset=0)
#d._redraw_labels()
#d.ticks(axis='brl',multiple=0.1)
#p.axis('off')
#d.heatmap(v110,style="triangular",vmin=0,vmax=1)
##d.heatmap(v120,style="triangular",vmin=0,vmax=1)
##d.heatmap(v100,style="triangular",vmin=0,vmax=1)
##d.heatmap(v010,style="triangular",vmin=0,vmax=1)                
#d.resize_drawing_canvas(scale=1.15)
#
#point1=[(0.3980599331366308,0.3112164005027349,0.2907236663606344)]
##point2=[(0.34669820676138435,0.3336302826666826,0.31967151057193305)]
##point3=[(0.55214511226237,0.24397475401089158,0.20388013372673847)]
##point4=[(0.24397475401089158,0.3784580469945782,0.3775671989945304)]
#d.scatter(point1, marker='*', color='black', alpha=1, label=r"$(\frac{1}{2},\frac{1}{2},0)$",s=50)
##d.scatter(point2, marker='*', color='black', alpha=1, label=r"$(1,0,0)$",s=50)
##d.scatter(point3, marker='*', color='black', alpha=1, label=r"$(\frac{1}{3},\frac{2}{3},0)$",s=50)
##d.scatter(point4, marker='*', color='black', alpha=1, label=r"$(0,1,0)$",s=50)
#d.show()

