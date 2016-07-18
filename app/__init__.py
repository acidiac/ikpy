from flask import Flask, Response

class MyResponse (Response):
	default_mimetype = 'application/xml'
	# !! check for mimetype and which ones do we use for json data for responses



# App factory pattern 

def make_app(config_filename):
	app = Flask(__name__)
	app.config.from_object(config_filename)
	# !! check for the config from file options for production and development servers 
	app.response_class = MyResponse

	from app.db import db
	# !! write a seperate db config to take care of this, so that we can initialize from an independent file
	db.init_app(app)

	# Registering Blueprints

	# !! import all the views and then 
	from app.x.views import y
    app.register_blueprint(x, url_prefix='/api/x')
    

    return app
