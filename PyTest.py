from lib.gtec import *


g1=gUSBamp("UB-2012.10.03")
g1.init()
g1.selfCheck()
g1.close()
