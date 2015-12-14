# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 15:00:16 2015

@author: hareyakana
"""

import math as m
import random as r
import pylab as p

def c(x):
    return m.cos(x)    
def s(x):
    return m.sin(x)

"""mixing parameters"""
t12=33.48*m.pi/180.0
#sig12up=0.78*m.pi/180.0
#sig12down=0.75*m.pi/180.0
#t12=[]
#
t23=45.9*m.pi/180.0
#sig23up=3.5*m.pi/180.0
#sig23down=3.5*m.pi/180.0
#t23=[]
#
t13=8.50*m.pi/180.0
#sig13up=0.20*m.pi/180.0
#sig13down=0.21*m.pi/180.0
#t13=[]
#
sig=0
#CP=(r.randint(-180,180))*m.pi/180.0
#
#"""iteration"""
#N=100000
#
"""source ratio"""#keep ES+MS+TS=1
ES=2/3
MS=1/3
TS=0

#Ue1=[]
#Ue2=[]
#Ue3=[]
#Um1=[]
#Um2=[]
#Um3=[]
#Ut1=[]
#Ut2=[]
#Ut3=[]
#E1=[]
#E2=[]
#E3=[]
#E=[]
#M1=[]
#M2=[]
#M3=[]
#M=[]
#T1=[]
#T2=[]
#T3=[]
#T=[]
#
#for i in range(N):
#    t12.append(r.gauss(T12,sig12down))
#    t23.append(r.gauss(T23,sig23up))
#    t13.append(r.gauss(T13,sig13up))
#    sig.append((r.randint(-180,180))*m.pi/180.0)
#    Ue1.append(c(t12[i])*c(t13[i])*c(t12[i])*c(t13[i])) #matrix U element, probability amplitude
#    Ue2.append(c(t13[i])*s(t12[i])*c(t13[i])*s(t12[i]))
#    Ue3.append(s(t13[i])*s(t13[i]))
#    Um1.append(s(t12[i])*s(t12[i])*c(t23[i])*c(t23[i])+c(t12[i])*c(t12[i])*s(t23[i])*s(t23[i])*s(t13[i])*s(t13[i])+2*s(t12[i])*c(t23[i])*c(t12[i])*s(t23[i])*s(t13[i])*c(sig[i]))
#    Um2.append(c(t12[i])*c(t12[i])*c(t23[i])*c(t23[i])+s(t12[i])*s(t12[i])*s(t23[i])*s(t23[i])*s(t13[i])*s(t13[i])-2*c(t12[i])*c(t23[i])*s(t12[i])*s(t23[i])*s(t13[i])*c(sig[i]))
#    Um3.append(c(t13[i])*s(t23[i])*c(t13[i])*s(t23[i]))
#    Ut1.append(s(t12[i])*s(t12[i])*s(t23[i])*s(t23[i])+c(t12[i])*c(t12[i])*c(t23[i])*c(t23[i])*s(t13[i])*s(t13[i])-2*s(t12[i])*s(t23[i])*c(t12[i])*c(t23[i])*s(t13[i])*c(sig[i]))
#    Ut2.append(c(t12[i])*c(t12[i])*s(t23[i])*s(t23[i])+s(t12[i])*s(t12[i])*c(t23[i])*c(t23[i])*s(t13[i])*s(t13[i])+2*c(t12[i])*s(t23[i])*s(t12[i])*c(t23[i])*s(t13[i])*c(sig[i]))
#    Ut3.append(c(t13[i])*c(t23[i])*c(t13[i])*c(t23[i]))
#    E1.append(Ue1[i]*Ue1[i]+Ue2[i]*Ue2[i]+Ue3[i]*Ue3[i]) #Nu_e source only
#    E2.append(Ue1[i]*Um1[i]+Ue2[i]*Um2[i]+Ue3[i]*Um3[i])
#    E3.append(Ue1[i]*Ut1[i]+Ue2[i]*Ut2[i]+Ue3[i]*Ut3[i])
#    M1.append(Um1[i]*Ue1[i]+Um2[i]*Ue2[i]+Um3[i]*Ue3[i]) #Nu_mu source only
#    M2.append(Um1[i]*Um1[i]+Um2[i]*Um2[i]+Um3[i]*Um3[i])
#    M3.append(Um1[i]*Ut1[i]+Um2[i]*Ut2[i]+Um3[i]*Ut3[i])
#    T1.append(Ut1[i]*Ue1[i]+Ut2[i]*Ue2[i]+Ut3[i]*Ue3[i]) #Nu_tao source only
#    T2.append(Ut1[i]*Um1[i]+Ut2[i]*Um2[i]+Ut3[i]*Um3[i])
#    T3.append(Ut1[i]*Ut1[i]+Ut2[i]*Ut2[i]+Ut3[i]*Ut3[i])
#    E.append(ES*E1[i]+MS*M1[i]+TS*T1[i]) #Nu_e detected at earth
#    M.append(ES*E2[i]+MS*M2[i]+TS*T2[i]) #Nu_mu detected at earth
#    T.append(ES*E3[i]+MS*M3[i]+TS*T3[i]) #Nu_tao detected at earth
#
#NUE=[]
#NUMU=[]
#NUTAU=[]
#P1=[]
#P2=[]
#D=[]
#for i in range(1000):
#    NUE.append(0)
#    NUMU.append(0)
#    NUTAU.append(0)
#    D.append(0)
#    P1.append(i/1000)
#    P2.append(i/1000+0.001)
#
#for i in range(1000):    
#    for j in range(N):
#        if P1[i]<E[j] and E[j]<P2[i]:
#            NUE[i]=(NUE[i]+1)
#        if P1[i]<M[j] and M[j]<P2[i]:
#            NUMU[i]=(NUMU[i]+1)
#        if P1[i]<T[j] and T[j]<P2[i]:
#            NUTAU[i]=(NUTAU[i]+1)
#        else:
#            D[i]=D[i]+1
#nue=[]
#numu=[]
#nutau=[]
#for i in range(1000):
#    nue.append(NUE[i]/N)
#    numu.append(NUMU[i]/N)
#    nutau.append(NUTAU[i]/N)
#
#p.title(r"$(\nu_e,\nu_\mu,\nu_\tau)=(\frac{1}{4},\frac{3}{4},0)$",fontsize=15)
#p.xlabel("probability")
#p.ylabel(r"$\nu_e,\nu_\mu,\nu_\tau$")
#p.step(P1,nue,label=r"$\nu_e$")
#p.step(P1,numu,label=r"$\nu_\mu$")
#p.step(P1,nutau,label=r"$\nu_\tau$")
#p.legend()
#    
"""best fit values"""
Ue1=(c(t12)*c(t13)*c(t12)*c(t13)) #matrix U element, probability amplitude
Ue2=(c(t13)*s(t12)*c(t13)*s(t12))
Ue3=(s(t13)*s(t13))
Um1=(s(t12)*s(t12)*c(t23)*c(t23)+c(t12)*c(t12)*s(t23)*s(t23)*s(t13)*s(t13)+2*s(t12)*c(t23)*c(t12)*s(t23)*s(t13)*c(sig))
Um2=(c(t12)*c(t12)*c(t23)*c(t23)+s(t12)*s(t12)*s(t23)*s(t23)*s(t13)*s(t13)-2*c(t12)*c(t23)*s(t12)*s(t23)*s(t13)*c(sig))
Um3=(c(t13)*s(t23)*c(t13)*s(t23))
Ut1=(s(t12)*s(t12)*s(t23)*s(t23)+c(t12)*c(t12)*c(t23)*c(t23)*s(t13)*s(t13)-2*s(t12)*s(t23)*c(t12)*c(t23)*s(t13)*c(sig))
Ut2=(c(t12)*c(t12)*s(t23)*s(t23)+s(t12)*s(t12)*c(t23)*c(t23)*s(t13)*s(t13)+2*c(t12)*s(t23)*s(t12)*c(t23)*s(t13)*c(sig))
Ut3=(c(t13)*c(t23)*c(t13)*c(t23))
E1=(Ue1*Ue1+Ue2*Ue2+Ue3*Ue3) #Nu_e source only
E2=(Ue1*Um1+Ue2*Um2+Ue3*Um3)
E3=(Ue1*Ut1+Ue2*Ut2+Ue3*Ut3)
M1=(Um1*Ue1+Um2*Ue2+Um3*Ue3) #Nu_mu source only
M2=(Um1*Um1+Um2*Um2+Um3*Um3)
M3=(Um1*Ut1+Um2*Ut2+Um3*Ut3)
T1=(Ut1*Ue1+Ut2*Ue2+Ut3*Ue3) #Nu_tao source only
T2=(Ut1*Um1+Ut2*Um2+Ut3*Um3)
T3=(Ut1*Ut1+Ut2*Ut2+Ut3*Ut3)
E=(ES*E1+MS*M1+TS*T1) #Nu_e detected at earth
M=(ES*E2+MS*M2+TS*T2) #Nu_mu detected at earth
T=(ES*E3+MS*M3+TS*T3) #Nu_tao detected at earth
print(E,M,T)