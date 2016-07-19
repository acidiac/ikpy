import os
from flask import Flask, url_for, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy 
from datetime import datetime

# setting the db path to the root path of the folder
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir,'../data.sqlite')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'+db_path

db = SQLAlchemy(app)

'''
	SQLAlchemy Available Types:
	---------------------------	
	Integer 		-	an integer
	String (size) 	- 	a string with a maximum length
	Text  			- 	some longer unicode text
	DateTime 		-	date and time expressed as Python datetime object.
	Float 			-	stores floating point values
	Boolean 		-	stores a boolean value
	PickleType 		-	stores a pickled Python object
	LargeBinary	 	-   
	stores large arbitrary binary data
'''


class ValidationError(ValueError):
	"""docstring for ValidationError"""
	pass

class IKAssets(db.Model):
	"""

		Defining the database model for Organizations table.
		Version 0.0.2, Date: 19-07-2016 author: Amit Chanchal
		DB Table Schema:
		id	
		name	
		category_id	
		Legal 
		Type	
		Activity	
		description	
		geo_village	
		geo_district	
		geo_state	
		geo_country	
		geo_pincode	
		phone	
		address	
		social_website	
		social_linkedin	
		social_twitter	
		social_facebook	
		social_instagram	
		email	
		startdate	
		admin

	"""
	__tablename__ = 'organizations'
	'''
	
	'''
	id = db.Column(db.Integer, primary_key = True)

	
		
		
