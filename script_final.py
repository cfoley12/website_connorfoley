import psycopg2
import sys
import re
 
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

	# reading in from file
	for line in open("ella_park_fixed.txt", 'r'):
		parts = re.split(r'\t+', line)
		# print parts
		place = int(parts[0])
		year = parts[1]
		name = parts[2]
		time = parts[3]
		school = parts[4]
		race = parts[5]
		course = parts[6]
		speed = parts[7]

		query =  "INSERT INTO ella (place, year, name, time, school, race, speed) VALUES (%s, %s, %s, %s, %s, %s, %s);"
		data = (place, year, name, time, school, race, speed)

		cursor.execute(query, data)

		print "Inserted: " + name

	conn.commit()

 
if __name__ == "__main__":
	main()