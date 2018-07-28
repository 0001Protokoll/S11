
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
        'Testreihe 1 Intensitäten bei verschiedenen Wellenlängen.txt',
        'Testreihe 2 Intensitäten bei verschiedenen Wellenlängen.txt',   
        'Testreihe 3 Intensitäten bei verschiedenen Wellenlängen.txt',
        'Testreihe 4 Intensitäten bei verschiedenen Wellenlängen.txt',
        'Testreihe 5 Intensitäten bei verschiedenen Wellenlängen.txt',
        'Testreihe 6 Intensitäten bei verschiedenen Wellenlängen.txt',
        'Testreihe 7 Intensitäten bei verschiedenen Wellenlängen.txt',
        'Testreihe 8 Intensitäten bei verschiedenen Wellenlängen.txt',
        ]

def getData(name):
    
    return np.genfromtxt(str(name), dtype=float, comments='#')
                         
data = [getData(i) for i in names]

konz = np.genfromtxt(str('I_max   bei 589.37 nm vs konzentrationen.txt'), dtype=float)


####Überschrift wird als Marker für die erhaltenen Infos verwendet ... 
Überschrift=np.array([                                                          #n
        'CO',                                                #0
        'HCl',                                               #1
        'HCl CSSD (SCF)',                                         #2
        'HCl CSSD (MP2)',                                         #3
        'HCl CSSD (MP3)',                                         #4
        'CO CSSD (SCF)',                                             #5
        'CO CSSD (MP2)',                                             #6
        'CO CSSD (MP3)', 
        ])
###Latex erlaubt keine leerstellen. Hier werden die Speichernamen der Bilder festgelegt.
Speicher=np.array([                 
         'CO_b3lyp',                                                     #0
        'HCl_b3lyp',                                                     #1
        'HCl_CSSD(SCF)',                                                   #2
        'HCl_CSSD(MP2)',                                                   #3
        'HCl_CSSD(MP3)',                                                   #4
        'CO_CSSD(SCF)',                                                    #5
        'CO_CSSD(MP2)',                                                    #6
        'CO_CSSD(MP3)',
        ])



print (data)
tmp=[]
for n in range (13):
    tmp.append([])

CO=''
print (12) 


for n in range (12):
    #print (data[n])
    
    for i in range (7):
        tmp[n].append(data[i][n][0])
    tmp[n].append(" bei "+str(data[i][n][1])+" nm")    
    
for i in range (7):
    tmp[12].append(konz[i][0])
tmp[12].append(" konzentrationen")   
print (tmp)

f = open('workfile.txt', 'w')
for item in tmp:
    f.write("%s\n" % item)
f.close()
