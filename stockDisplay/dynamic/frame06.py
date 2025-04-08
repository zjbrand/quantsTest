import pymysql
import json

# 路由列表
func_list = {}


# 路由装饰器 向列表中添加数据
def route(data):  # data=>/index.html

    def func_out(func):  # func=> index
        # 添加数据
        func_list[data] = func

        def func_inner():
            pass

        return func_inner

    return func_out


@route("/index.html")  # 1 @func_out  2 index = func_out(index)
def index():
    # 读取模板数据返回给浏览器
    with open("./template/index.html",'r',encoding='utf-8') as f:
        file_data = f.read()

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
    # (1, '000007', '全新好', '10.01%', '4.40%', Decimal('16.05'), Decimal('14.60'), datetime.date(2017, 7, 18))

    template = """
        <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>
            <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="000007">
        </td>
</tr>
    """
    html = ''

    for i in stock_data:
        html += template % (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7],)

    # 模板中的数据替换
    content = file_data.replace("{%content%}", html, 1)

    cursor.close()
    conn.close()

    return content


@route("/center.html")
def center():
    # 读取模板数据返回给浏览器
    with open("./template/center.html",'r',encoding='utf-8') as f:
        file_data = f.read()

    # 模板中的数据替换
    content = file_data.replace("{%content%}", "stock_data", 1)

    return content


# 返回股票数据
@route("/center_data.html")
def center_data():
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
    sql = "select " \
          "info.code,info.short,info.chg,info.turnover,info.price,info.highs,focus.note_info " \
          "from info inner join focus on info.id=focus.id;"

    cursor.execute(sql)
    # 获取数据
    stock_data = cursor.fetchall()
    # 把元组数据转化成列表格式
    # ('000007', '全新好', '10.01%', '4.40%', Decimal('16.05'), Decimal('14.60'), '你确定要买这个？')
    center_data_list = [{
                            "code": row[0],
                            "short": row[1],
                            "chg": row[2],
                            "turnover": row[3],
                            "price": str(row[4]),
                            "highs": str(row[5]),
                            "note_info": row[6],
                          }for row in stock_data]
    # 生成json可是的字符串
    json_str = json.dumps(center_data_list)

    cursor.close()
    conn.close()

    return json_str


def error():
    return "404 error"

# 向路由列表中添加数据
# func_list["/index.html"] = index
# func_list["/center.html"] = center
# 列表中的数据
# {
#     "/index.html":index,
#     "/center.html":center
# }


# 接口 解耦和
def application(request_path):
    # if request_path == "/index.html":
    #     # 应答体
    #     return index()
    # elif request_path == "/center.html":
    #     # 应答体
    #     return center()
    # else:
    #     # 应答体
    #     return error()
    try:
        # 正确的结果
        # index         "/index.html"
        func = func_list[request_path]
        #     index()
        ret = func()
        # 返回对动态数据的处理结果
        return ret
    except Exception as e:
        # 出现错了
        return error()
