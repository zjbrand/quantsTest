import pymysql

# 创建连接
conn = pymysql.connect(host="localhost",
                       port=3306,
                       database="mysql",
                       user="root",
                       password="123456",
                       charset="utf8")
# 创建游标
cursor = conn.cursor()
# 执行sql语句
sql = "select * from info;"
cursor.execute(sql)
# 获取数据
stock_data = cursor.fetchall()
print(stock_data)