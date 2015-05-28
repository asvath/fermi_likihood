import subprocess
from make2FGLxml import *
#import xml.dom.minidom 
import cfg

import os, sys

def genxmlfunc(healpix,ra,dec,week1,week2):

	"""
	Generates the xml file with the fermi sources found in the fermi catalog. The source that you are analysing is not in this file and needs to be added 		later using makefunc.py
	
	This function also writes a log file, makexmllog, noting if there are extended sources present:

		This is make2FGLxml version 04r1.
		For use with the gll_psc_v02.fit and gll_psc_v05.fit and later LAT catalog files.
		Creating file and adding sources for 2FGL
		Added 86 point sources and 0 extended sources


	"""
	
	if week1!=week2:
		identity="%06d_%d_%d_w%03d_w%03d" %(healpix,ra,dec,week1,week2)
		ltcube="%s/lat_ltcube_weekly_w%03d_w%03d_p203_v001.fits" %(cfg.home,week1,week2)
	else:
		identity="%06d_%d_%d_w%03d" %(healpix,ra,dec,week1)
		ltcube="%s/lat_spacecraft_weekly_w%03d_p203_v001_ltcube.fits" %(cfg.home,week1)

	region_filtered="%s_region_filtered_gti.fits" %(identity)
	fermisources="%s_fermisources_model.xml" %(identity)
	makexmllog="%s_output_makexml.log" %identity
	
	

	with open(makexmllog,'w') as outputFile: #will write if there are extended sources present
		subprocess.call(['%s'%(cfg.pythoncommand),'makesyfunc.py', '%s' %(region_filtered), '%s' %fermisources],stdout=outputFile) #makesyfunc generates the xml file containing the fermi sources in the catalog in the region of interest. It excludes the source that you are analysing.


if __name__ == "__main__":
	import sys
	genxmlfunc(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]))

