import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="mariadb",
  database="maintenance"
)
mycursor=mydb.cursor(dictionary=True)
sql="insert into assets (Manufacture_Brand,Cost,Invoice_no) values(%s,%s,%s)"
val =['Samsung tablet',25000,'2635']
mycursor.execute(sql,val)

sql_query="select * from assets"

mycursor.execute(sql_query)
records=mycursor.fetchall()
mydb.commit()
print("Data",mycursor.rowcount)
print(records)
mycursor.close()
mydb.close()
