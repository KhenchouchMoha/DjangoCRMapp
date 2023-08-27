import mysql.connector

#db connection 
database=mysql.connector.connect(
 host= 'localhost',
 user='mohamed',
 passwd='661v-rm244'
)

#prepare a cursor object
cursorObject=database.cursor()

#create a database 
cursorObject.execute("CREATE DATABASE khenchouch")

print("done!")