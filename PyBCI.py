from Sound import *
from gUSBamp import *
import ctypes

# Config
BufferSize=8
SampleRate=256
channels=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
channelNum=len(channels)
Ref=(0,0,0,0)
GND=(0,0,0,0)

# Initializing Device
hMaster = OpenDeviceEx('UB-2012.10.03')
hSlave= OpenDeviceEx('UB-2012.10.04')

SetMode(hMaster,NORMAL)
SetSampleRate(hMaster,SampleRate)
SetBufferSize(hMaster,BufferSize)
SetSyncMode(hMaster,MASTER)

SetMode(hSlave,NORMAL)
SetSampleRate(hSlave,SampleRate)
SetBufferSize(hSlave,BufferSize)
SetSyncMode(hSlave,SLAVE)

print GetSerial(hMaster)
print GetSerial(hSlave)

Start(hMaster)
buff=ctypes.create_string_buffer(32768)
overlap=ctypes.create_string_buffer(32768)
GetData(hMaster,buff,overlap)
Stop(hMaster)
print buff[0]
print overlap[0]


#CloseDevice(hMaster)
##SetGround(hMaster,GND)
##SetReference(hMaster,Ref)

# Buffer


# Sound              
# play(Sound.dirLeft)

