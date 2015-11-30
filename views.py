from flask import render_template, request
from app import app
from schedule_api import *

@app.route('/')
def index():
    options = {}

    options['terms'] = get_terms()

    return render_template('index.html', **options)

@app.route('/about')
def index():
    options = {}

    options['terms'] = get_terms()

    return render_template('about.html', **options)