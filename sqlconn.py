import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    username="root",
    password="",
    database="college"
)
print(mydb)
cursor=mydb.cursor()
# cursor.execute("create database college")
cursor.execute("show databases")
for x in cursor:
    print(x)
# cursor.execute("create table student(id int(20) primary key auto_increment,name varchar(20),age int(20),gender enum('male','female'))")
# sql="insert into student (name,age,gender) values(%s,%s,%s)"
# val=[("anu",34,"female"),("sree",34,"female"),("abi",34,"female")]
# cursor.executemany(sql,val)
# print(cursor.rowcount,"row was inserted")
cursor.execute("select * from student where name='sree'")
# for x in cursor:
#     print(x)
result=cursor.fetchall()
print(result)
# mydb.commit()