import numpy
import psycopg2
import sys
import re

def mean():

	for value in dict[time]:
		split(value)
		sumMins += mins
		sumSecs += float(secs)

	# Multiply mins by 60 to get seconds
	totalSum = float(sumSecs + (sumMins * 60))
	mean = float((totalSum / numRunners))

	return mean

def splitter(time):

	time_list = time.split(":", 2)
	mins = int(time_list[0])
	secs = float(time_list[1])
	time_in_secs = float(mins_to_secs(mins, secs))
	return time_in_secs

def mins_to_secs(mins, secs):

	temp_time = float(((mins * 60) + secs))
	return temp_time

def st_dev_michigan(myList1, myList2, myList3, myList4, 
	myList5, myList6, myList7, myList8, myList9, myList10):

	mean1 = float(mean_of_list(myList1))
	mean2 = float(mean_of_list(myList2))
	mean3 = float(mean_of_list(myList3))
	mean4 = float(mean_of_list(myList4))
	mean5 = float(mean_of_list(myList5))
	mean6 = float(mean_of_list(myList6))
	mean7 = float(mean_of_list(myList7))
	mean8 = float(mean_of_list(myList8))
	mean9 = float(mean_of_list(myList9))
	mean10 = float(mean_of_list(myList10))

	#mean_list = (mean1, mean2, mean3, mean4, mean5, mean6, mean7, mean8, mean9, mean10)

	mean_temp = float((mean1 + mean2 + mean3 + mean4 + mean5 + mean6 + mean7 + mean8 + mean9 + mean10)/10)
	
	sigma_value = (float(((mean1 - mean_temp)**2) + ((mean2 - mean_temp)**2) + ((mean3 - mean_temp)**2) + ((mean4 - mean_temp)**2) + ((mean5 - mean_temp)**2) + 
		((mean6 - mean_temp)**2) + ((mean7 - mean_temp)**2) + ((mean8 - mean_temp)**2) + ((mean9 - mean_temp)**2) + ((mean10 - mean_temp)**2)))
	
	st_dev_michigan_ = float((sigma_value/10)**0.5)

	#st_dev_michigan = float(numpy.std(mean_list))

	return st_dev_michigan_

def mean_michigan(myList1, myList2, myList3, myList4, 
	myList5, myList6, myList7, myList8, myList9, myList10):

	mean1 = float(mean_of_list(myList1))
	mean2 = float(mean_of_list(myList2))
	mean3 = float(mean_of_list(myList3))
	mean4 = float(mean_of_list(myList4))
	mean5 = float(mean_of_list(myList5))
	mean6 = float(mean_of_list(myList6))
	mean7 = float(mean_of_list(myList7))
	mean8 = float(mean_of_list(myList8))
	mean9 = float(mean_of_list(myList9))
	mean10 = float(mean_of_list(myList10))
	
	mean_michigan_ = float((mean1 + mean2 + mean3 + mean4 + mean5 + mean6 + mean7 + mean8 + mean9 + mean10)/ 10)

	return mean_michigan_

def mean_of_list(myList):
	
	sumList = 0

	for row in myList:
		sumList += row[6]
	mean_course = float((sumList / len(myList)))
	return mean_course

def std_dev_course(myList):

	std_dev_course = float(numpy.std(zip(*myList)[6]))
	return std_dev_course

def z_score_athlete(time_in_secs, mean_course_, std_dev_course_):

	z_score_athlete_ = (time_in_secs - mean_course_) / (std_dev_course_)

	return z_score_athlete_

def z_score_course(list1, mean_michigan_, std_dev_michigan_):

	mean_course = mean_of_list(list1)

	z_score_course = float((mean_course - mean_michigan_) / (std_dev_michigan_))

	return z_score_course

def calc_speed_rating(z_score_course_, z_score_athlete_):

	speed_rating = float(50 + (-1 *(z_score_course_ * 3)) + (-1 * (z_score_athlete_ * 30)))

	return speed_rating

def speed_rating_loop(list1, z_score_course_):

	mean_course_ = 0.0
	std_dev_course_ = 0.0

	mean_course_ = mean_of_list(list1)
	std_dev_course_ = std_dev_course(list1)

	i = 0
	for row in list1:
		z_score_athlete_ = z_score_athlete(row[6], mean_course_, std_dev_course_)
		speed_rating = float(calc_speed_rating(z_score_course_, z_score_athlete_))
		list1[i].append(speed_rating)
		i = i + 1

if __name__ == "__main__":
	
	'''
	_________________________________________________
	'''


	#MIS
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
	cursor.execute("SELECT * FROM mis_states_2015")
	
	mis = []
	i = 0
	for row in cursor.fetchall():
		mis.append(row)
		temp = splitter(row[3])
		mis[i] = list(mis[i])
		mis[i].append(temp)
		i = i + 1
		
	conn.close()

	'''
	_________________________________________________
	'''


	#Huron Meadows

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
	cursor.execute("SELECT * FROM huron_meadows_metropark_2015")
	
	huron_mp = []
	i = 0
	for row in cursor.fetchall():
		huron_mp.append(row)
		temp = splitter(row[3])
		huron_mp[i] = list(huron_mp[i])
		huron_mp[i].append(temp)
		i = i + 1
		
	conn.close()

	'''
	_________________________________________________
	'''

	#Willow Metropark

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
	cursor.execute("SELECT * FROM willow_metropark_2015")
	
	willow_mp = []
	i = 0
	for row in cursor.fetchall():
		willow_mp.append(row)
		temp = splitter(row[3])
		willow_mp[i] = list(willow_mp[i])
		willow_mp[i].append(temp)
		i = i + 1
		
	conn.close()

	'''
	_________________________________________________
	'''

	#Portage

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
	cursor.execute("SELECT * FROM portage_2k15")
	
	portage_ms = []
	i = 0
	for row in cursor.fetchall():
		portage_ms.append(row)
		temp = splitter(row[3])
		portage_ms[i] = list(portage_ms[i])
		portage_ms[i].append(temp)
		i = i + 1
		
	conn.close()

	'''
	_________________________________________________
	'''

	#Forest Akers

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
	cursor.execute("SELECT * FROM spartanfixed2_2015")
	
	forest_ak = []
	i = 0
	for row in cursor.fetchall():
		forest_ak.append(row)
		temp = splitter(row[3])
		forest_ak[i] = list(forest_ak[i])
		forest_ak[i].append(temp)
		i = i + 1
		
	conn.close()


	'''
	_________________________________________________
	'''


	#Springfield Oaks

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
	cursor.execute("SELECT * FROM nholly_2015")
	
	spring_ok = []
	i = 0
	for row in cursor.fetchall():
		spring_ok.append(row)
		temp = splitter(row[3])
		spring_ok[i] = list(spring_ok[i])
		spring_ok[i].append(temp)
		i = i + 1
		
	conn.close()

	'''
	_________________________________________________
	'''

	#Ella Sharp

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
	cursor.execute("SELECT * FROM ella_sharp_park_15")
	
	ella_sp = []
	i = 0
	for row in cursor.fetchall():
		ella_sp.append(row)
		temp = splitter(row[3])
		ella_sp[i] = list(ella_sp[i])
		ella_sp[i].append(temp)
		i = i + 1
		
	conn.close()

	
	'''
	_________________________________________________
	'''

	#Bloomer Park

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
	cursor.execute("SELECT * FROM bloomer_park_2015")
	
	bloom_pk = []
	i = 0
	for row in cursor.fetchall():
		bloom_pk.append(row)
		temp = splitter(row[3])
		bloom_pk[i] = list(bloom_pk[i])
		bloom_pk[i].append(temp)
		i = i + 1
		
	conn.close()

	'''
	_________________________________________________
	'''

	#Uncle John's Cider Mill

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
	cursor.execute("SELECT * FROM uncle_johns_cider_mill_2015")
	
	uncle_cm = []
	i = 0
	for row in cursor.fetchall():
		uncle_cm.append(row)
		temp = splitter(row[3])
		uncle_cm[i] = list(uncle_cm[i])
		uncle_cm[i].append(temp)
		i = i + 1
		
	conn.close()

	'''
	_________________________________________________
	'''

	#Lake Erie Metropark

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
	cursor.execute("SELECT * FROM lake_erie_metropark_2015")
	
	lake_mp = []
	i = 0
	for row in cursor.fetchall():
		lake_mp.append(row)
		temp = splitter(row[3])
		lake_mp[i] = list(lake_mp[i])
		lake_mp[i].append(temp)
		i = i + 1
		
	conn.close()
	'''
	_________________________________________________
	'''

	mean_michigan = mean_michigan(mis, huron_mp, willow_mp, portage_ms, forest_ak, spring_ok, ella_sp, bloom_pk, uncle_cm, lake_mp)
		
	st_dev_michigan_ = st_dev_michigan(mis, huron_mp, willow_mp, portage_ms, forest_ak, spring_ok, ella_sp, bloom_pk, uncle_cm, lake_mp)

	mis_std_dev = std_dev_course(mis)

	mean_test = mean_of_list

	z_score_mis = z_score_course(mis, mean_michigan, st_dev_michigan_)
	z_score_huron_mp = z_score_course(huron_mp, mean_michigan, st_dev_michigan_)
	z_score_willow_mp = z_score_course(willow_mp, mean_michigan, st_dev_michigan_)
	z_score_portage_ms = z_score_course(portage_ms, mean_michigan, st_dev_michigan_)
	z_score_forest_ak = z_score_course(forest_ak, mean_michigan, st_dev_michigan_)
	z_score_spring_ok = z_score_course(spring_ok, mean_michigan, st_dev_michigan_)
	z_score_ella_sp = z_score_course(ella_sp, mean_michigan, st_dev_michigan_)
	z_score_bloom_pk = z_score_course(bloom_pk, mean_michigan, st_dev_michigan_)
	z_score_uncle_cm = z_score_course(uncle_cm, mean_michigan, st_dev_michigan_)
	z_score_lake_mp = z_score_course(lake_mp, mean_michigan, st_dev_michigan_)

	speed_rating_loop(mis, z_score_mis)
	speed_rating_loop(huron_mp, z_score_huron_mp)
	speed_rating_loop(willow_mp, z_score_willow_mp)
	speed_rating_loop(portage_ms, z_score_portage_ms)
	speed_rating_loop(forest_ak, z_score_forest_ak)
	speed_rating_loop(spring_ok, z_score_spring_ok)
	speed_rating_loop(ella_sp, z_score_ella_sp)
	speed_rating_loop(bloom_pk, z_score_bloom_pk)
	speed_rating_loop(uncle_cm, z_score_uncle_cm)
	speed_rating_loop(lake_mp, z_score_lake_mp)

	print mis

	'''

	'''
	#_________________________________________________
	'''
	#MIS
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
	i = 0
	for index in mis:
		if i < len(mis):
			place = str(mis[i][0])
			year = str(mis[i][1])
			name = str(mis[i][2])
			time = str(mis[i][3])
			school = str(mis[i][4])
			race_name = str(mis[i][5])
			speed_rating = str(mis[i][7])

			query =  "INSERT INTO mis (place, year, name, time, school, race_name, speed_rating) VALUES (%s, %s, %s, %s, %s, %s, %s);"
			data = (place, year, name, time, school, race_name, speed_rating)

			cursor.execute(query, data)

			print "Inserted: " + name
			i = i + 1

	conn.commit()
	conn.close()

	'''
	#_________________________________________________
	'''
	#Huron Meadows
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
	i = 0
	for index in huron_mp:
		if i < len(huron_mp):
			place = str(huron_mp[i][0])
			year = str(huron_mp[i][1])
			name = str(huron_mp[i][2])
			time = str(huron_mp[i][3])
			school = str(huron_mp[i][4])
			race_name = str(huron_mp[i][5])
			speed_rating = str(huron_mp[i][7])

			query =  "INSERT INTO huron (place, year, name, time, school, race_name, speed_rating) VALUES (%s, %s, %s, %s, %s, %s, %s);"
			data = (place, year, name, time, school, race_name, speed_rating)

			cursor.execute(query, data)

			print "Inserted: " + name
			i = i + 1

	conn.commit()
	conn.close()

	'''
	#_________________________________________________
	'''
	#Willow MetroPark
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
	i = 0
	for index in willow_mp:
		if i < len(willow_mp):
			place = str(willow_mp[i][0])
			year = str(willow_mp[i][1])
			name = str(willow_mp[i][2])
			time = str(willow_mp[i][3])
			school = str(willow_mp[i][4])
			race_name = str(willow_mp[i][5])
			speed_rating = str(willow_mp[i][7])

			query =  "INSERT INTO willow (place, year, name, time, school, race_name, speed_rating) VALUES (%s, %s, %s, %s, %s, %s, %s);"
			data = (place, year, name, time, school, race_name, speed_rating)

			cursor.execute(query, data)

			print "Inserted: " + name
			i = i + 1

	conn.commit()
	conn.close()

	'''
	#_________________________________________________
	'''
	#Portage MS
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
	i = 0
	for index in portage_ms:
		if i < len(portage_ms):
			place = str(portage_ms[i][0])
			year = str(portage_ms[i][1])
			name = str(portage_ms[i][2])
			time = str(portage_ms[i][3])
			school = str(portage_ms[i][4])
			race_name = str(portage_ms[i][5])
			speed_rating = str(portage_ms[i][7])

			query =  "INSERT INTO portage (place, year, name, time, school, race_name, speed_rating) VALUES (%s, %s, %s, %s, %s, %s, %s);"
			data = (place, year, name, time, school, race_name, speed_rating)

			cursor.execute(query, data)

			print "Inserted: " + name
			i = i + 1

	conn.commit()
	conn.close()

	'''
	#_________________________________________________
	'''
	#Forest Akers
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
	i = 0
	for index in forest_ak:
		if i < len(forest_ak):
			place = str(forest_ak[i][0])
			year = str(forest_ak[i][1])
			name = str(forest_ak[i][2])
			time = str(forest_ak[i][3])
			school = str(forest_ak[i][4])
			race_name = str(forest_ak[i][5])
			speed_rating = str(forest_ak[i][7])

			query =  "INSERT INTO spartan (place, year, name, time, school, race_name, speed_rating) VALUES (%s, %s, %s, %s, %s, %s, %s);"
			data = (place, year, name, time, school, race_name, speed_rating)

			cursor.execute(query, data)

			print "Inserted: " + name
			i = i + 1

	conn.commit()
	conn.close()

	'''
	#_________________________________________________
	'''
	#Springfield Oaks
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
	i = 0
	for index in spring_ok:
		if i < len(spring_ok):
			place = str(spring_ok[i][0])
			year = str(spring_ok[i][1])
			name = str(spring_ok[i][2])
			time = str(spring_ok[i][3])
			school = str(spring_ok[i][4])
			race_name = str(spring_ok[i][5])
			speed_rating = str(spring_ok[i][7])

			query =  "INSERT INTO nholly (place, year, name, time, school, race_name, speed_rating) VALUES (%s, %s, %s, %s, %s, %s, %s);"
			data = (place, year, name, time, school, race_name, speed_rating)

			cursor.execute(query, data)

			print "Inserted: " + name
			i = i + 1

	conn.commit()
	conn.close()

	'''
	#_________________________________________________
	'''
	#Ella Sharp Park
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
	i = 0
	for index in ella_sp:
		if i < len(ella_sp):
			place = str(ella_sp[i][0])
			year = str(ella_sp[i][1])
			name = str(ella_sp[i][2])
			time = str(ella_sp[i][3])
			school = str(ella_sp[i][4])
			race_name = str(ella_sp[i][5])
			speed_rating = str(ella_sp[i][7])

			query =  "INSERT INTO ella (place, year, name, time, school, race_name, speed_rating) VALUES (%s, %s, %s, %s, %s, %s, %s);"
			data = (place, year, name, time, school, race_name, speed_rating)

			cursor.execute(query, data)

			print "Inserted: " + name
			i = i + 1

	conn.commit()
	conn.close()

	'''
	#_________________________________________________
	'''
	#Bloomer Park
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
	i = 0
	for index in bloom_pk:
		if i < len(bloom_pk):
			place = str(bloom_pk[i][0])
			year = str(bloom_pk[i][1])
			name = str(bloom_pk[i][2])
			time = str(bloom_pk[i][3])
			school = str(bloom_pk[i][4])
			race_name = str(bloom_pk[i][5])
			speed_rating = str(bloom_pk[i][7])

			query =  "INSERT INTO bloomer (place, year, name, time, school, race_name, speed_rating) VALUES (%s, %s, %s, %s, %s, %s, %s);"
			data = (place, year, name, time, school, race_name, speed_rating)

			cursor.execute(query, data)

			print "Inserted: " + name
			i = i + 1

	conn.commit()
	conn.close()

	'''
	#_________________________________________________
	'''
	#Uncle John's Cider Mill
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
	i = 0
	for index in uncle_cm:
		if i < len(uncle_cm):
			place = str(uncle_cm[i][0])
			year = str(uncle_cm[i][1])
			name = str(uncle_cm[i][2])
			time = str(uncle_cm[i][3])
			school = str(uncle_cm[i][4])
			race_name = str(uncle_cm[i][5])
			speed_rating = str(uncle_cm[i][7])

			query =  "INSERT INTO uncle (place, year, name, time, school, race_name, speed_rating) VALUES (%s, %s, %s, %s, %s, %s, %s);"
			data = (place, year, name, time, school, race_name, speed_rating)

			cursor.execute(query, data)

			print "Inserted: " + name
			i = i + 1

	conn.commit()
	conn.close()

	'''
	#_________________________________________________
	'''
	#Lake Erie MetroPark
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
	i = 0
	for index in lake_mp:
		if i < len(lake_mp):
			place = str(lake_mp[i][0])
			year = str(lake_mp[i][1])
			name = str(lake_mp[i][2])
			time = str(lake_mp[i][3])
			school = str(lake_mp[i][4])
			race_name = str(lake_mp[i][5])
			speed_rating = str(lake_mp[i][7])

			query =  "INSERT INTO lake_erie (place, year, name, time, school, race_name, speed_rating) VALUES (%s, %s, %s, %s, %s, %s, %s);"
			data = (place, year, name, time, school, race_name, speed_rating)

			cursor.execute(query, data)

			print "Inserted: " + name
			i = i + 1

	conn.commit()
	conn.close()

	'''
	#_________________________________________________
	'''
	'''



