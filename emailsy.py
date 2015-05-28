import subprocess
import cfg

def emailfunc(healpix,ra,dec,week1,week2,distance):

	
	if week1!=week2:
		identity="%06d_%d_%d_w%03d_w%03d" %(healpix,ra,dec,week1,week2)
		
	else:
		identity="%06d_%d_%d_w%03d" %(healpix,ra,dec,week1)
		

	
	TSFile="TS_%s.txt" %(identity)

	extendedlog="%s_number_of_extendedsources.log" %identity
	global b1

	with open(extendedlog) as thefile:
		b1=thefile.readline()
		b1=int(b1)
		
	if b1==1:
		Folder="%s/%s_%s" %(cfg.folder_extended,cfg.name2,identity)
	if b1==0:
		Folder="%s/%s_%s" %(cfg.folder, cfg.name2,identity)
	if b1!=0 and b1!=1:
		Folder="%s/%s_%s" %(cfg.folder_others,cfg.name2,identity)


	with open("%s" %(TSFile)) as hh:
		for line in hh:
			if line.startswith("TS"):
				x=line
				
				m,k,c,=x.split(' ')
				print c
		
						
				ts=float(c)
				if ts < 25:
					print "Hello!"
			
				else:
					

					proc=subprocess.Popen(["mail","-s","Blazar Ra: %f Dec: %f" %(ra,dec),"blazarsgama@gmail.com"],stdin=subprocess.PIPE)
					proc.communicate("Hello Jeremy and Asha,\n\ \n\
					I have found an object for you!\n\
					\n\
					Here are the details: \n\
					RA: %f \n\
					DEC: %f \n\
					TS: %f \n\
					Weeks: %d to %d\n\
					Distance: %f \n\
					Folder:%s\n\
					Best wishes,\n\
					\n\
					You know who\n" %(ra,dec,ts,week1,week2,distance,Folder))


'''
if __name__ == "__main__":
	import sys
	emailfunc(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]),float(sys.argv[6]))
'''
