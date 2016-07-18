from app import make_app

app = make_app('config')

if __name__ = "__main__":
	app.run( 	host = app.config['HOST'],
				port = app.config['PORT'],
				debug = app.config['DEBUG'])

	