# This program reads the current time and date 
# (in the format H-m-s and Y-M-D, respectively).
# It then returns both as a tuple, in the form [date][time].

#!/usr/python
import datetime

def readTime():
	now = datetime.datetime.now()

	date = now.strftime("%Y-%m-%d");
	time = now.strftime("%H-%M-%S");

	return [date, time];
