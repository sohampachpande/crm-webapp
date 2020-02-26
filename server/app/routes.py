from flask import render_template
from app import app
from pymongo import MongoClient


@app.route('/')
@app.route('/home')
def homepage():
	return render_template('home.html')