import subprocess
import cfg



def gtexpmapcallfunc(healpix,ra,dec,week1,week2):


	"""
	Performs gtexpmap on a fermi source given the healpix number, ra, dec ,week1 and week2

	"""
	
	    
	
	if week1!=week2: #For analysis done on a source for more an a span of a week
		identity="%06d_%d_%d_w%03d_w%03d" %(healpix,ra,dec,week1,week2)
		ltcube="%s/lat_ltcube_weekly_w%03d_w%03d_p203_v001.fits" %(cfg.home,week1,week2)
		#spacecraft="%s/w%03d_w%03d_newspacecraft.fits" %(cfg.ispace,week1,week2) #uncomment if you do not want to use the spacecraft file that spans for whole mission
	else:#For analysis done on a source for a span of a week
		identity="%06d_%d_%d_w%03d" %(healpix,ra,dec,week1)
		ltcube="%s/lat_spacecraft_weekly_w%03d_p203_v001_ltcube.fits" %(cfg.home,week1)
		#spacecraft="%s/lat_spacecraft_weekly_w%03d_p202_v001.fits " %(cfg.ispace,week1) #same as above

	spacecraft="%s/lat_spacecraft_merged.fits" %(cfg.home)
	region_filtered="%s_region_filtered_gti.fits" %(identity)
	expmap="%s_expmap.fits" %(identity)
	response=str(cfg.response)
	inputfile="%s_input.txt" %(identity)
	radius1=int(cfg.radius1)
	longitude=int(cfg.longitude)
	latitude=int(cfg.latitude)
	energies=int(cfg.energies)

        
	with open("%s" %(inputfile),"a+") as outsyFile:
		outsyFile.write("Running gtexpmap with the following input:\n\
%s\n\
%s\n\
%s\n\
%s\n\
%s\n\
%f\n\
%f\n\
%f\n\
%f\n"%(region_filtered,spacecraft,ltcube,expmap,response,radius1,longitude,latitude,energies))




		

	proc = subprocess.call(['%s' %(cfg.pythoncommand), 'gtexpmap.py', '%s' %identity,'%s' %region_filtered, '%s' %spacecraft, '%s' %ltcube, '%s' %expmap,'%s' %response, '%f'%radius1, '%f' %longitude, '%f' %latitude, '%f' %energies ])
	



'''
if __name__ == "__main__":#uncomment this section if used alone. It is commented as the function is imported into fermitute.py
    import sys
    gtexpmapfunc(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]))

'''


