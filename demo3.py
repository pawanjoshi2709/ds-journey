import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("select * from test1.table_test")
for i in mycursor.fetchall():
    print(i)
    