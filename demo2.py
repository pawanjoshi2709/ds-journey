import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("insert into test1.table_test values(234,'pawan',43,34.2,'joshi')")
mydb.commit()
mydb.close()