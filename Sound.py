import winsound

dirLeft, dirRight = range(2)

def play(dir):
	if(dir==dirLeft):
		winsound.Beep(37,2000)
	elif(dir==dirRight):
		winsound.Beep(60,2000)

