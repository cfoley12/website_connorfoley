import psycopg2
import sys
 
def main():
	#Define our connection string
	conn_string = "host='pellefant-01.db.elephantsql.com' dbname='rphkcioy' user='rphkcioy' password='tlFXsKFJHBOewOTyKvadX-CMbQnCOm0j'"
 
	# print the connection string we will use to connect
	print "Connecting to database\n	->%s" % (conn_string)
 
	# get a connection, if a connect cannot be made an exception will be raised here
	conn = psycopg2.connect(conn_string)
 
	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	cursor = conn.cursor()
	print "Connected!\n"

	# create a COURSE table
	# cursor.execute("CREATE TABLE place_course_name_here (race_name varchar(80));")

	# create a RACE table
	cursor.execute("CREATE TABLE mis (place int, year varchar(80), name varchar(80), time varchar(80), school varchar(80), race_name varchar(80), speed_rating varchar(80));")

	conn.commit()

	print "Successfully created table!\n"

if __name__ == "__main__":
	main()