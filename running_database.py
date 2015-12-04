import json
import time
import requests
import psycopg2
import sys
import re

def get_courses():
    '''
    Return the PostgresSQL data for all of the
    valid courses.
    '''
    #Define our connection string
    conn_string = "host='pellefant-01.db.elephantsql.com' dbname='rphkcioy' user='rphkcioy' password='tlFXsKFJHBOewOTyKvadX-CMbQnCOm0j'"

    # print the connection string we will use to connect
    # print "Connecting to database\n ->%s" % (conn_string)

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    # print "Connected!\n"

    # creating the query
    # query =  "SELECT compiled_races  FROM information_schema.tables WHERE table_schema='public' AND column_name='course'   AND table_type='BASE TABLE';"
    query =  "SELECT table_name FROM information_schema.columns WHERE column_name = 'race_name';"

    cursor.execute(query)
    conn.commit()

    courses = cursor.fetchall()
    # comment this out later
    # print results
    # print courses 

    courseStrings = []

    for courseTuple in courses:
        courseStrings.append(courseTuple[0])

    
    return courseStrings


# you'll need a function that gets a list of races from the database provided a course name,
# which will look similar but the main difference is that the "query" will be different.

def get_races(course):
    ''' 
    Return the PostgresSQL data for all of the
    valid courses.
    '''
    #Define our connection string
    conn_string = "host='pellefant-01.db.elephantsql.com' dbname='xbmscouy' user='xbmscouy' password='yOu5MzMJwp4D8QxJtL1Es1z8sf4XiVtV'"
    
    # print the connection string we will use to connect
    print "Connecting to database\n ->%s" % (conn_string)

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    #print "Connected!\n"

    # creating the query
    # make if statements that allow an input to a function
        # each input should allow for a different "query =" statements with different table names
    # this will need to be fixed
    
    if course == 'huron':
        query = "SELECT * FROM Huron_Meadows_Metro_Park"
    if course == 'lake_erie':
        query = "SELECT * FROM Lake_Erie_Metro_Park"
    if course == 'nholly':
        query = "SELECT * FROM Springfield_Oaks_Metro_Park"
    if course == 'ella':
        query = "SELECT * FROM Ella_Sharp_Park"
    if course == 'bloomer':
        query = "SELECT * FROM Bloomer_Park"
    if course == 'uncle':
        query = "SELECT * FROM Uncle_Johns_Cider_Mill"
    if course == 'portage':
        query = "SELECT * FROM Portage_Middle_School"
    if course == 'mis':
        query = "SELECT * FROM Michigan_International_Speedway"
    if course == 'willow':
        query = "SELECT * FROM Willow_Metro_Park"
    if course == 'spartan':
        query = "SELECT * FROM Forest_Akers_East_Golf_Course"

    cursor.execute(query)
    conn.commit()
    

    #This puts all MIS results into a tuple of lists
    races = cursor.fetchall()
    # transposes list
    #results = list(map(list, zip(*results)))
    # pulls out all of race names of the lists
    print races
    raceStrings = []
    for raceTuple in races:
        raceStrings.append(raceTuple[0])

    # races is now a list of all of the names of the races at the course in one list
    #races = races[0]
    # races is now a list of the names of the races

    
    return raceStrings


# you'll also need a function that gets race results for a given race, same as before,
# its just changing the query.

def get_results(race_name, course_name):
    # ''' 
    # Return the PostgresSQL data for all of the
    # valid courses.
    # '''
    #Define our connection string
    conn_string = "host='pellefant-01.db.elephantsql.com' dbname='rphkcioy' user='rphkcioy' password='tlFXsKFJHBOewOTyKvadX-CMbQnCOm0j'"

    # print the connection string we will use to connect
    # print "Connecting to database\n ->%s" % (conn_string)

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    # print "Connected!\n"
    if race_name == "AARC Early Bird Open":
        db_race_name = "aarc_early_bird"
    if race_name == "MHSAA Regional 04-1":
        db_race_name = "04_1_regionals"
    if race_name == "KLAA Kensington Conference Finals Varsity":
        db_race_name = "klaa_varsity"
    if race_name == "KLAA Kensington Conference Finals JV":
        db_race_name = "klaa_jv"
    if race_name == "River Rat Open Sub 20 Minutes":
        db_race_name = "river_rat_sub20"
    if race_name == "River Rat Open Over 20 Minutes":
        db_race_name = "river_rat_over20"
    # creating the query
    # make if statements that allow an input to a function
        # each input should allow for a different "query =" statements with different table names
    # this will need to be fixed
    query =  "SELECT * FROM " + course_name + " WHERE race_name LIKE '%" + db_race_name + "%'"
    print query
    cursor.execute(query)
    conn.commit()

    resultList = cursor.fetchall()
    # makes it a list within a list instead of a tuple within a tuple
    # '''
    # results = list(map(list, zip(*results)))
    # results = list(map(list, zip(*results)))
    # '''
    # now we just need to figure out a way to only print the values of a specific race...
    
    # comment this out later
    # print resultList
    return resultList


if __name__ == "__main__":
    get_courses()