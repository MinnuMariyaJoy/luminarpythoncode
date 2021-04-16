#mysql- connector
#step 1 -import mysql module
import mysql.connector
#step 2 - establish connection
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    auth_plugin='mysql_native_password'


)
#step 3 - create curser object (for transporting data from and to )

cursor=db.cursor()
#step 4- execute sql quries
sql="select version()"
cursor.execute(sql)
data=cursor.fetchone()
print(data)
db.close()
#step 5  - close database connection

