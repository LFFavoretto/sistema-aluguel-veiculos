from app import app
from flask import render_template as rt

@app.route('/')
@app.route('/index')

def index():
    return rt('index.html')
























