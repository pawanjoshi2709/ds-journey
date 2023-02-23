import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("create database if not exists test1;")
mycursor.execute("create table if not exists test1.table_test(c1 int ,c2 varchar(45),c3 int, c4 float , c5 varchar(50));")
mydb.close()