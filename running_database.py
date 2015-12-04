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

def get_races(course):
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

    # creating the query
    # make if statements that allow an input to a function
        # each input should allow for a different "query =" statements with different table names
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

    print races
    return races


# you'll also need a function that gets race results for a given race, same as before,
# its just changing the query.

def get_results():
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
    # make if statements that allow an input to a function
        # each input should allow for a different "query =" statements with different table names
    # this will need to be fixed
    query =  "SELECT * FROM mis"

    cursor.execute(query,)
    conn.commit()

    results = cursor.fetchall()
    # makes it a list within a list instead of a tuple within a tuple
    results = list(map(list, zip(*results)))
    results = list(map(list, zip(*results)))

    # now we just need to figure out a way to only print the values of a specific race...
    
    # comment this out later
    # print results
    return results


if __name__ == "__main__":
    get_results()

