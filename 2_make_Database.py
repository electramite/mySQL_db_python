import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="yourpassword"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE sensor_data") # creating a database as sensor_data
