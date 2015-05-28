import subprocess
from make2FGLxml import *
import cfg
#home="/home/asha/functions"
#This function makes the xml file without your source. And if a diffuse source is present, you must ensure that the path is right as the diffuse source templates are stored in a different directory. 

def makesyfunc(region_filtered,fermisources):
	mymodel=srcList('%s/gll_psc_v04.fit' %(cfg.home),'%s'%(region_filtered),'%s'%(fermisources))
	mymodel.makeModel('%s/gll_iem_v05_rev1.fit' %(cfg.home),'gll_iem_v05_rev1','%s/iso_source_v05_rev1.txt' %(cfg.home),'iso_source_v05')

if __name__ == "__main__":
	import sys
	makesyfunc(str(sys.argv[1]),str(sys.argv[2]))
