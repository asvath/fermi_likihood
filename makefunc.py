import subprocess
from make2FGLxml import *
import cfg
import os, sys

def makexmlfunc(healpix,ra,dec,week1,week2,distance):

	"""
	Adds the source that you are analysing into the xml file containing the other fermi sources from the fermi catalog in the region of interest. 
	Also corrects the path name to any extended sources
	"""
	
	if week1!=week2:
		identity="%06d_%d_%d_w%03d_w%03d" %(healpix,ra,dec,week1,week2)
		ltcube="%s/lat_ltcube_weekly_w%03d_w%03d_p203_v001.fits" %(cfg.home,week1,week2)
		spacecraft="%s/w%03d_w%03d_newspacecraft.fits" %(cfg.ispace,week1,week2)
	else:
		identity="%06d_%d_%d_w%03d" %(healpix,ra,dec,week1)
		ltcube="%s/lat_spacecraft_weekly_w%03d_p203_v001_ltcube.fits" %(cfg.home,week1)
		spacecraft="%s/lat_spacecraft_weekly_w%03d_p202_v001.fits " %(cfg.ispace,week1)

	region_filtered="%s_region_filtered_gti.fits" %(identity)
	fermisources="%s_fermisources_model.xml" %(identity)
	inputmodel="%s_input_model.xml" %(identity)
	fermis="%s_fermis.xml" %identity
	response="P7REP_SOURCE_V15"
	makexmllog="%s_output_makexml.log" %identity
	global extendedsource
	global numberofextendedsources
	extendedlog="%s_number_of_extendedsources.log" %identity
	ExtendedList="ExtendedList.txt"
	OthersList="OthersList.txt"

	
	with open (makexmllog,'r') as outputFile: #opens the makexmllog file from makesyfunc. This document contains info about the extended sources.
		
		for line in outputFile:
			
			with open (makexmllog,'r') as File:
				if line.startswith('Added')==True:
					a,b=line.split('and ')	
					b1,b2,b3=b.split(' ')
				
					numberofextendedsources=int(b1) #b1 is the number of extended sources
	outputFile.close()
	outputFile=open(inputmodel, 'w')
	print numberofextendedsources

	if numberofextendedsources==1: #if there is an extended source
		with open (makexmllog,'r') as outputFile:
		
			for line in outputFile:
			
				with open (makexmllog,'r') as File:
					if line.startswith('Extended')==True:
						print line
								
						c,d=line.split(' in')
					
						c1,c2,c3,c4=c.split(' ')
					
					
						extendedsource=str(c3) #extracts the name of the extended source from makexmllog
	

		


		outputFile.close()	


	

		with open("%s"  %fermisources) as thefile: #opens the xml file that was created from makesyfunc
			for line in thefile:
				if    line.startswith('	<spatialModel file="%s.fits"' %(extendedsource))==True:

										
					special=str.replace(line,'%s.fits'%extendedsource,'%s/%s.fits' %(cfg.homesy,extendedsource)) 
					print special #replace with the correct path to the extendedsource(Templates folder)
			
					special1=str.replace(special,'type="SpatialMap"','type="SpatialMap" map_based_integral="true"')
					print special1 #instruction from fermi tutorial, you must add map_based...
					outputFile=open(fermis, 'w') #write to fermis, the original xml with the right path to the extended source
					with open("%s"  %fermisources,'r') as infile:
						for line in infile:
							if    line.startswith('	<spatialModel file="%s.fits"' %(extendedsource))==False:
								outputFile.write(line)
							else:
								outputFile.write(special1)
					outputFile.close()
									


			
		outputFile=open(inputmodel, 'w') #final xml file. contains the right path and the source info of "your" source.
		with open(fermis,'r') as infile:
			for line in infile:
				if line.startswith('</source_library>')==False:
					outputFile.write(line)
							
		outputFile.write('\n\
			<!-- My sources -->\n\
			<source name="%f_%f" type="PointSource">\n\
			<spectrum type="PowerLaw">\n\
			<parameter free="1" max="1000.0" min="0.001" name="Prefactor" scale="1e-09" value="10"/>\n\
			<parameter free="1" max="-1.0" min="-5.0" name="Index" scale="1.0" value="-2.1"/>\n\
			<parameter free="0" max="2000.0" min="30.0" name="Scale" scale="1.0" value="100.0"/>\n\
			</spectrum>\n\
			<spatialModel type="SkyDirFunction">\n\
			<parameter free="0" max="360" min="-360" name="RA" scale="1.0" value="%f"/>\n\
			<parameter free="0" max="90" min="-90" name="DEC" scale="1.0" value="%f"/>\n\
			</spatialModel>\n\
			</source>\n\
			</source_library>\n' % (ra,dec,ra,dec))

				

		outputFile.close()
	
		with open("%s_diffrsp.log" % (identity), 'w') as outsyputFile: #run diffrsp if you have an extended source.
			subprocess.call(['%s' %(cfg.pythoncommand),'gtdiffrsp.py', '%s' %(region_filtered),'%s' %(spacecraft), '%s' %inputmodel, '%s' %(response),'%s' %identity ],stdout=outsyputFile)
			
		with open(ExtendedList,"a+") as outsyFile:
			outsyFile.write("%d %f %f %d %d %f\n" %(healpix,ra,dec,week1,week2,distance))
					
	if numberofextendedsources==0: #if there is no extended source
		outputFile=open('%s' %(inputmodel), 'w') #write to inputmodel, "your" source
		with open('%s' %(fermisources),'r') as infile:
			for line in infile:
				if line.startswith('</source_library>')==False:
					outputFile.write(line)
					
			

		outputFile.write('\n\
			<!-- My sources -->\n\
			<source name="%f_%f" type="PointSource">\n\
			<spectrum type="PowerLaw">\n\
			<parameter free="1" max="1000.0" min="0.001" name="Prefactor" scale="1e-09" value="10"/>\n\
			<parameter free="1" max="-1.0" min="-5.0" name="Index" scale="1.0" value="-2.1"/>\n\
			<parameter free="0" max="2000.0" min="30.0" name="Scale" scale="1.0" value="100.0"/>\n\
			</spectrum>\n\
			<spatialModel type="SkyDirFunction">\n\
			<parameter free="0" max="360" min="-360" name="RA" scale="1.0" value="%f"/>\n\
			<parameter free="0" max="90" min="-90" name="DEC" scale="1.0" value="%f"/>\n\
			</spatialModel>\n\
			</source>\n\
			</source_library>\n' % (ra,dec,ra,dec))

		outputFile.close()
	if numberofextendedsources>1:
		with open(OthersList,"a+") as outsyFile:
			outsyFile.write("%d %f %f %d %d %f\n" %(healpix,ra,dec,week1,week2,distance))
	
	if numberofextendedsources==1:
		outsyputFile=open(extendedlog,'w') #write the number of extended sources and name in a file
		outsyputFile.write("%s\n\
        	%s"%(numberofextendedsources,extendedsource))
		outsyputFile.close()

	if numberofextendedsources !=1:
		outsyputFile=open(extendedlog,'w') #write the number of extended sources and name in a file
		outsyputFile.write("%s" %(numberofextendedsources))
		outsyputFile.close()

	

	

if __name__ == "__main__":
	import sys
	makexmlfunc(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]),float(sys.argv[6]))

	#from make2FGLxml import *

