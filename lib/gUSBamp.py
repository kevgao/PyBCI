import gUSBampLib

class gUSBamp(object):
    ''' The gUSBamp Class'''
       
    def __init__(self,Serial):
        self.handle=gUSBampLib.OpenDeviceEx(Serial)
        #gUSBampLib.SetChannels(self.handle)
        #gUSBampLib.SetSampleRate(self.handle)


    
