# all the imports which can be put in a separate .ini or .py file, loaded, and imported
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
        render_template, flash

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file, flaskr.py

#Load default config and override config from an environment variable
app.config.update(dict(
    DATABADE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True) # silent=True tells flask
# to not complain if the environment key 'FLASKR_SETTINGS' doesn't exist.

def connect_db():
    """Connects to the specified database."""
    rv = sqlite3.connect(app.config['DATABAE'])
    rv.row_factory = sqlite3.Row
    return rv
