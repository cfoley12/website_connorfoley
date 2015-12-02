import psycopg2
import sys
import re
 
def main():
	#Define our connection string
	conn_string = "host='pellefant-01.db.elephantsql.com' dbname='uncrgpvf' user='uncrgpvf' password='rkWkfGnFqOJsniQbLNAFk07p-XOEIz31'"
 
	# print the connection string we will use to connect
	print "Connecting to database\n	->%s" % (conn_string)
 
	# get a connection, if a connect cannot be made an exception will be raised here
	conn = psycopg2.connect(conn_string)
 
	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	cursor = conn.cursor()
	print "Connected!\n"

	# reading in from file

	cursor.execute("SELECT * FROM portage_2015")
	for row in cursor.fetchall():
	    print row

			

	conn.close()

 
if __name__ == "__main__":
	main()

