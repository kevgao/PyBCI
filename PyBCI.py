from lib.Sound import *
from lib.gtec import *
from lib.svmutil import *

from ctypes import *

# main program constants
BufferSize=8
SampleRate=256
channels=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
channelNum=len(channels)
Ref=(0,0,0,0)
GND=(0,0,0,0)

# Initializing Device
hMaster = OpenDeviceEx('UB-2012.10.03')
#hSlave= OpenDeviceEx('UB-2012.10.04')
v=GetDriverVersion()
x=GetHardWareVersion(hMaster)
print v
print x
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





