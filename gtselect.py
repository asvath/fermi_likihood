
#from  gtexpmapfunc import gtexpmapfunc

import subprocess
import pyfits
import cfg




def gtselectfunc(healpix,ra,dec,week1,week2):
	
	"""
	Performs gtselect on a fermi source given the healpix number, ra, dec ,week1 and week2

	"""
				
	if week1!=week2: #For analysis done on a source for more an a span of a week
		identity="%06d_%d_%d_w%03d_w%03d" %(healpix,ra,dec,week1,week2) 
		ltcube="%s/lat_ltcube_weekly_w%03d_w%03d_p203_v001.fits" %(cfg.home,week1,week2)
	else: #For analysis done on a source for a span of a week
			identity="%06d_%d_%d_w%03d" %(healpix,ra,dec,week1)
			ltcube="%s/lat_spacecraft_weekly_w%03d_p203_v001_ltcube.fits" %(cfg.home,week1)
	radius=int(cfg.radius)
	region_filtered="%s_region_filtered_gti.fits" %(identity)
	events="%s_events.txt" %(identity)
		
	with open(events, 'w') as outputFile:
		for x in range(week1,week2+1):
			outputFile.write("%s/lat_photon_weekly_w%03d_p202_v001_gti.fits\n" % (cfg.home,x))
	
	header=pyfits.getheader("%s" %(ltcube)) #grabs the start and stop time from the ltcube
	header.keys()

	time=header['TSTART']
	stop=header['TSTOP']
      
	with open("%s_output.log" % (identity),"a") as outputFile:
		proc=subprocess.Popen(['gtselect'],stdin=subprocess.PIPE,stdout=outputFile)
		proc.communicate('@%s\n\
%s\n\
%f\n\
%f\n\
%f\n\
%f\n\
%f\n\
%f\n\
%f\n\
%f\n' %(events,region_filtered,ra,dec,radius,time,stop,cfg.lowerenergy,cfg.upperenergy,cfg.zenith))
'''
if __name__ == "__main__": #uncomment this section if used alone. It is commented as the function is imported into fermitute.py
    import sys
    gtselectfunc(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]))
'''
