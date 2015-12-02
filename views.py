from flask import render_template, request
from app import app
# from schedule_api import *
from running_database import *

@app.route('/')
def index():
    options = {}

    # options['terms'] = get_terms()

    return render_template('index.html', **options)

@app.route('/about.html')
def about():
    options = {}

    # options['terms'] = get_terms()

    return render_template('about.html', **options)

@app.route('/rankings.html')
def rankings():
    options = {}

    # get the courses, comment in to use
    # options['courses'] = get_courses()
    # add in get_course function

    return render_template('rankings.html', **options)

@app.route('/races/<course_name>')
def races():
    options = {}

    # get the races, comment in to use
    # options['races'] = get_races(course_name)
    # add in get_race function

    return render_template('races.html', **options)

@app.route('/results/<race_name>/')
def results():
    options = {}

    # get the results, comment in to use
    # options['results'] = get_results(race_name)
    # add in get_results function

    return render_template('results.html', **options)
	