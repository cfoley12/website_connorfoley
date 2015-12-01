from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config['DEBUG'] = True

def get_resource_as_string(name, charset='utf-8'):
    with app.open_resource(name) as f:
        return f.read().decode(charset)

app.jinja_env.globals['get_resource_as_string'] = get_resource_as_string