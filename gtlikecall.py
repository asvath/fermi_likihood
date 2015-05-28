import subprocess
import cfg

def gtlikecallfunc(healpix,ra,dec,week1,week2):
	
		if week1!=week2:
			identity="%06d_%d_%d_w%03d_w%03d" %(healpix,ra,dec,week1,week2)
			ltcube="%s/lat_ltcube_weekly_w%03d_w%03d_p203_v001.fits" %(cfg.home,week1,week2)
			#spacecraft="%s/w%03d_w%03d_newspacecraft.fits" %(cfg.ispace,week1,week2)
		else:
			identity="%06d_%d_%d_w%03d" %(healpix,ra,dec,week1)
			ltcube="%s/lat_spacecraft_weekly_w%03d_p203_v001_ltcube.fits" %(cfg.home,week1)
			#spacecraft="%s/lat_spacecraft_weekly_w%03d_p202_v001.fits " %(cfg.ispace,week1)

		spacecraft="%s/lat_spacecraft_merged.fits" %(cfg.home)		
		region_filtered="%s_region_filtered_gti.fits" %(identity)
		expmap="%s_expmap.fits" %(identity)
		inputmodel="%s_input_model.xml" %(identity)
		outputmodel="%s_output_model.xml" % (identity)


		
		proc = subprocess.call(['%s' %(cfg.pythoncommand),'gtlike.py', '%s' %identity, '%s' %outputmodel,'%s' %spacecraft,'%s' %region_filtered, '%s' %expmap, '%s' %ltcube, '%s' %inputmodel])
		


'''
if __name__ == "__main__":
    import sys
    gtlikecallfunc(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]))
'''
