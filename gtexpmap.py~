import subprocess
import cfg



def gtexpmapfunc(identity,region_filtered,spacecraft,ltcube,expmap,response,radius1,longitude,latitude,energies):
   
	    
	



	with open("%s_output.log" % (identity),"a") as outputFile:
		


		proc = subprocess.Popen(['gtexpmap'],stdin=subprocess.PIPE,stdout=outputFile)
		proc.communicate('\
%s\n\
%s\n\
%s\n\
%s\n\
%s\n\
%d\n\
%d\n\
%d\n\
%d\n' %(region_filtered,spacecraft,ltcube,expmap,response,radius1,longitude,latitude,energies))




if __name__ == "__main__":
    import sys
    gtexpmapfunc(str(sys.argv[1]),str(sys.argv[2]),str(sys.argv[3]),str(sys.argv[4]),str(sys.argv[5]),str(sys.argv[6]),float(sys.argv[7]),float(sys.argv[8]),float(sys.argv[9]),float(sys.argv[10]))
