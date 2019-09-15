import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="")
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE customers1 (name VARCHAR(255), address VARCHAR(255))")
#mycursor.execute("""INSERT INT customers VALUES'ramiz','Chaibasa')""")
