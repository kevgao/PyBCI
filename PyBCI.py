from lib.Sound import *
from lib.gtec import *
#from lib.svmutil import *

from ctypes import *

# main program constants
BufferSize=8
SampleRate=256
channels=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
channelNum=len(channels)
Ref=(0,0,0,0)
GND=(0,0,0,0)

# Initializing Device
xx = OpenDeviceEx('UB-2012.10.03')
hMaster=xx
#hSlave= OpenDeviceEx('UB-2012.10.04')
v=GetSerial(hMaster)
x=GetHardWareVersion(hMaster)
print v
print x
i=GetImpedence(hMaster,3)
print i
print SetChannels(hMaster,[1,2,3,4])
print SetMode(hMaster,0)
print GetMode(hMaster)
GetScale(hMaster)
CloseDevice(hMaster)
##SetMode(hMaster,NORMAL)
##SetSampleRate(hMaster,SampleRate)
##SetBufferSize(hMaster,BufferSize)
##SetSyncMode(hMaster,MASTER)
##
##SetMode(hSlave,NORMAL)
##SetSampleRate(hSlave,SampleRate)
##SetBufferSize(hSlave,BufferSize)
##SetSyncMode(hSlave,SLAVE)
##
##print GetSerial(hMaster)
##print GetSerial(hSlave)
##
##Start(hMaster)
##buff=ctypes.create_string_buffer(32768)
##overlap=ctypes.create_string_buffer(32768)
##GetData(hMaster,buff,overlap)
##Stop(hMaster)
##print buff[0]
##print overlap[0]

# Data Aquisition





#CloseDevice(hMaster)
##SetGround(hMaster,GND)
##SetReference(hMaster,Ref)





