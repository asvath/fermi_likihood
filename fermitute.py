import os
import subprocess
from  gtselect import gtselectfunc
from  gtexpmapcall import gtexpmapcallfunc
from generatexmlfunc import genxmlfunc
from makefunc import makexmlfunc
from gtlikecall import gtlikecallfunc
from tsfile import tsfunc
from emailsy import emailfunc
from gtbin import gtbinfunc
from movefiles import movefilesfunc



def fermitutefunc(healpix,ra,dec,week1,week2,distance):
	"""
	Performs the fermi likihood unbinned analysis on a single fermi source, given the healpix number, ra, dec,
	week1 when it first appears, week2 when it last appears and distance to the nearest known fermi source.

	http://fermi.gsfc.nasa.gov/ssc/data/analysis/scitools/likelihood_tutorial.html

	Example:
  

      		$ python fermitute.py  healpix,ra,dec,week1,week2,distance

	"""

	
	if week1!=week2:
		identity="%06d_%d_%d_w%03d_w%03d" %(healpix,ra,dec,week1,week2)
		
	else:
		identity="%06d_%d_%d_w%03d" %(healpix,ra,dec,week1)
		
	
	
	gtselectfunc(healpix,ra,dec,week1,week2)
	gtexpmapcallfunc(healpix,ra,dec,week1,week2)
	genxmlfunc(healpix,ra,dec,week1,week2)
	makexmlfunc(healpix,ra,dec,week1,week2,distance)	
	gtlikecallfunc(healpix,ra,dec,week1,week2)
	tsfunc(healpix,ra,dec,week1,week2,distance)
	emailfunc(healpix,ra,dec,week1,week2,distance)
	gtbinfunc(healpix,ra,dec,week1,week2)
	movefilesfunc(healpix,ra,dec,week1,week2)

	

if __name__ == "__main__":
	import sys
	fermitutefunc(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]),float(sys.argv[6]))

