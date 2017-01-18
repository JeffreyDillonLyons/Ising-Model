#!/usr/bin/envpython


"""
Implementation of the Metropolis Algorithm for investigation of the two dimensional Ising model.

Jeffrey Lyons

13325575

"""
import numpy as np
import random
import math
import matplotlib.pyplot as plt
from array import array

##Lattice size
##Lattice of side size will have size*size lattice points.
size = 5

'''TOOLBOX'''
#The following function builds our lattice. First creating an array of the desired size populated by zeros. It is then filled with spins whose orientation is chosen by the numpy random choice operator.
def random_lattice(size):
    dir = [-1,1]
    lattice = np.zeros((size,size), int) # Creates lattice of specified size and populates it with zeros. 
    for i in range (size):
        for j in range (size):
            lattice[i][j] = np.random.choice(dir) #Chooses initial spin configuration of sites.
    return lattice
    
lattice = random_lattice((size)) #Lattice building function is called. Lattice is created. 

##Here we code for the periodic boundary condition. Lattice sites on edge will interact with spins on geometrically opposite edge.
def pb(i):
    if i > size-1:
        return 0
    if i < 0:
        return size-1
    else:
        return i
      
#Hamiltion of ithjth spin due to nearest neighbour interactions.
def spin_H(i,j):
    return -1 * lattice[i,j] * (lattice[pb(i+1), j] + lattice[pb(i-1), j]+ lattice[i, pb(j+1)] + lattice[i, pb(j-1)])

#Here we calculate the lattice energy by summing the individual spin hamiltonions and account for quadruple counting. 
def lattice_energy(lattice):
    E_lattice = 0
    for i in range(size):
        for j in range (size):
            E_lattice += spin_H(i,j)
    return E_lattice/4

###Sums rows and columns in order to calculate the magnetizaion of the system. The effect of opposite spins will cancel as in physical reality.###
def mag(lattice):
    mag = sum(sum(lattice)) #
    return mag

'''Metropolis Algorithm'''
#Here we implement the metropolis algorithm which is the backbone of this investigation and the source of all numerical data. The follwing function will also calculate and write specified data at predetermined points. 

def metro(it,T, k, J):
    Energy = E1 = E = E_2 = C = Mag = M1 = M_2 = Magnet = X = 0 
    equil = 50000.0 #Equilibration time. Number of iterations before the algorithm proceeds to take measurements.
    lattice_list = list(xrange(size))
    for step in range(it*100000):#To ensure the number of iterations is above certain level/More convenient to enter small integers for raw input.
        i = np.random.choice(lattice_list,1) #Choose random lattice index[i]
        j = np.random.choice(lattice_list,1) #Choose random lattice index[j]
        flipcost = spin_H(i,j)*J*2 #Energy cost of flipping single spin.
        if flipcost >= 0 or (flipcost < 0 and np.exp(flipcost/(k*T)) >= random.random()): #Calculates Boltzmann factor for flipping spin.
            lattice[i,j] = -1*lattice[i,j] #Flips spin if it is energetically favourable.
        else:  
            lattice[i,j] = lattice[i,j]

        if step > equil:
 
            Energy = lattice_energy(lattice)
            E1 = E1 + Energy
            E = E1/((it - equil)*size*size) #Calculates energy per spin										
            E_2 = E_2 + E**2 #Calculation of E^2 for use as <E^2>
            C = (E_2/(it - equil) - E1*E1 / (it - equil)**2)/(size*T*T) #Calculates specific heat capacity of the 								
            Mag = mag(lattice)
            M1 = M1 + Mag
	    M_2 = M_2 + M_2*M_2
            Magnet = M1/((it - equil)) + 0.0 #Calculates average magnetization per spin.
            

    return str(E) + " " + str((Magnet)/size**2) + " " + str(C)
    
    
     
    
def data_maker(ts,end,it,inc):  #For production of data regarding observables as function of temperature.
	with open('data.txt', 'w') as f: #Opens file before loop. Solves overwriting problem.
		while end > ts:
			random_lattice(size)
			ans = metro(it,ts,1.0,1.0) #Calling the metro function which will institute the metropolis algorithm and return mesurements of observable
			f.write(str(ans) + " " + str(ts) + "\n") #For the desired observable only the others may be #'d out in the metro function and the return line altered. This also serves to optimize the code.
			print ans  
			ts = ts + inc #Increments temperature for next cycle.
		
def data(ts, end, it, inc):
	fig = plt.figure(figsize=(35,7), dpi=100)
	with open('output.txt', 'w') as f:
		while end > ts:
			random_lattice(size)
			ans = metro(it,ts,1.0,1.0) #Calling the metro function which will institute the metropolis algorithm and return mesurements of observable
			f.write(str(ans) + " " + str(ts) + "\n") #For the desired observable only the others may be #'d out in the metro function and the return line altered. This also serves to optimize the code.
			print str(ans) #Provides print out of each step to ensure the function is working properly. Long run times demand surety. 
			ts = ts + inc #Increments temperature for next cycle.       
		 
	E, C, Magnet, temp = np.loadtxt('output.txt', unpack = True)  #Plots graphs of salient observable as a function of temperature.
	
	gEvT = fig.add_subplot(1,3,1)
	plt.scatter(temp,E)
	plt.xlabel("Temperature",fontsize=15)
	plt.ylabel("Energy per spin",fontsize=15)

	gCvT = fig.add_subplot(1,3,2)
	plt.scatter(temp,C)
	plt.xlabel("Temperature",fontsize=15)
	plt.ylabel("Specific Heat",fontsize=15)

	gTvM = fig.add_subplot(1,3,3)
	plt.scatter(temp,abs(Magnet)) 
	plt.xlabel("Temperature",fontsize=15)
	plt.ylabel("Magnetization per spin",fontsize=15)
	plt.show()
	
				
									
data( 1.0,2.0,1,0.5)




##Write shell script to this line




        








        
        










