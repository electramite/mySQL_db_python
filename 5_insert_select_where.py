import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="sensor_data"
)
mycursor = mydb.cursor()
#insert
sql = "INSERT INTO data (sensor1, time) VALUES (%s, %s)"
val = ("23.4", "12:45")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

#insert multiple
sql = "INSERT INTO data (sensor1, time) VALUES (%s, %s)"
val = [
  ('23.56', '12:46'),
  ('45.17', '12:47')

]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")

#Insert one row and return the ID
sql = "INSERT INTO data (sensor1, time) VALUES (%s, %s)"
val = ("23.4", "12:45")
mycursor.execute(sql, val)
mydb.commit()
print("1 record inserted, ID:", mycursor.lastrowid)

#SELECT and display the table
mycursor.execute("SELECT * FROM data")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

#Select only name and address
mycursor.execute("SELECT sensor1, time FROM data")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

#Fetchone method - will return the first row of the result
mycursor.execute("SELECT * FROM data")
myresult = mycursor.fetchone()
print(myresult)

#WHERE
sql = "SELECT * FROM data WHERE time ='12:47'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
