# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 15:00:16 2015

@author: hareyakana
"""
"""CHANGE THE SOURCE RATIO/FILENAME"""
#

import math as m
import random as r
import pylab as p
import ternary as t
import csv
import numpy as np
import matplotlib as cm

def c(x):
    return m.cos(x)    
def s(x):
    return m.sin(x)

"""mixing parameters"""
T12=33.48*m.pi/180.0
sig12up=0.78*m.pi/180.0
sig12down=0.75*m.pi/180.0
t12=[]

T23=45.9*m.pi/180.0
sig23up=3.5*m.pi/180.0
sig23down=1.6*m.pi/180.0
t23=[]

T13=8.50*m.pi/180.0
sig13up=0.20*m.pi/180.0
sig13down=0.21*m.pi/180.0
t13=[]

sig=[]
CP=(r.uniform(-180,180))*m.pi/180.0

"""iteration"""
N=40000

"""source ratio"""#keep ES+MS+TS=1
ES110=1/2 #110
MS110=1/2
TS110=0
ES100=1 #100
MS100=0
TS100=0
ES120=1/3 #120
MS120=2/3
TS120=0
ES010=0 #010
MS010=1
TS010=0
ES210=2/3
MS210=1/3
TS210=0

Ue1=[]
Ue2=[]
Ue3=[]
Um1=[]
Um2=[]
Um3=[]
Ut1=[]
Ut2=[]
Ut3=[]
E1=[]
E2=[]
E3=[]
M1=[]
M2=[]
M3=[]
T1=[]
T2=[]
T3=[]
E110=[]
M110=[]
T110=[]
E100=[]
M100=[]
T100=[]
E120=[]
M120=[]
T120=[]
E010=[]
M010=[]
T010=[]
E210=[]
M210=[]
T210=[]
data1=[]
data2=[]
data3=[]
data4=[]
data5=[]

for i in range(N):
    t12.append(T12)
    t23.append(r.gauss(T23,sig23up))
    t13.append(r.gauss(T13,sig13up))
    sig.append((r.gauss(0,180))*m.pi/180.0)
    Ue1.append(c(t12[i])*c(t13[i])*c(t12[i])*c(t13[i])) #matrix U element, probability amplitude
    Ue2.append(c(t13[i])*s(t12[i])*c(t13[i])*s(t12[i]))
    Ue3.append(s(t13[i])*s(t13[i]))
    Um1.append(s(t12[i])*s(t12[i])*c(t23[i])*c(t23[i])+c(t12[i])*c(t12[i])*s(t23[i])*s(t23[i])*s(t13[i])*s(t13[i])+2*s(t12[i])*c(t23[i])*c(t12[i])*s(t23[i])*s(t13[i])*c(sig[i]))
    Um2.append(c(t12[i])*c(t12[i])*c(t23[i])*c(t23[i])+s(t12[i])*s(t12[i])*s(t23[i])*s(t23[i])*s(t13[i])*s(t13[i])-2*c(t12[i])*c(t23[i])*s(t12[i])*s(t23[i])*s(t13[i])*c(sig[i]))
    Um3.append(c(t13[i])*s(t23[i])*c(t13[i])*s(t23[i]))
    Ut1.append(s(t12[i])*s(t12[i])*s(t23[i])*s(t23[i])+c(t12[i])*c(t12[i])*c(t23[i])*c(t23[i])*s(t13[i])*s(t13[i])-2*s(t12[i])*s(t23[i])*c(t12[i])*c(t23[i])*s(t13[i])*c(sig[i]))
    Ut2.append(c(t12[i])*c(t12[i])*s(t23[i])*s(t23[i])+s(t12[i])*s(t12[i])*c(t23[i])*c(t23[i])*s(t13[i])*s(t13[i])+2*c(t12[i])*s(t23[i])*s(t12[i])*c(t23[i])*s(t13[i])*c(sig[i]))
    Ut3.append(c(t13[i])*c(t23[i])*c(t13[i])*c(t23[i]))
    E1.append(Ue1[i]*Ue1[i]+Ue2[i]*Ue2[i]+Ue3[i]*Ue3[i]) #Nu_e source only
    E2.append(Ue1[i]*Um1[i]+Ue2[i]*Um2[i]+Ue3[i]*Um3[i])
    E3.append(Ue1[i]*Ut1[i]+Ue2[i]*Ut2[i]+Ue3[i]*Ut3[i])
    M1.append(Um1[i]*Ue1[i]+Um2[i]*Ue2[i]+Um3[i]*Ue3[i]) #Nu_mu source only
    M2.append(Um1[i]*Um1[i]+Um2[i]*Um2[i]+Um3[i]*Um3[i])
    M3.append(Um1[i]*Ut1[i]+Um2[i]*Ut2[i]+Um3[i]*Ut3[i])
    T1.append(Ut1[i]*Ue1[i]+Ut2[i]*Ue2[i]+Ut3[i]*Ue3[i]) #Nu_tao source only
    T2.append(Ut1[i]*Um1[i]+Ut2[i]*Um2[i]+Ut3[i]*Um3[i])
    T3.append(Ut1[i]*Ut1[i]+Ut2[i]*Ut2[i]+Ut3[i]*Ut3[i])
    E110.append(ES110*E1[i]+MS110*M1[i]+TS110*T1[i]) 
    M110.append(ES110*E2[i]+MS110*M2[i]+TS110*T2[i]) 
    T110.append(ES110*E3[i]+MS110*M3[i]+TS110*T3[i]) 
    data1.append((E110[i],M110[i],T110[i]))
    E100.append(ES100*E1[i]+MS100*M1[i]+TS100*T1[i]) 
    M100.append(ES100*E2[i]+MS100*M2[i]+TS100*T2[i]) 
    T100.append(ES100*E3[i]+MS100*M3[i]+TS100*T3[i]) 
    data2.append((E100[i],M100[i],T100[i]))
    E120.append(ES120*E1[i]+MS120*M1[i]+TS120*T1[i]) 
    M120.append(ES120*E2[i]+MS120*M2[i]+TS120*T2[i]) 
    T120.append(ES120*E3[i]+MS120*M3[i]+TS120*T3[i]) 
    data3.append((E120[i],M120[i],T120[i]))
    E010.append(ES010*E1[i]+MS010*M1[i]+TS010*T1[i]) 
    M010.append(ES010*E2[i]+MS010*M2[i]+TS010*T2[i]) 
    T010.append(ES010*E3[i]+MS010*M3[i]+TS010*T3[i]) 
    data4.append((E010[i],M010[i],T010[i]))
    E210.append(ES210*E1[i]+MS210*M1[i]+TS210*T1[i]) 
    M210.append(ES210*E2[i]+MS210*M2[i]+TS210*T2[i]) 
    T210.append(ES210*E3[i]+MS210*M3[i]+TS210*T3[i]) 
    data5.append((E210[i],M210[i],T210[i]))

NUE=[]
NUMU=[]
NUTAU=[]
P1=[]
P2=[]
D=[]
for i in range(1000):
    NUE.append(0)
    NUMU.append(0)
    NUTAU.append(0)
    D.append(0)
    P1.append(i/1000)
    P2.append(i/1000+0.001)

for i in range(1000):    
    for j in range(N):
        if P1[i]<E110[j] and E110[j]<P2[i]:
            NUE[i]=(NUE[i]+1)
        if P1[i]<M110[j] and M110[j]<P2[i]:
            NUMU[i]=(NUMU[i]+1)
        if P1[i]<T110[j] and T110[j]<P2[i]:
            NUTAU[i]=(NUTAU[i]+1)
        else:
            D[i]=D[i]+1
nue=[]
numu=[]
nutau=[]
for i in range(1000):
    nue.append(NUE[i]/N)
    numu.append(NUMU[i]/N)
    nutau.append(NUTAU[i]/N)

#p.title(r"$(\nu_e,\nu_\mu,\nu_\tau)=(\frac{1}{2},\frac{1}{2},0)$",fontsize=15)
#p.xlabel("probability")
#p.ylabel(r"$\nu_e,\nu_\mu,\nu_\tau$")
#p.step(P1,nue,label=r"$\nu_e$")
#p.step(P1,numu,label=r"$\nu_\mu$")
#p.step(P1,nutau,label=r"$\nu_\tau$")
#p.legend()

"""ternary plot/triangular plot configuration/settings"""
figure, d=t.figure(scale=1)

d.boundary(linewidth=2)
d.gridlines(multiple=0.1,color="blue",linewidth=0.8)
#d.gridlines(multiple=0.02,color="green",linewidth=0.2)

d.set_title(r"source flavour composition $\nu_e,\nu_\mu,\nu_\tau$",fontsize=20)
d.left_axis_label(r"$\nu_\tau$",fontsize=20,offset=0.12)
d.right_axis_label(r"$\nu_\mu$",fontsize=20,offset=0.1)
d.bottom_axis_label(r"$\nu_e$",fontsize=20,offset=0.01)
d._redraw_labels()

"""data points"""
point1=[(0.3980599331366308,0.3112164005027349,0.2907236663606344)]
point2=[(0.55214511226237,0.24397475401089158,0.20388013372673847)]
point3=[(0.34669820676138435,0.3336302826666826,0.31967151057193305)]
point4=[(0.24397475401089158,0.3784580469945782,0.3775671989945304)]
democratic=[(1/3,1/3,1/3)]
point5=[(0.4494216595118771,0.2888025183387871,0.26177582214933576)]
ice1=[(0,0.2,0.8)]
ice2=[(0.18,0.41,0.41)]

"""plotting the data points"""
d.ticks(axis='brl',multiple=0.1)
p.axis('off')
d.scatter(data1,marker='.', color='#00BFFF', alpha=0.2,s=5)
d.scatter(data2,marker='.', color='#9370DB', alpha=0.2,s=5)
d.scatter(data3,marker='.', color='#FA8072', alpha=0.2,s=5)
#d.scatter(data1,marker='.', color='#00BFFF', alpha=0.2,s=5)
d.scatter(data4,marker='.', color='#FFDAB9', alpha=0.2,s=5)
d.scatter(data5,marker='.', color='#98FB98', alpha=0.2,s=5)

d.scatter(point1, marker='D', color='#000080', alpha=1, 
          label=r"$(\frac{1}{2},\frac{1}{2},0)$",s=50)
d.scatter(point2, marker='o', color='#663399', alpha=1, 
          label=r"$(1,0,0)$",s=50)
d.scatter(point3, marker='^', color='#FF0000', alpha=1, 
          label=r"$(\frac{1}{3},\frac{2}{3},0)$",s=50)
d.scatter(point4, marker='s', color='#FFD700', alpha=1, 
          label=r"$(0,1,0)$",s=50)
d.scatter(democratic,marker='*',color='black',
          label=r"$(\frac{1}{3},\frac{1}{3},\frac{1}{3})$",s=50)
d.scatter(point5, marker='d',color='#32CD32',alpha=1,
          label=r"$(\frac{2}{3},\frac{1}{3},0)$",s=50)
d.scatter(ice1, marker='+',label='icecube 1', s=200)
d.scatter(ice2, marker='x',label='icecube 2', s=100)
d.legend(prop={'size':8},markerscale=0.5)
d.legend()
d.show()



"""wriitng into files"""
with open('110.txt', 'w') as f:
    fieldnames = ['x', 'y','z']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(len(data1)):
        writer.writerow({'x': E110[i], 'y': M110[i],'z':T110[i]})
with open('100.txt', 'w') as f:
    fieldnames = ['x', 'y','z']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(len(data1)):
        writer.writerow({'x': E100[i], 'y': M100[i],'z':T100[i]})
with open('120.txt', 'w') as f:
    fieldnames = ['x', 'y','z']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(len(data1)):
        writer.writerow({'x': E120[i], 'y': M120[i],'z':T120[i]})
with open('010.txt', 'w') as f:
    fieldnames = ['x', 'y','z']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(len(data1)):
        writer.writerow({'x': E010[i], 'y': M010[i],'z':T010[i]})

with open('210.txt', 'w') as f:
    fieldnames = ['x', 'y','z']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(len(data1)):
        writer.writerow({'x': E210[i], 'y': M210[i],'z':T210[i]})   
        
