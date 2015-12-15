# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 11:09:22 2015

@author: hareyakana
"""
import numpy as np
#from scipy import stats
#import pylab as p
#import ternary as t
import csv
import time
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
BRL=[]
with open('ternary_coordinate1000.txt','r')as f:
    reader = csv.DictReader(f)
    for row in reader:
        B.append(float(row['x']))
        R.append(float(row['y']))
        L.append(float(row['z']))
        BRL.append((float(row['x']),float(row['y']),float(row['z'])))


"""data obtained from the generated flavour compositions"""
E110=[]
M110=[]
T110=[]
#data110=[]
    
with open('110fixed23.txt','r')as f:
    reader = csv.DictReader(f)
    for row in reader:
        E110.append(float("%.3f" % float(row['x'])))
        M110.append(float("%.3f" % float(row['y'])))
        T110.append(float("%.3f" % float(row['z'])))
#        data110.append((E110,M110,T110))

E120=[]
M120=[]
T120=[]
#data120=[]
    
with open('120fixed23.txt','r')as f:
    reader = csv.DictReader(f)
    for row in reader:
        E120.append(float("%.3f" % float(row['x'])))
        M120.append(float("%.3f" % float(row['y'])))
        T120.append(float("%.3f" % float(row['z'])))
#        data120.append((E120,M120,T120))
        
E100=[]
M100=[]
T100=[]
#data100=[]
    
with open('100fixed23.txt','r')as f:
    reader = csv.DictReader(f)
    for row in reader:
        E100.append(float("%.3f" % float(row['x'])))
        M100.append(float("%.3f" % float(row['y'])))
        T100.append(float("%.3f" % float(row['z'])))
#        data100.append((E100,M100,T100))


E010=[]
M010=[]
T010=[]
#data010=[]
    
with open('010fixed23.txt','r')as f:
    reader = csv.DictReader(f)
    for row in reader:
        E010.append(float("%.3f" % float(row['x'])))
        M010.append(float("%.3f" % float(row['y'])))
        T010.append(float("%.3f" % float(row['z'])))
#        data010.append((E010,M010,T010))

E210=[]
M210=[]
T210=[]
#data210=[]

with open('210fixed23.txt','r')as f:
    reader = csv.DictReader(f)
    for row in reader:
        E210.append(float("%.3f" % float(row['x'])))
        M210.append(float("%.3f" % float(row['y'])))
        T210.append(float("%.3f" % float(row['z'])))
#        data210.append((E210,M210,T210))

"""binning process of obtained data"""
Coor=len(B)
N=len(E110)

value110=np.zeros(Coor)
value120=np.zeros(Coor)
value100=np.zeros(Coor)
value010=np.zeros(Coor)
value210=np.zeros(Coor)

print(len(BRL),len(E110))

#coor=np.array(BRL)
#data1=np.array(data110)
#data2=np.array(data120)
#data3=np.array(data100)
#data4=np.array(data010)
#data5=np.array(data210)
#he=stats.binned_statistic_dd(test1,data1,statistic='median',bins=len(test1))
#from itertools import slice, zip
dump=[]
for i in range(Coor):
    for k in range(N):
        if E110[k]==B[i] and M110[k]==R[i] and T110[k]==L[i]:
            value110[i]=(value110[i]+1)
        if E120[k]==B[i] and M120[k]==R[i] and T120[k]==L[i]:
            value120[i]=(value120[i]+1)
        if E100[k]==B[i] and M100[k]==R[i] and T100[k]==L[i]:
            value100[i]=(value100[i]+1)
        if E010[k]==B[i] and M010[k]==R[i] and T010[k]==L[i]:
            value010[i]=(value010[i]+1)
        if E210[k]==B[i] and M210[k]==R[i] and T210[k]==L[i]:
            value210[i]=(value210[i]+1)
        else:
            dump.append(0)
v110=[]
v120=[]
v100=[]
v010=[]
v210=[]
#
for i in range(Coor):
    v110.append(float(value110[i]/max(value110)))
    v120.append(float(value120[i]/max(value120)))
    v100.append(float(value100[i]/max(value100)))
    v010.append(float(value010[i]/max(value010)))
    v210.append(float(value210[i]/max(value210)))
    
"""ternary heatmap"""
with open('heatmap110.txt', 'w') as f:
    fieldnames = ['x', 'y','z','w']
    writer = csv.DictWriter(f, delimiter=',',fieldnames=fieldnames)
#    writer.writeheader()
    for i in range(len(B)):
        if v110[i]>0:
            writer.writerow({'x': B[i], 'y': R[i],'z':L[i],'w':v110[i]})
with open('heatmap120.txt', 'w') as f:
    fieldnames = ['x', 'y','z','w']
    writer = csv.DictWriter(f, delimiter=',',fieldnames=fieldnames)
#    writer.writeheader()
    for i in range(len(B)):
        if v120[i]:
            writer.writerow({'x': B[i], 'y': R[i],'z':L[i],'w':v120[i]})
with open('heatmap100.txt', 'w') as f:
    fieldnames = ['x', 'y','z','w']
    writer = csv.DictWriter(f, delimiter=',',fieldnames=fieldnames)
#    writer.writeheader()
    for i in range(len(B)):
        if v100[i]>0:
            writer.writerow({'x': B[i], 'y': R[i],'z':L[i],'w':v100[i]})
with open('heatmap010.txt', 'w') as f:
    fieldnames = ['x', 'y','z','w']
    writer = csv.DictWriter(f, delimiter=',',fieldnames=fieldnames)
#    writer.writeheader()
    for i in range(len(B)):
        if v010[i]>0:
            writer.writerow({'x': B[i], 'y': R[i],'z':L[i],'w':v010[i]})
with open('heatmap210.txt', 'w') as f:
    fieldnames = ['x', 'y','z','w']
    writer = csv.DictWriter(f, delimiter=',',fieldnames=fieldnames)
#    writer.writeheader()
    for i in range(len(B)):
        if v210[i]>0:
            writer.writerow({'x': B[i], 'y': R[i],'z':L[i],'w':v210[i]})

time.time()