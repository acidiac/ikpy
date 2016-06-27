# This file initializes your application and brings together all of the various components.
# /ik/__init__.py 
# author: Amit Chanchal @amitchnchl
# description: main file for the IK application main module
# version : 0.0.2
# Project timeline: June - July 2016

# all the main imports
from flask import Flask 

app = Flask(__name__)
# Using the cofig variables define in /config.py
app.config.from_object('config')





