#!/usr/bin/env python

"""
Plotting data
"""
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import pylab





###MAGNETIZATION OF SYSTEM OVER TIME DISTINCT TEMPERATURES.###
m1, it001 = np.loadtxt("m1.txt", unpack = True)
Mag_01TC, it01 = np.loadtxt("mag01.txt", unpack= True)
MagTC, itTC = np.loadtxt("magTC.txt", unpack= True)
Mag1_5TC, it1_5 = np.loadtxt("magTC1_5.txt", unpack = True)
Mag15TC, it15 = np.loadtxt("magTC15.txt", unpack= True)

m1 = m1/-1600 #Dividing by size*size in order that full magnetization = unity. Division by -1 in cases where the lattice has magnetized downward/antiparallel.
Mag_01TC = Mag_01TC/1600
MagTC = MagTC/1600
Mag1_5TC = Mag1_5TC/-1600
Mag15TC = Mag15TC/1600

pylab.plot(m1, it001,'b-', markersize = 1.5, label='$\ 0.001 TC$')
pylab.plot(Mag_01TC, it01, 'g-',label='$\ 0.01 TC$')
pylab.plot(MagTC, itTC, 'r-',label='$TC$')
pylab.plot(Mag1_5TC, it1_5, 'c-',label='$\ 1.5 TC$')
pylab.plot(Mag15TC, it15, 'm-',label='$\ 15 TC$')
pylab.ylim([-1.0,1.0])
pylab.xlim([0,1000000])
pylab.title('Magnetization of system over time.',fontsize=20)
pylab.xlabel('Iteration', fontsize=20)
pylab.ylabel('Magnetization' ,fontsize=20)
pylab.legend(bbox_to_anchor=(1.,0.4),prop={'size':20})
plt.show()

#GRAPH OF MAGNETIZATION VS TEMPERATURE FOR THREE DISTINCE LATTICE SIZES

'''
#Lattice of side 50
x_40,y_40 = np.loadtxt("MvT50.txt", unpack = True)
x_40= (np.sqrt(x_40 ** 2))/2500 #Ensuring that the unpacked numbers are positivr

#Lattice of side 20
x_20,y_20 = np.loadtxt("MvT20.txt", unpack = True)
x_20 = (np.sqrt(x_20 ** 2))/400

#Lattice of side 10
x_10,y_10 = np.loadtxt("MvT10.txt", unpack = True)
x_10 = (np.sqrt(x_10 ** 2))/100

z_40 = np.polyfit(y_40,x_40,10)  
p_40 = np.poly1d(z_40)

z_20 = np.polyfit(y_20,x_20,10) 
p_20 = np.poly1d(z_20)

z_10 = np.polyfit(y_10,x_10,10)  
p_10 = np.poly1d(z_10)

yy = np.linspace(1.2,3.8,100)

pylab.plot(y_40,x_40,'c.', markersize = 2.5) and pylab.plot(yy, p_40(yy), '-c',linewidth = 1,label = 'Size = 40')
pylab.plot(y_20,x_20, 'r*', markersize = 2.5) and pylab.plot( yy, p_20(yy), '-r',linewidth = 1,label = 'Size = 25')
pylab.plot(y_10,x_10, 'k^', markersize = 2.5) and pylab.plot( yy, p_10(yy), '-k',linewidth = 1,label = 'Size = 10')
plt.title('Magnetization of system versus temperature',fontsize=20)
plt.xlabel('Temperature',fontsize = 20)
plt.ylabel('Magnetization',fontsize = 20)
pylab.legend(bbox_to_anchor=(1,1),prop={'size':10})
'''





#GRAPH OF ENERGY VERSUS TEMPERATURE FOR THREE DISTINCT LATTICE SIZES###
'''
x15,y15 = np.loadtxt("EvT15.txt", unpack = True)
x10,y10 = np.loadtxt("EvT10.txt", unpack = True)
x5,y5 = np.loadtxt("EvT5.txt", unpack = True )
x2,y2 = np.loadtxt("EvT2.txt", unpack = True)

z15 = np.polyfit(y15,x15,8)
p15 = np.poly1d(z15)  

z10 = np.polyfit(y10,x_10,8)  
p10 = np.poly1d(z10)

z5 = np.polyfit(y5,x5,8)  
p5 = np.poly1d(z5)

z2 = np.polyfit(y2,x2,8) 
p2 = np.poly1d(z2)

yy = np.linspace(0.8,6,100)
yy2 = np.linspace(0.8,4.5,100)

pylab.plot(y15,x15,'b.', markersize = 2.5) and pylab.plot(yy, p15(yy), '-b',linewidth = 1,label = 'Size = 15')
pylab.plot(y10,x10,'^g', markersize = 2.5) and pylab.plot(yy, p10(yy), '-g',linewidth = 1,label = 'Size = 10')
pylab.plot(y5,x5, '*r', markersize = 2.5) and pylab.plot( yy2, p5(yy2), '-r',linewidth = 1,label = 'Size = 5')
pylab.plot(y2,x2, 'ok', markersize = 2.5) and pylab.plot( yy, p2(yy), '-k',linewidth = 1,label = 'Size = 2')

plt.title('Energy versus temperature per site',fontsize=20)
plt.xlabel('Temperature',fontsize = 20)
plt.ylabel('Energy',fontsize = 20)
plt.legend(bbox_to_anchor=(1,0.4),prop={'size':10})
'''



#Graph for specific Heat

'''
c_5, t_5 = np.loadtxt('C5.txt', unpack = True)
c_10, t_10 = np.loadtxt('C10.txt', unpack = True)
c_20, t_20 = np.loadtxt('C20.txt', unpack = True)



pylab.plot(t_5, c_5, 'c.', markersize = 2.5, label = 'L = 5')
pylab.plot(t_10, c_10, 'k*', markersize = 2.5, label = 'L = 10')
pylab.plot(t_20, c_20, 'g^', markersize = 2.5, label = 'L = 20')
plt.plot((2.269, 2.269), (0.0, 5.0), '-k')

plt.title('Specific Heat versus temperature', fontsize = 20)
plt.xlabel('Temperature', fontsize=20)
plt.ylabel('Specific Heat', fontsize=20)
plt.legend(bbox_to_anchor=(1,1.0),prop={'size':10})


plt.show()
'''








plt.show()

