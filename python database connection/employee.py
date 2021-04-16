import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="pythonfeb",
    auth_plugin='mysql_native_password'

)

cursor=db.cursor()
f=open ("employeefile")
for lines in f:                              # 102,ram,26500
    data=lines.rstrip("\n").split(",")      #[102,ram,26500]
    sql="insert into demo(eid,ename,desig,salary) values(%s,%s,%S,%s)"
    cursor.execute(sql,tuple(data))
    db.commit()
db.close()

