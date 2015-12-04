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
    query =  "SELECT table_name FROM information_schema.columns WHERE column_name='race_name';"

    cursor.execute(query,)
    conn.commit()

    results = cursor.fetchall()
    # comment this out later
    # print results
    return results


# you'll need a function that gets a list of races from the database provided a course name,
# which will look similar but the main difference is that the "query" will be different.

def get_races():
    ''' 
    Return the PostgresSQL data for all of the
    valid courses.
    '''
    #Define our connection string
    conn_string = "host='pellefant-01.db.elephantsql.com' dbname='rphkcioy' user='rphkcioy' password='tlFXsKFJHBOewOTyKvadX-CMbQnCOm0j'"
    
    # print the connection string we will use to connect
    print "Connecting to database\n ->%s" % (conn_string)

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    #print "Connected!\n"

    # creating the query WHERE column_name='race_name';"
    # this will need to be fixed
    query =  "SELECT * FROM mis"

    cursor.execute(query,)
    conn.commit()

    #This puts all MIS results into a tuple of lists
    results = cursor.fetchall()
    # transposes list
    results = list(map(list, zip(*results)))
    # pulls out all of race names of the lists
    for n in results:
        results = list(results)
        races = []
        races.append(results[5])

    # races is now a list of all of the names of the races at the course in one list
    races = races[0]
    # races is now a list of the names of the races
    for n in races:
        

    print races
    return races


# you'll also need a function that gets race results for a given race, same as before,
# its just changing the query.

def get_results(race):
    ''' 
    Return the PostgresSQL data for all of the
    valid courses.
    '''
    #Define our connection string
    conn_string = "host='pellefant-01.db.elephantsql.com' dbname='rphkcioy' user='rphkcioy' password='tlFXsKFJHBOewOTyKvadX-CMbQnCOm0j'"

    # print the connection string we will use to connect
    print "Connecting to database\n ->%s" % (conn_string)

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    print "Connected!\n"

    # creating the query
    # this will need to be fixed
    query =  "SELECT table_name FROM information_schema.columns WHERE column_name='race';"

    cursor.execute(query,)
    conn.commit()

    results = cursor.fetchall()
    # comment this out later
    # print results
    return results


#if __name__ == "__main__":
    #get_races()

