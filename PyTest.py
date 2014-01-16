from lib.gtec import *
import time

g1=gUSBamp("UB-2012.10.03")
g1.init()
#g1.selfCheck()
g1.startAquisition()
time.sleep(3)
x=g1.printData()
g1.close()

##print str(x)
##for i in range(0,500):
##    print str(x[i])
    
fp=open('rec.txt','w')
fp.write(str(x))
fp.close()
