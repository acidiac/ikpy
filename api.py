# -*- coding: utf-8 -*-
# @Author: amit chanchal
# @Date:   2016-07-19 19:56:16
# @Last Modified by:   amit chanchal
# @Last Modified time: 2016-07-19 23:39:32
import os
from flask import Flask, url_for, jsonify, request
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

# setting the db path to the root path of the folder
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir,'../data.sqlite')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'+db_path

db = SQLAlchemy(app)

class ValidationError(ValueError):
	"""docstring for ValidationError"""
	pass

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


class Organizations(db.Model):
	"""
		Defining the database model for Organizations table.
		Version 0.0.2, Date: 19-07-2016 author: Amit Chanchal
		DB Table Schema:
			id, name, category_id, Legal, Type, Activity, description	
			geo_village, geo_district, geo_state, geo_country, geo_pincode	
			phone, address, email
			social_website, social_linkedin ,social_twitter, social_facebook, social_instagram	
			startdate, admin
	"""
	__tablename__ = 'organizations'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(65))
	group = db.Column(db.Boolean) # group or individual
	legal = db.Column(db.String(25)) # society, not for profit, trust, llc, public, sole propriety..
	#type??
	# activities <<-- Another table
	description = db.Column(db.Text)
	geo_town = db.Column(db.String(65))
	geo_state = db.Column(db.String(65))
	geo_country = db.Column(db.String(75))
	geo_postcode = db.Column(db.String(12))
	phone = db.Column(db.Integer(16))
	address = db.Column(db.Text)
	wensite = db.Column(db.String(255))
	social_linkedin = db.Column(db.String(255))
	social_twitter =  db.Column(db.String(255))
	social_facebook = db.Column(db.String(255))
	social_instagram = db.Column(db.String(255))
	create_on = db.Column(db.DateTime)
	join_date = db.Column(db.DateTime)
'''

class Customer(db.Model):
	"""docstring for Customer"""
	__tablename__ = "customers"
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(64), index = True)

	def get_url(self):
		return url_for('get_customer', id = self.id, _external = True)

	def export_data(self):
		return {
			'self_url': self.get_url(),
			'name': self.name
		}
	def import_data(self,data):
		try:
			self.name = data['name']
		except KeyError as e:
			raise ValidationError ('Invalid customer: Missing'+ e.args[0])
		return self

@app.route('/customers/', methods = ['GET'])
def get_customers():
	return jsonify({'customers': [customer.get_url() for customer in Customer.query.all()]})

@app.route('/customers/<int:id>', methods = ['GET'])
def get_customer(id):
	return jsonify(Customer.query.get_or_404(id).export_data())

@app.route('/customers/', methods = ['POST'])
def new_customer():
	customer = Customer()
	customer.import_data(request.json)
	db.session.add(customer)
	db.session.commit()
	return jsonify({}), 201, {'Location': customer.get_url()}

@app.route('/customers/<int:id>', methods = ['PUT'])
def edit_customer(id):
	customer = Customer.query.get_or_404(id)
	customer.import_data(request.json)
	db.session.add(customer)
	db.session.commit()
	return jsonify ({})

if __name__ == "__main__":
	app.run(debug = True)





	







