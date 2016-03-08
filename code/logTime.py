#This program logs the current time and date into a sqlite database.
#It relies on the function 'readTime()' in the external file readTime.py
#to determine the time and date (in format [Y-M-D][H-m-s]). 
#!/usr/bin/python

import sqlite3 as db 
from readTime import readTime

dt = readTime()

try:
   con = db.connect('testTime.db')
   cur = con.cursor()
   cur.execute('''INSERT INTO timeLogs(date, time) 
		VALUES(?,?)''', (dt[0], dt[1]))
   print ("Date: " + dt[0] + " | Tie: " + dt[1] + " ) added successfully") 


except db.Error, e:
   print "Error %s:" % e.args[0];
   sys.exit(1);

finally:
   if con:
      con.close();
