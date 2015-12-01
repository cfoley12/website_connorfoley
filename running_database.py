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
    conn_string = "host='' dbname='' user='' password=''"

    # print the connection string we will use to connect
    # print "Connecting to database\n ->%s" % (conn_string)

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    # print "Connected!\n"

    # creating the query
    # query =  "SELECT table_name  FROM information_schema.tables WHERE table_schema='public' AND column_name='race_name'   AND table_type='BASE TABLE';"
    query =  "SELECT table_name FROM information_schema.columns WHERE column_name='race_name';"

    cursor.execute(query,)
    # conn.commit()

    results = cursor.fetchall()
    return results


# you'll need a function that gets a list of races from the database provided a course name,
# which will look similar but the main difference is that the "query" will be different.


# you'll also need a function that gets race results for a given race, same as before,
# its just changing the query.

