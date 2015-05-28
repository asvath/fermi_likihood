import subprocess

def gtdiffrspfunc(region_filtered,spacecraft,inputmodel,response,identity):
 
		
      	inputfile="%s_gtdiffrsp_input.txt" %(identity)
	with open("%s" %(inputfile),"a+") as outsyFile:
		outsyFile.write("Running gtdiffrsp with the following input:\n\
%s\n\
%s\n\
%s\n\
%s\n"%(region_filtered,spacecraft,inputmodel,response))

	proc = subprocess.Popen(['gtdiffrsp'],stdin=subprocess.PIPE)
	proc.communicate('\
%s\n\
%s\n\
%s\n\
%s\n' %(region_filtered,spacecraft,inputmodel,response))




if __name__ == "__main__":
    import sys
    gtdiffrspfunc(str(sys.argv[1]),str(sys.argv[2]),str(sys.argv[3]),str(sys.argv[4]),str(sys.argv[5]))



'''
      	inputfile="%s_input.txt" %(identity)
	with open("%s" %(inputfile),"a+") as outsyFile:
		outsyFile.write("Running gtdiffrsp with the following input:\n\
%s\n\
%s\n\
%s\n\
%s\n"%(region_filtered,spacecraft,inputmodel,response))



	with open("%s_output.log" % (identity),"a") as outputFile:
'''
