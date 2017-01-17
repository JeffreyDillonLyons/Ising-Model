#!/bin/sh

chmod +rwx ising.py   #Allows the bash script to read, write to and execute the python script. 


while true; do
	read -p "What size lattice do you wish to run?" size;
	sed -i "20s/.*/size = $size/" ising.py #Prints desired lattice size to line 17 of the python script.

	echo " "

	read -p "How many iterations should be run per cycle of the metropolis algorithm? Input of n reults in n100000 iterations." itera; 
	read -p "Enter starting temperature - " initial
   	
	echo  "  "

	read -p "Enter final temperature - " final
	echo "  "  
	
	read -p "Enter temperature increment - " increment
	echo "  "                                                                     
	
	sed -i "133s/.*/data( $initial,$final,$itera,$increment)/" ising.py;break;


done

echo "Executing Ising model...please wait"

python ./ising.py # Executes Ising model. Runs python script. 



echo " "
echo "The Ising model has finished."
echo " "
