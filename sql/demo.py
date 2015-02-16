# demo of reading sql from python

import csv, sqlite3

#set up db links
connection = sqlite3.connect("SWC.db") #creates SWC.db if it doesn't exist
cursor = connection.cursor()

#declare some tables
#data = cursor.execute("select * from person;")
#print data.fetchone();

for row in cursor.execute("select * from person;"):
  print row

#save & quit
#connection.commit()
#cursor.close()
#connection.close()



