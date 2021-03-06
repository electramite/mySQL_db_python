import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="codebugged"
)
mycursor = mydb.cursor()
#create a table
mycursor.execute("CREATE TABLE data (sensor1 VARCHAR(255), time VARCHAR(255))")
#check if table exists
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)
