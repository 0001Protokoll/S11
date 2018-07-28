

# -*- coding: utf-8 -*-

"""
Created on Sun May  6 17:42:22 2018

@author: David
"""

import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#### wenn mehr dateien geladen werden sollen, einfach Liste erweitern ohne großen Umstand schön und sehr clever! ---verstehen wohl blos einige nicht ...
names = [
        '1.5_10(-5).txt',
        '3_10(-5).txt',
        '5_10(-5).txt',
        '8_10(-5).txt',
        '1_10(-6).txt',
        '3_10(-6).txt',
        '5_10(-6).txt',
        '8_10(-6).txt',
        ]

def getData(name):
    
    return np.genfromtxt(str(name), dtype=float, comments='#')
                         
data = [getData(i) for i in names]

####Überschrift wird als Marker für die erhaltenen Infos verwendet ... 
Überschrift=np.array([                                                          #n
        '$1.5 \\cdot 10^{-5}$',
        '$3 \\cdot 10^{-5}$',
        '$5 \\cdot 10^{-5}$',
        '$8 \\cdot 10^{-5}$',
        '$1 \\cdot 10^{-6}$',
        '$3 \\cdot 10^{-6}$',
        '$5 \\cdot 10^{-6}$',
        '$8 \\cdot 10^{-6}$',
        ])
###Latex erlaubt keine leerstellen. Hier werden die Speichernamen der Bilder festgelegt.
Speicher=np.array([                 
        '1.5_10(-5)_latex.txt',
        '3_10(-5)_latex.txt',
        '5_10(-5)_latex.txt',
        '8_10(-5)_latex.txt',
        '1_10(-6)_latex.txt',
        '3_10(-6)_latex.txt',
        '5_10(-6)_latex.txt',
        '8_10(-6)_latex.txt',
        ])
    
tmp=''

print (data[0])
tmp = '$\\lambda$ in nm' + ' & '
for i in range (len(data)):
    tmp += str(Überschrift[i])
    if i < len(data)-1:
        tmp += ' & '
tmp+= '  \\\\' + '\n'
tmp+='\\hline'+ '\n' + '\\endhead' +'\n'
print (data[0][0][1]) 
print (len(data[0]))
for n in range (len(data[0])):
    tmp += str(data[0][n][0])+ ' & '
    for i in range(len(data)):  
        tmp += ' ' + str(data[i][n][1]) 
        if i < len(data)-1:
            tmp += ' & '
    tmp+=' '+'\\\\'+ '\n'
        
   
print (tmp)

f = open('latextabelleRohdaten.txt', 'w')
f.write(tmp)
f.close()

print (len(data))