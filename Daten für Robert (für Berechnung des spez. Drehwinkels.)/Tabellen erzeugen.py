
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



#print (data)

tmp=[]  #### leeren Array zum speichern erzeugen
for n in range (13):
    tmp.append([])

CO=''
print (12) 

###### txt dateien in Array sortiert speichern
for n in range (12):
        for i in range (8):
            tmp[n].append(data[i][n][0])
        tmp[n].append(" bei "+str(data[i][n][1])+" nm")    
    
    #### ein weiterer für die Konzentrationen
for i in range (7):
    tmp[12].append(konz[i][0])
tmp[12].append(" konzentrationen")   
print (tmp)


#### speichern in einer txt Datei
f = open('workfile.txt', 'w')
for item in tmp:
    f.write("%s\n" % item)
f.close()
