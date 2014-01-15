# 	gUSBamp Interface for Python
# 	Author: Duanfeng Gao
# 	Date: Jan 5th, 2014
#	Email: kevgao@live.com
#	Website: www.kevgao.org

import ctypes

# Load DLL Library
dll=ctypes.windll.LoadLibrary('gUSBamp.dll') # 'gUSBamp.dll' should be located in the working directory


#-------------------------------------------------#
#            Configuration Parameters             #
#-------------------------------------------------#

# Filters
global CHEBYSHEV,BUTTERWORTH,BESSEL
CHEBYSHEV	= 	0	# The Chebyshev Filter
BUTTERWORTH	=	1 	# The Butterworth Filter
BESSEL		= 	2 	# The Bessel Filter

# Device Modes
global NORMAL,IMPEDENCE,CALIBRATE,COUNTER
NORMAL 		=	0	# The Normal Mode
IMPEDENCE	= 	1 	# The Impedence Mode
CALIBRATE 	= 	2 	# The Calibrate Mode
COUNTER 	= 	3   # The Counter Mode

# Device Sync
global SLAVE, MASTER
MASTER		=	0	# Setting the device as the Master
SLAVE		=	1 	# Setting the device as the Slave


#-------------------------------------------------#
#                 Data Structures                 #
#-------------------------------------------------#




#-------------------------------------------------#
#                   API Fuctions                  #
#-------------------------------------------------#

# Common Functions
def OpenDevice(PortNum):  	 # Get the Device Handle through the USB Port Number, the port number should be an integer and could be found on the device manage window of the Windows OS.
	hDevice = dll.GT_OpenDevice(PortNum)
	if(hDevice):
		return hDevice
	else:
		print "No Device on this Port"

def OpenDeviceEx(Serial):	# Get the Device Handle through the Serial Number of the Device, the Serial Number should be a string like "UB-2012.10.03"
	hDevice = dll.GT_OpenDeviceEx(Serial)
	if(hDevice):
		return hDevice
	else:
		print "No Such Device"

def CloseDevice(hDevice):	# Close the device through device handle
        pHandle=ctypes.pointer(ctypes.c_int(hDevice))
	if(dll.GT_CloseDevice(pHandle)):
		print "Device Closed"
	else:
		print "Failed to Close Device!"

def SetSyncMode(hDevice,SyncMode): # Set the device mode when more than one devices are ultilized, only one Master Device could exist.
	return dll.GT_SetSlave(hDevice,SyncMode)

def SetMode(hDevice,Mode):	# Set the Device Mode
	if(Mode<4):
		Status = dll.GT_SetMode(hDevice,Mode)
		return Status
	else:
		print "Invalid Mode"
		return 0

# Data Functions
def SetBufferSize(hDevice, size): 	# Set the Buffer Size
	return dll.GT_SetBufferSize(hDevice,size)

def SetSampleRate(hDevice, rate):	# Set the Sampling Rate, rate should be integers like 128, 256, 512 etc.
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
# def SetChannels(hDevice,)


# Device Info Functions
def GetHardWareVersion(hDevice):
	return dll.GT_GetHWVersion(hDevice)

def GetSerial(hDevice):
	pStr=('aaaaaaaaaaaaa')
	dll.GT_GetSerial(hDevice,pStr,16)
	return pStr

def GetDriverVersion():
	return dll.GT_GetDriverVersion()	
