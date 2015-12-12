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


    courseStrings = [course.replace('huron', "Huron Meadows Metropark, Brighton, MI") for course in courseStrings]
    courseStrings = [course.replace('lake_erie', "Lake Erie Metropark, Brownstown, MI") for course in courseStrings]
    courseStrings = [course.replace('nholly', "Springfield Oaks County Park, Davisburg, MI") for course in courseStrings]
    courseStrings = [course.replace('bloomer', "Bloomer Park, Rochester Adams, MI") for course in courseStrings]
    courseStrings = [course.replace('ella', "Ella Sharp Park, Jackson, MI") for course in courseStrings]
    courseStrings = [course.replace('uncle', "Uncle John's Cider Mill, St. John's, MI") for course in courseStrings]
    courseStrings = [course.replace('portage', "Portage West MS, Portage, MI") for course in courseStrings]
    courseStrings = [course.replace('mis', "Michigan International Speedway (MIS), Brooklyn, MI") for course in courseStrings]
    courseStrings = [course.replace('willow', "Willow Metropark, New Boston, MI") for course in courseStrings]
    courseStrings = [course.replace('spartan', "Forest Akers East Golf Course, East Lansing, MI") for course in courseStrings]

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
    
    if course == 'Huron Meadows Metropark, Brighton, MI':
        query = "SELECT * FROM Huron_Meadows_Metro_Park"
    if course == 'Lake Erie Metropark, Brownstown, MI':
        query = "SELECT * FROM Lake_Erie_Metro_Park"
    if course == 'Springfield Oaks County Park, Davisburg, MI':
        query = "SELECT * FROM Springfield_Oaks_County_Park"
    if course == 'Ella Sharp Park, Jackson, MI':
        query = "SELECT * FROM Ella_Sharp_Park"
    if course == 'Bloomer Park, Rochester Adams, MI':
        query = "SELECT * FROM Bloomer_Park"
    if course == "Uncle John's Cider Mill, St. John's, MI":
        query = "SELECT * FROM Uncle_Johns_Cider_Mill"
    if course == 'Portage West MS, Portage, MI':
        query = "SELECT * FROM Portage_Middle_School"
    if course == 'Michigan International Speedway (MIS), Brooklyn, MI':
        query = "SELECT * FROM Michigan_International_Speedway"
    if course == 'Willow Metropark, New Boston, MI':
        query = "SELECT * FROM Willow_Metropark"
    if course == 'Forest Akers East Golf Course, East Lansing, MI':
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

    # adjusting race_names appropriately
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
    if race_name == "Adams-Cicciarelli Invitational Varsity":
        db_race_name = "Adams_Cic_Invite 2"
    if race_name == "Adams-Cicciarelli Invitational Varsity":
        db_race_name = "Adams_Cic_Invite"
    if race_name == "OAA Red Jamboree 1 Varsity":
        db_race_name = "Red_Jamb1"
    if race_name == "OAA - Red Championships Varsity":
        db_race_name = "Red_Champs"
    if race_name == "OAA - Red Championships JV":
        db_race_name = "Red_ChampsJV"
    if race_name == "OAA White Jamboree 2 Varsity":
        db_race_name = "White_Jamb" 
    if race_name == "MHSAA Regional 25-3":
        db_race_name = "Reg_25-3"
    if race_name == "MHSAA Regional 33-4":
        db_race_name = "Reg_33-4"    
    if race_name == "Jackson HS Invite Division 1":
        db_race_name = "JacksonInviteD1"
    if race_name == "Jackson HS Invite Division 2":
        db_race_name = "JacksonInviteD2"
    if race_name == "Jackson HS Invite Division 3 & 4":
        db_race_name = "JacksonInviteD3-4"
    if race_name == "Warrior Classic Varsity":
        db_race_name = "WarriorClassic"
    if race_name == "MHSAA Regional 05-1":
        db_race_name = "Reg_5-1"
    if race_name == "MHSAA Regional 18-2":
        db_race_name = "Reg_18-2"        
    if race_name == "Marauder Invitational":
        db_race_name = "Marauder_Invitational"
    if race_name == "MHSAA Regional 27-3":
        db_race_name = "Reg_27-3"
    if race_name == "Division 1 Championships":
        db_race_name = "D1"
    if race_name == "Division 2 Championships":
        db_race_name = "D2"
    if race_name == "Division 3 Championships":
        db_race_name = "D3"
    if race_name == "Division 4 Championships":
        db_race_name = "D4"
    if race_name == "Nike-Holly-Duane Raffin Festival of Races Division 1":
        db_race_name = "NHolly D1"
    if race_name == "Nike-Holly-Duane Raffin Festival of Races Division 2":
        db_race_name = "NHolly D2"
    if race_name == "Nike-Holly-Duane Raffin Festival of Races Division 3":
        db_race_name = "NHolly D3"
    if race_name == "Nike-Holly-Duane Raffin Festival of Races Division 4":
        db_race_name = "NHolly D4"
    if race_name == "Nike-Holly-Duane Raffin Festival of Races Division 5":
        db_race_name = "NHolly D5"
    if race_name == "Portage Invite Division 1 Varsity":
        db_race_name = "VarD1"
    if race_name == "Portage Invite Division 2 Varsity":
        db_race_name = "VarD2"
    if race_name == "Portage Invite Division 2 JV":
        db_race_name = "JVD2"
    if race_name == "Portage Invite Division 4 Varsity":
        db_race_name = "VarD4"
    if race_name == "Portage Invite Division 3 Varsity":
        db_race_name = "VarD3"
    if race_name == "MSU Spartan Invitational Elite Race":
        db_race_name = "Spartan Elite"
    if race_name == "MSU Spartan Invitational Green Race (D1 & D2)":
        db_race_name = "Spartan D12"
    if race_name == "MSU Spartan Invitational Bronze Race (D2 & D3)":
        db_race_name = "Spartan D23"
    if race_name == "MSU Spartan Invitational White Race (D3 & D4)":
        db_race_name = "Spartan D34"
    if race_name == "MSU Spartan Invitational JV 1":
        db_race_name = "Spartan JV1"
    if race_name == "Fowler Cider Mill Invite Varsity and JV":
        db_race_name = "FolwerCiderMill"
    if race_name == "TVC Central Jamboree 2 Varsity and JV":
        db_race_name = "TVCCentralJamb"
    if race_name == "Marauder Invite Large Schools":
        db_race_name = "MarauderInvite"
    if race_name == "MHSAA Regional 14-2":
        db_race_name = "Reg_14-2"
    if race_name == "MHSAA Regional 23-3":
        db_race_name = "Reg_23-3"
    if race_name == "MHSAA Regional 06-1":
        db_race_name = "06_1_regionals"
    if race_name == "MHSAA Regional 36-4":
        db_race_name = "36_4_regionals"
    if race_name == "Wayne County Championship JV":
        db_race_name = "wayne_co_jv"
    if race_name == "Wayne County Championship Varsity":
        db_race_name = "wayne_co_varsity"
    if race_name == "Ramblin Rock Invitational Varsity":
        db_race_name = "ramblin_rock_varsity"
    if race_name == "Ramblin Rock Invitational JV":
        db_race_name = "ramblin_rock_jv"

    # adjusting course names accordingly
    if course_name == "Huron Meadows Metropark, Brighton, MI":
        db_course_name = "huron"
    if course_name == "Lake Erie Metropark, Brownstown, MI":
        db_course_name = "lake_erie"
    if course_name == "Springfield Oaks County Park, Davisburg, MI":
        db_course_name = "nholly"
    if course_name == "Bloomer Park, Rochester Adams, MI":
        db_course_name = "bloomer"
    if course_name == "Ella Sharp Park, Jackson, MI":
        db_course_name = "ella"
    if course_name == "Uncle John's Cider Mill, St. John's, MI":
        db_course_name = "uncle"
    if course_name == "Portage West MS, Portage, MI":
        db_course_name = "portage"
    if course_name == "Michigan International Speedway (MIS), Brooklyn, MI":
        db_course_name = "mis"
    if course_name == "Willow Metropark, New Boston, MI":
        db_course_name = "willow"
    if course_name == "Forest Akers East Golf Course, East Lansing, MI":
        db_course_name = "spartan"

    # creating the query
    # make if statements that allow an input to a function
        # each input should allow for a different "query =" statements with different table names
    # this will need to be fixed
    query =  "SELECT * FROM " + db_course_name + " WHERE race_name LIKE '%" + db_race_name + "%'"
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


'''if __name__ == "__main__":
    get_races("Huron Meadows Metropark, Brighton, MI")'''