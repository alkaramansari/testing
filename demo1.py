import MySQLdb



# Open database connection
db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

print("ok")

# disconnect from server
db.close()
