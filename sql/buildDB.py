# use this to build a binary db file out of CSV; open it from the bash shell like:
# sqlite3 SWC.db

import csv, sqlite3

#set up db links
connection = sqlite3.connect("SWC.db") #creates SWC.db if it doesn't exist
cursor = connection.cursor()

#declare some tables
cursor.execute("create table if not exists Person(ident text, personal text, family text)")
cursor.execute("create table if not exists Site(name text, lat real, long real);")
cursor.execute("create table if not exists Visited(ident integer, site text, dated text);")
cursor.execute("create table if not exists Survey(taken integer, person text, quant text, reading real);")

#define table population routine:
def populate(tableName, columnNames, nCols, dbConnection):
        '''
        populate a table named <tableName> in the database
        <columnNames> is a tuple of strings naming the columns
        <nCols> is the length of <columnNames>
        <dbConnection> is an sqlite3.connect object
        <tableName> will build its rows from CSV data in file named <tableName>.csv
        '''
        fileName = tableName + '.csv'

        csvReader = csv.reader(open(fileName), delimiter=',', quotechar='"')

	#build insert command, looks like "insert into mytable (x, y, z) values (?, ?, ?)"
        sql = 'insert into ' + tableName + ' ' + str(columnNames) + ' values ('
        for i in range(0, nCols):
        	sql += '?,'
        sql = sql[:-1] + ')'

        for row in csvReader:
                dbConnection.execute(sql, row)

#fill the tables
populate('person', '(ident, personal, family)', 3, connection)
populate('site', '(name, lat, long)', 3, connection)
populate('visited', '(ident, site, dated)', 3, connection)
populate('survey', '(taken, person, quant, reading)', 4, connection)

#save & quit
connection.commit()
cursor.close()
connection.close()



