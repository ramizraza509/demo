import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="db2"
)


mycursor = mydb.cursor()
mycursor.execute("INSERT INTO customers(name,address) VALUES ('Asif','Kolkata');")
#mycursor.execute("CREATE TABLE customers1 (name VARCHAR(255), address VARCHAR(255))")
mydb.commit()