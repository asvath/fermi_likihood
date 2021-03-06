#This is the config file for our fermi likelihood process. Enjoy! 

home="/d/Software/all_weeks" #all the functions and files needed for the generation of xml are here.

homesy="/d/Software/all_weeks/Templates" #consists of template files of the extended sources

ispace="/Software/all_weeks/4wspacecraft" #home of the spacecraft files

name1="NGC185" #folder where all files are made

name2="NGC185" #name of individual folders (e.g NGC185_healpix_ra_dec_week1_week2 will go into name1 folder)

folder="%s/%s" %(home,name1) #path where all files are made
folder_extended="%s/extended"%(folder) #where files that have 1 extended source is moved to
folder_others="%s/others" %(folder) #where files that have 2 or more extended sources are moved to
healpixcol = 0
thedatafile="analysis.dat"
RA=7
DEC=8
x=23 #column 23 contains a string with the weeks in it, example : sig_match_sorted_073_076.dat The string must be in this order as the number of the week (eg. 73) will be extracted from the string
distance=25 #distance to the nearest known fermi source
interval=3 #the number of weeks to analyse. If you're looking at 4 weeks, then interval is 3. Because the range is week, week+3.  

#the following numbers are for the gtlike and gtexp functions (refer to fermi likelihood tutorial): http://fermi.gsfc.nasa.gov/ssc/data/analysis/scitools/likelihood_tutorial.html

radius=20
lowerenergy=100
upperenergy=100000
zenith=100
radius1=30
longitude=120
latitude=120
energies=20
response="P7REP_SOURCE_V15"
pythoncommand="/opt/rocks/bin/python"



