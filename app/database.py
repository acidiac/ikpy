from app import db

def dbAdmin():
	option =  str(input("please select an option 'c' from create DB and 't' for teardown DB : "))
	if option == 'c':
		try:
			db.create_all()
		except e:
			print("script has errors {}".format(e))
	elif option == 't':
		try:
			pass
		except e:
			print("script has errors {}".format(e))
	else:
		print("please enter one of the provided options.")
		dbAdmin()
