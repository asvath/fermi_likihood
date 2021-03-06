import os 
import string
from array import * 
import cfg
import subprocess

"""

This code automates the fermi unbinned liklihood tutorial as described in : 
http://fermi.gsfc.nasa.gov/ssc/data/analysis/scitools/likelihood_tutorial.html
It also identifies sources that have Test Statistic (TS) >25 and emails the user with the following details:
-Name of source
-TS value
-RA and DEC 
-Folder where source can be found
-The week number when the source had a TS >25  

A sorted (by week number) data list (cfg.datafile: imported from cfg.py) containing the details of the fermisources is analysized. 
The sources that appear, disappear and reappear (in a span of 4 weeks respectively) are of particular interest in the analysis*.
These sources of interest are picked out and the unbinned liklihood tutorial is performed.

*Example of 3 columns from datafile:

# eg:	Healpix 	Weeks sources appears			Weeks sources disappears

#	444140   	sig_match_sorted_253_256.dat 	sig_match_sorted_249_252.dat   
#     	444140  	sig_match_sorted_253_256.dat 	sig_match_sorted_257_260.dat 

# Notice that weeks 253-256 are the weeks that the source appears. This source is repeated. 
The source is to be analysized for the weeks 253-256


Example:
  

      $ python analysis_4weeks.py 



"""

RA=array('f')
DEC=array('f')
WEEK=array('f')
DISTANCE=array('f')
HEALPIX=array('f')
week=array('f')
r=array('f')
de=array('f')
w=array('f')
healp=array('f')
distance=array('f')
datafile="%s/%s" %(cfg.home,cfg.thedatafile)


with open(datafile) as source_file: #data file containing fermisources, the details are stored in the arrays defined above
    		for line in source_file:
        		cols = string.split(line)
        		
           		try:
				healpix=cols[cfg.healpixcol]
				right_asc=cols[cfg.RA]
				declination=cols[cfg.DEC]
				x=cols[cfg.x] #x is a string. e.g sig_match_sorted_073_076.dat
				a,b,c,d,e=x.split('_')
				firstweek=d #week the source appears
				dist=cols[cfg.distance] #distance to the nearest known fermisource
				
				
			
			except ValueError:
                		print "Could not convert data to a float: ",line
            		except IndexError:
				print "Index Error ", line		
			else:
				
				RA.append(float(right_asc))
				DEC.append(float(declination))   #mind the reapeated letters in the ending. 
				WEEK.append(float(firstweek))
				HEALPIX.append(float(healpix))
				DISTANCE.append(float(dist))
				


for j in range(0,len(RA)): # we do this loop to get rid of repeated info in the data file 
	
		
	if j==0: #we start with this because the first datapoint in thedatafile is not repeated. Recall that the datafile contains things that appear and disappear. So they are on the list twice * See docstring for more details.
		r.append(RA[j])
		de.append(DEC[j])
		w.append(int(WEEK[j]))
		healp.append(HEALPIX[j])
		distance.append(DISTANCE[j])
	
	if j!=0:
		if int(HEALPIX[j])==int(HEALPIX[j-1]) and int(WEEK[j])==int(WEEK[j-1]): #checks if the fermisource is a repeat as described in the docstring
			print " "
		else:
			r.append(RA[j])
			de.append(DEC[j])
			w.append(int(WEEK[j]))
			healp.append(HEALPIX[j])
			distance.append(DISTANCE[j])



#Here you must qsub. We use a loop to analyse each unrepeated soure found in the datafile

for j in range(0,len(healp)):

	week2=w[j] + cfg.interval #cfg.interval is the number of steps (weeks) that the fermisources appear
	identity="analysis_%d_%d_%d" %(healp[j],w[j],week2) #generic name for the analysis for the different sources 
	
	
	subprocess.call(['qsub','-N',identity,'-V','-b','y','-cwd','%s' %(cfg.pythoncommand),'fermitute.py','%f' %healp[j],'%f' %r[j],'%f' %de[j],'%d' %w[j],'%d' %week2, '%f'%distance[j]])




