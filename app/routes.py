from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    retrun render_template('index.html')
