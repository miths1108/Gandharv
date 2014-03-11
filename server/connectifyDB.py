import MySQLdb

def getDB():
	db = MySQLdb.connect( unix_socket = "/Applications/MAMP/tmp/mysql/mysql.sock", user="root", passwd="root", host="localhost",db="majorproj")
	return db
