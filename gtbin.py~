import os 
import subprocess

def gtbinfunc(healpix,ra,dec,week1,week2):
	

	if week1!=week2:
		identity="%06d_%d_%d_w%03d_w%03d" %(healpix,ra,dec,week1,week2)
		
	else:
		identity="%06d_%d_%d_w%03d" %(healpix,ra,dec,week1)
	
	region_filtered="%s_region_filtered_gti.fits" %(identity)
	TSFile="TS_%s.txt" %(identity)
	cmap="%s_cmap.fits" %(identity)
	with open(TSFile) as hh:
		for line in hh:
			if line.startswith("TS"): #get TS value
				x=line
				
				m,k,c,=x.split(' ')
				print c
		
						
				ts=float(c)
				if ts > 25:



					with open("%s_output_gtbin.log" % (identity),"a") as outputFile:
				
						proc = subprocess.Popen(['gtbin'],stdin=subprocess.PIPE,stdout=outputFile)
						proc.communicate('CMAP\n\
%s\n\
%s\n\
None\n\
160\n\
160\n\
0.25\n\
CEL\n\
%f\n\
%f\n\
0.0\n\
AIT\n'  %(region_filtered,cmap,ra,dec))




'''

if __name__ == "__main__":
	import sys
	gtbinfunc(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]))

'''		
