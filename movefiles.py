import shutil
import glob
import os
import cfg
def movefilesfunc(healpix,ra,dec,week1,week2):
	
	if week1!=week2:
		identity="%06d_%d_%d_w%03d_w%03d" %(healpix,ra,dec,week1,week2)
		
	else:
		identity="%06d_%d_%d_w%03d" %(healpix,ra,dec,week1)

	extendedlog="%s_number_of_extendedsources.log" %identity
	global b1

	with open(extendedlog) as thefile:
		b1=thefile.readline()
		b1=int(b1)


	if b1==1:
		try:
			os.makedirs("%s/%s_%s" %(cfg.folder_extended,cfg.name2,identity))
		except OSError:
			pass
		for files in glob.iglob("*%s*" %identity):
	
			shutil.move(files, "%s/%s_%s/%s" % (cfg.folder_extended,cfg.name2,identity,files))	
	if b1==0:
		try:
			os.makedirs("%s/%s_%s" %(cfg.folder,cfg.name2,identity))
		except OSError:
			pass
		for files in glob.iglob("*%s*" %identity):
	
			shutil.move(files, "%s/%s_%s/%s" %(cfg.folder, cfg.name2,identity,files))	
	if b1!=1 and b1!=0:

		
		try:
			os.makedirs("%s/%s_%s" %(cfg.folder_others,cfg.name2,identity))
		except OSError:
			pass
		for files in glob.iglob("*%s*" %identity):
	
			shutil.move(files, "%s/%s_%s/%s" % (cfg.folder_others,cfg.name2,identity,files))
	
'''			
if __name__ == "__main__":
	import sys
	movefilesfunc(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]))
'''
