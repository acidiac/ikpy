

# DB SETTINGS

mysql_user	= 'ikadmin'
mysql_auth	= ''
mysql_db	= 'ikdb'
mysql_host	= 'localhost'

# These are development settings
DEBUG = True 
PORT = 5000
HOST = "127.0.0.1"
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = " "

#MYSQL SQLALCHEMY SETTINGS
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(DB_USER=mysql_user,
                                                                                        DB_PASS=mysql_auth,
                                                                                        DB_ADDR=mysql_host,
                                                                                        DB_NAME=mysql_db)



