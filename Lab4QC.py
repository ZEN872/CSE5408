import datetime

def timeconversion(str1):
	
	if str1[-2:] == "AM" and str1[:2] == "12":
		return "00" + str1[2:-2]
	
	elif str1[-2:] == "AM":
		return str1[:-2]
	
	elif str1[-2:] == "PM" and str1[:2] == "12":
		return str1[:-2]
	
	else:
		return str(int(str1[:2]) + 12) + str1[2:8]
	
dt = datetime.datetime.now()
print("Current Date and Time = ", dt)
print("Military = ", timeconversion(dt.strftime("%H:%M:%S")))