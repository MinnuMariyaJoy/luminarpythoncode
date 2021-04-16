import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="pythonfeb",
    auth_plugin='mysql_native_password'

)


cursor=db.cursor()
# sql="create table demo(eid int, ename varchar(50),desig varchar(30),salary int)"
# cursor.execute(sql)
# db.close()
 sql="insert into demo(eid,ename,desig,salary) values(1009,'amal','hr',25000)"
try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print(e.args)
    db.rollback()
finally:
    db.close()
