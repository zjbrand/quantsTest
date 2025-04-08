from pymysql import Connection

conn=Connection(
    host='localhost',
    port=3306,
    user='root',
    password='123456'
)

#print(conn.get_server_info())
# 获取游标对象
cursor=conn.cursor()

#选择数据库
conn.select_db("mysql")

cursor.execute("select * from focus")

results:tuple=cursor.fetchall()

for r in results:
    print(r)


conn.close()