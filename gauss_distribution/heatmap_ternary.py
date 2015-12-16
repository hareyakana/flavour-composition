# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 00:27:24 2015

@author: hareyakana
"""
import ternary as t
import pylab as p
import os
import csv


scale=400

"""Loads sample heatmap data."""
def load_sample_heatmap_data1(filename="heatmap110.txt"):
    full_filename = os.path.join(filename)
    data = dict()
    handle = open(full_filename)
    for line in handle:
        line = line.strip()
        i, j, k, v = line.split(',')
        data[(int(scale*float(i)), int(scale*float(j)), int(scale*float(k)))] = float(v)
    return data

def load_sample_heatmap_data2(filename="heatmap120.txt"):
    full_filename = os.path.join(filename)
    data = dict()
    handle = open(full_filename)
    for line in handle:
        line = line.strip()
        i, j, k, v = line.split(',')
        data[(int(scale*float(i)), int(scale*float(j)), int(scale*float(k)))] = float(v)
    return data

def load_sample_heatmap_data3(filename="heatmap100.txt"):
    full_filename = os.path.join(filename)
    data = dict()
    handle = open(full_filename)
    for line in handle:
        line = line.strip()
        i, j, k, v = line.split(',')
        data[(int(scale*float(i)), int(scale*float(j)), int(scale*float(k)))] = float(v)
    return data

def load_sample_heatmap_data4(filename="heatmap010.txt"):
    full_filename = os.path.join(filename)
    data = dict()
    handle = open(full_filename)
    for line in handle:
        line = line.strip()
        i, j, k, v = line.split(',')
        data[(int(scale*float(i)), int(scale*float(j)), int(scale*float(k)))] = float(v)
    return data

def load_sample_heatmap_data5(filename="heatmap210.txt"):
    full_filename = os.path.join(filename)
    data = dict()
    handle = open(full_filename)
    for line in handle:
        line = line.strip()
        i, j, k, v = line.split(',')
        data[(int(scale*float(i)), int(scale*float(j)), int(scale*float(k)))] = float(v)
    return data

data1 = load_sample_heatmap_data1()
data2 = load_sample_heatmap_data2()
data3 = load_sample_heatmap_data3()
data4 = load_sample_heatmap_data4()
data5 = load_sample_heatmap_data5()

"""coordinate system"""
#B=[] #bottom axis
#R=[] #right axis
#L=[] #left axis
#BRL=[]
#with open('ternary_coordinate1000.txt','r')as f:
#    reader = csv.DictReader(f)
#    for row in reader:
#        BRL.append((float("%.3f" % float(row['x'])),float("%.3f" % float(row['y'])),float("%.3f" % float(row['z']))))

"""scatter heatmap"""
#E110=[]
#M110=[]
#T110=[]
#w110=[]
#    
#with open('heatmap110.txt','r')as f:
#    reader = csv.DictReader(f)
#    for row in reader:
#        E110.append(float("%.3f" % float(row['x'])))
#        M110.append(float("%.3f" % float(row['y'])))
#        T110.append(float("%.3f" % float(row['z'])))
#        w110.append(float("%.3f" % float(row['w'])))
#
#E120=[]
#M120=[]
#T120=[]
#w120=[]
#    
#with open('heatmap120i.txt','r')as f:
#    reader = csv.DictReader(f)
#    for row in reader:
#        E120.append(float("%.3f" % float(row['x'])))
#        M120.append(float("%.3f" % float(row['y'])))
#        T120.append(float("%.3f" % float(row['z'])))
#        w120.append(float("%.3f" % float(row['w'])))
#        
#E100=[]
#M100=[]
#T100=[]
#w100=[]
#    
#with open('heatmap100i.txt','r')as f:
#    reader = csv.DictReader(f)
#    for row in reader:
#        E100.append(float("%.3f" % float(row['x'])))
#        M100.append(float("%.3f" % float(row['y'])))
#        T100.append(float("%.3f" % float(row['z'])))
#        w100.append(float("%.3f" % float(row['w'])))
#
#E010=[]
#M010=[]
#T010=[]
#w010=[]
#    
#with open('heatmap010i.txt','r')as f:
#    reader = csv.DictReader(f)
#    for row in reader:
#        E010.append(float("%.3f" % float(row['x'])))
#        M010.append(float("%.3f" % float(row['y'])))
#        T010.append(float("%.3f" % float(row['z'])))
#        w010.append(float("%.3f" % float(row['w'])))
#
#E210=[]
#M210=[]
#T210=[]
#w210=[]
#    
#with open('heatmap210i.txt','r')as f:
#    reader = csv.DictReader(f)
#    for row in reader:
#        E210.append(float("%.3f" % float(row['x'])))
#        M210.append(float("%.3f" % float(row['y'])))
#        T210.append(float("%.3f" % float(row['z'])))
#        w210.append(float("%.3f" % float(row['w'])))

point1=[(0.3980599331366308,0.3112164005027349,0.2907236663606344)]
point2=[(0.34669820676138435,0.3336302826666826,0.31967151057193305)]
point3=[(0.55214511226237,0.24397475401089158,0.20388013372673847)]
point4=[(0.24397475401089158,0.3784580469945782,0.3775671989945304)]
democratic=[(1/3,1/3,1/3)]
point5=[(0.4494216595118771,0.2888025183387871,0.26177582214933576)]
ice1=[(0,0.2,0.8)]
ice2=[(0.18,0.41,0.41)]

"""ternary settings"""
figure, d=t.figure(scale=scale)
d.boundary(linewidth=2)
d.gridlines(multiple=scale/10,color="blue",linewidth=0.2)
d.set_title(r"source flavour composition ",fontsize=20)
d.left_axis_label(r"$\nu_\tau$",offset=0.12,fontsize=20)
d.right_axis_label(r"$\nu_\mu$",offset=0.1,fontsize=20)
d.bottom_axis_label(r"$\nu_e$",offset=0,fontsize=20)
d._redraw_labels()
ticks = [round(i / float(10), 1) for i in range(10+1)]
d.ticks(ticks=ticks)
p.axis('off')

"""scatter version"""
#max110=max(w110)
#max100=max(w100)
#max120=max(w120)
#max010=max(w010)
#max210=max(w210)
#for x in range(len(BRL)):
#    if w110[x]>0 and w110[x]<=0.135*max110:
#        d.scatter([BRL[x]], marker='.', color='#B0E0E6', alpha=0.5, s=5) 
#    if w110[x]>0.135*max110 and w110[x]<=0.606*max110:
#        d.scatter([BRL[x]], marker='.', color='#00BFFF', alpha=1, s=5)
#    if w110[x]>0.606*max110:
#        d.scatter([BRL[x]], marker='.', color='#0000FF', alpha=0.5, s=5)
#    
#    if w100[x]>0 and w100[x]<=0.135*max100:
#        d.scatter([BRL[x]], marker='.', color='#EE82EE', alpha=0.5, s=5)    
#    if w100[x]>0.135*max100 and w100[x]<=0.606*max100:
#        d.scatter([BRL[x]], marker='.', color='#9370DB', alpha=0.5, s=5)
#    if w100[x]>0.606*max100:
#        d.scatter([BRL[x]], marker='.', color='#6A5ACD', alpha=0.5, s=5)    
#   
#    if w120[x]>0 and w120[x]<=0.135*max120:
#        d.scatter([BRL[x]], marker='.', color='#FFA07A', alpha=0.5, s=5)    
#    if w120[x]>0.135*max120 and w120[x]<=0.606*max120:
#        d.scatter([BRL[x]], marker='.', color='#CD5C5C', alpha=0.5, s=5)
#    if w120[x]>0.606*max120:
#        d.scatter([BRL[x]], marker='.', color='#FF0000', alpha=0.5, s=5)
#        
#    if w010[x]>0 and w010[x]<=0.135*max010:
#        d.scatter([BRL[x]], marker='.', color='#FFEFD5', alpha=0.5, s=5)
#    if w010[x]>0.135*max010 and w010[x]<=0.606*max010:
#        d.scatter([BRL[x]], marker='.', color='#F0E68C', alpha=0.5, s=5)
#    if w010[x]>0.606*max010:
#        d.scatter([BRL[x]], marker='.', color='#FFFF00', alpha=0.5, s=5)
#    
#    if w210[x]>0 and w210[x]<=0.135*max210:
#        d.scatter([BRL[x]], marker='.', color='#98FB98', alpha=0.5, s=5)
#    if w210[x]>0.135*max210 and w210[x]<=0.606*max210:
#        d.scatter([BRL[x]], marker='.', color='#32CD32', alpha=0.5, s=5)
#    if w210[x]>0.606*max210:
#        d.scatter([BRL[x]], marker='.', color='#2E8B57', alpha=0.5, s=5)
#    else:
#        pass
#
#
#d.scatter(point1, marker='D', color='#000080', alpha=1, 
#          label=r"$(\frac{1}{2},\frac{1}{2},0)$",s=50)
#d.scatter(point3, marker='o', color='#663399', alpha=1, 
#          label=r"$(1,0,0)$",s=50)
#d.scatter(point2, marker='^', color='#8B0000', alpha=1, 
#          label=r"$(\frac{1}{3},\frac{2}{3},0)$",s=50)
#d.scatter(point4, marker='s', color='#FF4500', alpha=1, 
#          label=r"$(0,1,0)$",s=50)
#d.scatter(democratic,marker='*',color='black',
#          label=r"$(\frac{1}{3},\frac{1}{3},\frac{1}{3})$",s=50)
#d.scatter(point5, marker='d',color='#006400',alpha=1,
#          label=r"$(\frac{2}{3},\frac{1}{3},0)$",s=50)
#d.scatter(ice1, marker='+',label='icecube 1', s=200)
#d.scatter(ice2, marker='x',label='icecube 2', s=100)
#d.legend()

"""heatmap"""


d.heatmap(data1,style="hexagonal",cmap='plasma',colorbar=True)
#d.scatter(point1, marker='*', color='black', alpha=1, 
#          label=r"$(\frac{1}{2},\frac{1}{2},0)$",s=50)
#
#d.heatmap(data2,style='hexagonal',cmap='plasma',colorbar=None)
#d.scatter(point2, marker='*', color='black', alpha=1, 
#          label=r"$(1,0,0)$",s=50)
#          
#d.heatmap(data3,style="hexagonal",cmap='plasma',colorbar=None)
#d.scatter(point3, marker='*', color='black', alpha=1, 
#          label=r"$(\frac{1}{3},\frac{2}{3},0)$",s=50)
          
#d.heatmap(data4,style="hexagonal",cmap='plasma',colorbar=None)                
#d.scatter(point4, marker='*', color='black', alpha=1, 
#          label=r"$(0,1,0)$",s=50)
          
#d.heatmap(data5,style="hexagonal",cmap='plasma',colorbar=None)
#d.scatter(democratic,marker='+',color='black',
#          label=r"$(\frac{1}{3},\frac{1}{3},\frac{1}{3})$",s=100)
#d.resize_drawing_canvas(scale=1.15)
#figure.colorbar(ax='bottom',mappable=None)
