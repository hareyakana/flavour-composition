# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 00:27:24 2015

@author: hareyakana
"""
import ternary as t
import pylab as p
import os

grid=1

"""Loads sample heatmap data."""
#def load_sample_heatmap_data1(filename="heatmap110.txt"):
#    full_filename = os.path.join(filename)
#    data = dict()
#    handle = open(full_filename)
#    for line in handle:
#        line = line.strip()
#        i, j, k, v = line.split(' ')
#        data[(float(i), float(j), float(k))] = float(v)
#    return data

#def load_sample_heatmap_data2(filename="heatmap120.txt"):
#    full_filename = os.path.join(filename)
#    data = dict()
#    handle = open(full_filename)
#    for line in handle:
#        line = line.strip()
#        i, j, k, v = line.split(' ')
#        data[(float(i), float(j), float(k))] = float(v)
#    return data
#
#def load_sample_heatmap_data3(filename="heatmap100.txt"):
#    full_filename = os.path.join(filename)
#    data = dict()
#    handle = open(full_filename)
#    for line in handle:
#        line = line.strip()
#        i, j, k, v = line.split(' ')
#        data[(float(i), float(j), float(k))] = float(v)
#    return data

#def load_sample_heatmap_data4(filename="heatmap010.txt"):
#    full_filename = os.path.join(filename)
#    data = dict()
#    handle = open(full_filename)
#    for line in handle:
#        line = line.strip()
#        i, j, k, v = line.split(' ')
#        data[(float(i), float(j), float(k))] = float(v)
#    return data

#data1 = load_sample_heatmap_data1()
#data2 = load_sample_heatmap_data2()
#data3 = load_sample_heatmap_data3()
#data4 = load_sample_heatmap_data4()
    
"""heatmap"""
figure, d=t.figure(scale=grid)
d.boundary(linewidth=2)
d.gridlines(multiple=0.1,color="blue",linewidth=0.8)
d.set_title(r"source flavour composition $(\nu_e,\nu_\mu,\nu_\tau)=(\frac{1}{2},\frac{1}{2},0)$",fontsize=20)
d.left_axis_label(r"$\nu_\tau$",offset=0.12)
d.right_axis_label(r"$\nu_\mu$",offset=0.1)
d.bottom_axis_label(r"$\nu_e$",offset=0)
#d._redraw_labels()
d.ticks(axis='brl',multiple=0.1)
p.axis('off')
#d.heatmap(data1,style="triangular")
#d.boundary()
#d.heatmap(data2,style="triangular")
#d.heatmap(data3,style="hexagonal",cmap='Blues')
#d.heatmap(data4,style="triangular",cmap='viridis')                
#d.resize_drawing_canvas(scale=1.15)

#point1=[(0.3980599331366308,0.3112164005027349,0.2907236663606344)]
#point2=[(0.34669820676138435,0.3336302826666826,0.31967151057193305)]
#point3=[(0.55214511226237,0.24397475401089158,0.20388013372673847)]
#point4=[(0.24397475401089158,0.3784580469945782,0.3775671989945304)]
#d.scatter(point1, marker='*', color='black', alpha=1, label=r"$(\frac{1}{2},\frac{1}{2},0)$",s=50)
#d.scatter(point2, marker='*', color='black', alpha=1, label=r"$(1,0,0)$",s=50)
#d.scatter(point3, marker='*', color='black', alpha=1, label=r"$(\frac{1}{3},\frac{2}{3},0)$",s=50)
#d.scatter(point4, marker='*', color='black', alpha=1, label=r"$(0,1,0)$",s=50)
d.show()
