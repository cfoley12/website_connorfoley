from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config['DEBUG'] = True

url_for('static', filename='stylesheet.css')