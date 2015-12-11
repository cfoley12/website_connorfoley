from flask import render_template, request
from app import app
from schedule_api import *
from running_database import *

@app.route('/')
def index():
    options = {}

    # options['terms'] = get_terms()

    return render_template('index.html', **options)

@app.route('/about.html')
def about():
    options = {}

    options['terms'] = get_terms()

    return render_template('about.html', **options)

@app.route('/rankings.html')
def rankings():
    options = {}

    # get the courses, comment in to use
    options['courses'] = get_courses()
    # add in get_course function
    # translation = dict(mis="Michigan International Speedway (MIS), Brooklyn, MI", willow="Willow Metropark, New Boston, MI", portage="Portage West MS, Portage, MI", spartan="Forest Akers East Golf Course, East Lansing, MI", huron="Huron Meadows Metropark, Brighton, MI", lake_erie="Lake Erie Metropark, Brownstown, MI", nholly="Springfield Oaks County Park, Davisburg, MI", ella="Ella Sharp Park, Jackson, MI", bloomer="Bloomer Park, Rochester Adams, MI", uncle="Uncle John's Cider Mill, St. John's, MI")

    print options

    return render_template('rankings.html', **options)

@app.route('/races/<course_name>')
def races(course_name):
    options = {}

    # get the races, comment in to use
    options['races'] = get_races(course_name)
    options['course_name'] = course_name
    # add in get_race function

    print options

    return render_template('races.html', **options)

@app.route('/results/<race_name>/')
def results(race_name):
    options = {}
    course_name = request.args['course']
    # get the results, comment in to use
    options['results'] = get_results(race_name, course_name)
    # add in get_results function
    print options['results']
    return render_template('results.html', **options)
	
@app.route('/calculator.html')
def calculator():
    options = {}

    options['courses'] = get_courses()

    return render_template('calculator.html', **options)

@app.route('/calculator.php')
def calculator_results():
    options = {}

    options['courses'] = get_courses()

    return render_template('calculator.php', **options)

