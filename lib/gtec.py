#!/usr/bin/env python
'''
The gUSBamp Module is the python version of the gUSBamp API. gUSBamp is an amplifier 
of brain EEG signals produced by g.tec

Author: Duanfeng Gao
Date: Jan 5th, 2014
Email: kevgao@live.com
Website: www.kevgao.org

'''

import ctypes

# Load DLL Library
dll=ctypes.windll.LoadLibrary('gUSBamp.dll') # 'gUSBamp.dll' should be located in the lib directory


#-------------------------Configuration Parameters-------------------------------------#
# Filters
Filter={0:'CHEBYSHEV',1:'BUTTERWORTH',2:'BESSEL'}

# Device Modes
mode={0:'Normal',1:'Impedence',2:'Calibrate',3:'Counter'}

# Device Sync Modes
syncmode={0:'Master',1:'Slave'}

# Data structures
class Scale(ctypes.Structure):
	''' Scale struct'''
	_fields_=[("factor",ctypes.c_float*16),("offset",ctypes.c_float*16)]

class Ref(ctypes.Structure):
	''' Ref and Gnd struct '''
	_fields_=[("port1",ctypes.c_int),("port2",ctypes.c_int),("port3",ctypes.c_int),("port4",ctypes.c_int)]


#----------------------------------gUSBamp class-------------------------------------#

class gUSBamp(object):
    ''' The gUSBamp Class'''       
    def __init__(self,Serial):
        self.handle=OpenDeviceEx(Serial)
    
    def init(self,chanelarray=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],samplerate=256,syncmode=MASTER,mode=NORMAL):
    	''' Initiate the device, including setting channels, setting sample rate, setting sync mode and setting mode'''
        if(SetChannels(self.handle,chanelarray)):
        	if(SetSampleRate(self.handle,samplerate)):
        		if(SetSyncMode(self.handle,syncmode)):
        			if(SetMode(self.handle,mode)):
        				print "Device Initialized"
    

    def selfCheck(self):
    	''' Device self check'''
    	m=GetMode(self.handle)
    	print "Device Mode: "+ m
    	GetScale(self.handle)
    	
    	for i in range(1,16):
    		imp=GetImpedence(self.handle,i)
    		print "Impedence of Channel "+str(i)+" is: "+str(imp)  
   
    def getInfo(self):
    	''' print device info'''
        print "Device Serial Number is: " + GetSerial(self.handle)
        print "Device Hardware Version is:" + str(GetHardWareVersion(self.handle))

    def aquireData(self):
    	''' aquire data'''
    	pass

    def readData(self):
    	pass




    def close(self):
    	''' close the device '''
        CloseDevice(self.handle)
     




#-------------------------------------Python API-------------------------------------------#

# Common Functions
def OpenDevice(PortNum):
	''' Get the Device Handle through the USB Port Number, the port number should be an integer 
	and could be found in the device manager of the Windows OS. '''
	hDevice = dll.GT_OpenDevice(PortNum)
	if(hDevice):
		return hDevice
	else:
		print "No Device on this Port"
		return False

def OpenDeviceEx(Serial):
	''' Get the Device Handle through the Serial Number of the Device, the Serial Number 
	should be a string like "UB-2012.10.03" and could be found on the gUSBamp hardware. '''
	hDevice = dll.GT_OpenDeviceEx(Serial)
	if(hDevice):
		return hDevice
	else:
		print "No Such Device"
		return False

def CloseDevice(hDevice):
	'''Close the device through device handle'''
    pHandle=ctypes.pointer(ctypes.c_int(hDevice))
	if(dll.GT_CloseDevice(pHandle)):
		print "Device Closed"
		return True
	else:
		print "Failed to Close Device!"
		return False

def SetChannels(hDevice,channels):
	''' Set Device Channels. Device Channels should be expressed by list with elements 
	range from 1 to 16. '''
	n=len(channels)
	c=ctypes.create_string_buffer('/0'*(n+1))
	temp=chr(channels[0])
	for i in range(1,n):
		temp=temp+chr(channels[i])
	c.value=temp
	if(dll.GT_SetChannels(hDevice,ctypes.byref(c),n)):
		print "Channels are set to"+ str(channels)
		return True
	else:
		print "Failed to set channels"
		return False


def SetSyncMode(hDevice,SyncMode):
	'''Set the device mode when more than one devices are ultilized, only one Master 
	Device could exist. '''
	if(SyncMode==0 or SyncMode==1):
		if(dll.GT_SetSlave(hDevice,SyncMode)):
			print "Device set to be "+syncmode[SyncMode]
			return True
		else:
			print "Failed to set device to be "+syncmode[SyncMode]
			return False
	else:
		print "Invalid SyncMode. SyncMode should be 0 or 1"
		return False

def SetMode(hDevice,Mode):
	'''Set the Device Mode'''
	if(Mode<4):
		if(dll.GT_SetMode(hDevice,Mode)):
			return True
		else:
			print "Failed to set mode"
			return False
	else:
		print "Invalid Mode"
		return False

# Data Functions
def SetBufferSize(hDevice, size): 	
	'''Set the Buffer Size'''
	return dll.GT_SetBufferSize(hDevice,size)

def SetSampleRate(hDevice, rate):
	'''Set the Sampling Rate, rate should be integers like 128, 256, 512 etc.'''
	return dll.GT_SetSampleRate(hDevice,rate)

def SetGround(hDevice,GND):
	if(len(GND)==4):
		return dll.GT_SetGround(hDevice,GND)
	else:
		print "Invalid GND Config"

def SetReference(hDevice,Ref):
	if(len(Ref)==4):
		return dll.GT_SetReference(hDevice,Ref)
	else:
		print "Invalid Ref Config"

def SetScale(hDevice,scale):
	pass

def Start(hDevice):
	if(dll.GT_Start(hDevice)):
		print "Device Started!"
	else:
		print "Failed to start device"

def Stop(hDevice):
	if(dll.GT_Stop(hDevice)):
		print "Device Stopped!"
	else:
		print "Failed to Stop device"

def GetData(hDevice,buffer,overlap):
	return dll.GT_GetData(hDevice,buffer,550,overlap)



# Device Info Functions
def GetHardWareVersion(hDevice):
	v=dll.GT_GetHWVersion(hDevice)
	ver=ctypes.c_float(v)
	return ver.value

def GetSerial(hDevice):
	pStr=('aaaaaaaaaaaaa')
	dll.GT_GetSerial(hDevice,pStr,16)
	return pStr

def GetDriverVersion():
	return dll.GT_GetDriverVersion()	

def GetImpedence(hDevice,channel):
	s=ctypes.c_double(0.0);
	if(dll.GT_GetImpedance(hDevice,channel,ctypes.byref(s))):
		return s.value
	else:
		return 0

def GetMode(hDevice):
	c=ctypes.c_char('\0')
	if(dll.GT_GetMode(hDevice,ctypes.byref(c))):
		t=ord(c.value)
		return mode[t]
	else:
		print "Fail to get mode"
		return 0

def GetScale(hDevice):
	s=Scale()
	if(dll.GT_GetScale(hDevice,ctypes.byref(s))):
		for i in s.offset:
			print "Offset: "+str(i)
		for j in s.factor:
			print "Factor: "+str(j)
	else:
		print "Fail to get scale"



