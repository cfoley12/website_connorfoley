import psycopg2
import sys
import re
import numpy
 
def main():

	def mins_to_secs(mins, secs):

		temp_time = ((mins * 60) + secs)
		return temp_time

	def splitter(time):

		time_list = time.split(":", 2)
		mins = int(time_list[0])
		secs = float(time_list[1])
		time_in_secs = float(mins_to_secs(mins, secs))

		return time_in_secs

	def mean_of_list(myList):
	
		sumList = 0

		for row in myList:
			sumList += row[5]
		mean = (sumList / len(myList))
		return mean

	def std_dev_course(myList):

		std_dev_course = numpy.std(zip(*myList)[5])
		return std_dev_course

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

	cursor.execute("SELECT * FROM mhsaa_d1_states_2015")
	'''
	make sure to set the number of entrants before running the program
	'''
	
	total = []
	i = 0

	'''
	for row in cursor.fetchall():
		total.append(row)
		tempList = splitter(row[3])
		total[i] = list(total[i])
		total[i].append(tempList)
		i = i +1
	'''
	for row in cursor.fetchall():
		#total.append(row)
		#temp = splitter(row[3])
		#total[i] = list(total[i])
		#total[i].append(temp)
		#i = i + 1
		print row[3]
		
		

	    #total.append(splitter(row[3]))
		

	conn.close()

	#print total



 
if __name__ == "__main__":
	main()

	



