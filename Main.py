'''This code is a part of the 3D Scanner project'''
'''Developed by team SAAS'''
'''Ekalavya 2017'''
'''IIT Bombay'''


#the necessary packages are imported
import os
import v4l2 #a python binding for the video4linux2 users api
import fcntl
from ValueSelected import * #local package
from ShowBmp import * #local package
from About import * #local package
from Root import * #local package

AboutText = """
This is a software where you can select the Video Device and get the output
Developed by Team SAAS, Ekalavya 2017, IITB"""


def RefreshCamList(): #Function to refresh the list of available Webcams and Arduinos
	#Some local empty lists are initialised
	CamList=[]
	AddressList=[]#It has address-name of devices
	CamDict={}
	ArduinoList=[]
	DeviceList=os.listdir("/dev") #the method listdir() returns a list containing the name of enteries
	#in the directory given by the path.We know that any devices connected to system are in folder /dev
	for i in DeviceList:
		temp=i
		if (temp[:5]=='video'):
			AddressList.append(i) #the video devices are added to CamList
	for i in AddressList:
		vd = open("/dev/"+i, 'rw') 
		cp = v4l2.v4l2_capability() 
		fcntl.ioctl(vd, v4l2.VIDIOC_QUERYCAP, cp) 
		CamList.append(cp.card)#cp..card and cp.driver returns full detail of card
		CamDict[cp.card]=i 
		#With every cp.card name address is attached
		#appends the data to the dictionary in the format "Logitech":"video1"
		
	for i in DeviceList:
		temp=i
		if (temp[:6]=='ttyACM'):
			ArduinoList.append(i)
	VideoDeviceNumber=len(CamList)-1 #Default Camera is the external webcam
	BoardNumber=len(ArduinoList) #Default Arduino is the first one
	return VideoDeviceNumber,CamList,CamDict,ArduinoList,BoardNumber

def Main():
	VideoDeviceNumber,CamList,CamDict,ArduinoList,BoardNumber=RefreshCamList() #this will update the list of new devices ,if any new is connected
	MainWindow=Root(VideoDeviceNumber,CamList,CamDict,ArduinoList,BoardNumber)
	MainWindow.CreateMainWindow()

'''This code is a part of the 3D Scanner project'''
'''Developed by team SAAS'''
'''Ekalavya 2017'''
'''IIT Bombay'''
