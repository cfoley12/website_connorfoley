from flask import render_template, request
from app import app
from schedule_api import *

@app.route('/')
def index():
    options = {}

    options['terms'] = get_terms()

    return render_template('index.html', **options)

@app.route('/about.html')
def about():
    options = {}

    options['terms'] = get_terms()

    return render_template('about.html', **options)

@app.route('/rankings.html')
def rankings():
    options = {}

    options['terms'] = get_terms()

    return render_template('rankings.html', **options)

@app.route('/mis.html')
def mis():
    options = {}

    options['terms'] = get_terms()

    return render_template('mis.html', **options)