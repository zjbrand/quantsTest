import socket
import threading
import dynamic.frame06

# 获取用户请求资源的路径
# 根据请求资源的路径，读取指定文件的数据
# 组装指定文件数据的响应报文，发送给浏览器
# 判断请求的文件在服务端不存在，组装404状态的响应报文，发送给浏览器
class HttpWebServer:
    def __init__(self):
        # 1.编写一个TCP服务端程序
        # 创建socekt
        self.tcp_server_socekt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置端口复用　
        self.tcp_server_socekt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定地址
        self.tcp_server_socekt.bind(("", 9090))
        # 设置监听
        self.tcp_server_socekt.listen(128)

    def handle_client_request(self, client_socekt):
        # 获取浏览器的请求信息
        client_request_data = client_socekt.recv(1024).decode()
        print(client_request_data)
        # 获取用户请求资源的路径
        requst_data = client_request_data.split(" ")
        print(requst_data)

        # 判断客户端是否关闭
        if len(requst_data) == 1:
            client_socekt.close()
            return
        # 求资源的路径
        request_path = requst_data[1]

        if request_path == "/":
            request_path = "/index.html"

        # 服务器判断是否是动态资源
        if request_path.endswith(".html"):
            """动态资源"""
            # 应答行
            response_line = "HTTP/1.1 200 OK\r\n"
            # 应答头
            response_header = "Server:pwb\r\n"

            # if request_path == "/index.html":
            #     # 应答体
            #     response_body = dynamic.frame.index()
            # elif request_path == "/center.html":
            #     # 应答体
            #     response_body = dynamic.frame.center()
            # else:
            #     # 应答体
            #     response_body = dynamic.frame.error()

            response_body=dynamic.frame06.application(request_path)

            # 应答数据
            response_data = response_line + response_header + "\r\n" + response_body

            client_socekt.send(response_data.encode())

            client_socekt.close()
        else:
            """静态资源"""
            # 3.读取固定页面数据，把页面数据组装成HTTP响应报文数据发送给浏览器
            # 根据请求资源的路径，读取指定文件的数据
            try:
                with open("./static" + request_path, "rb") as f:
                    file_data = f.read()
            except Exception as e:
                # 返回404错误数据
                # 应答行
                response_line = "HTTP/1.1 404 Not Found\r\n"
                # 应答头
                response_header = "Server:pwb\r\n"
                # 应答体
                response_body = "404 Not Found sorry"
                # 应答数据
                # 组装指定文件数据的响应报文，发送给浏览器
                response_data = (response_line + response_header + "\r\n" + response_body).encode()

                client_socekt.send(response_data)
            else:
                # 应答行
                response_line = "HTTP/1.1 200 OK\r\n"
                # 应答头
                response_header = "Server:pwb\r\n"
                # 应答体
                response_body = file_data
                # 应答数据
                # 组装指定文件数据的响应报文，发送给浏览器
                response_data = (response_line + response_header + "\r\n").encode() + response_body

                client_socekt.send(response_data)
            finally:
                # 4.HTTP响应报文数据发送完成以后，关闭服务于客户端的套接字
                client_socekt.close()

    def start(self):
        while True:
            # 2.获取浏览器发送的HTTP请求报文数据
            # 建立链接
            client_socekt, client_addr = self.tcp_server_socekt.accept()
            # 创建子线程
            sub_thread = threading.Thread(target=self.handle_client_request, args=(client_socekt,))
            sub_thread.start()


if __name__ == '__main__':
    # 创建服务器对象
    my_web_server = HttpWebServer()
    # 启动服务器
    my_web_server.start()