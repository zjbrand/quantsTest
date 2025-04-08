import socket

#这是服务器端的程序

#创建Socket对象
socket_server=socket.socket()

#绑定IP地址，参数为一个元组
socket_server.bind(("localhost",8888))

#监听端口,listen的参数为接受的链接个数
socket_server.listen(1)

#等待客户端链接
# result:tuple=socket_server.accept()
# conn=result[0] #客户端和服务器链接对象
# address=result[1] #客户端地址信息

conn,address=socket_server.accept()
#accept为阻塞方法，会停在这等待

print(f"接收到了客户端的链接，客户端的信息是：{address}")
while True:
    #用链接对象接受客户端信息,recv参数为缓冲区大小
    data:str=conn.recv(1024).decode("UTF-8")
    #recv也是一个阻塞方法

    print(f"客户端发来的消息是:{data}")

    #发送回复消息
    msg=input("请输入你要和客户端回复的消息:")
    if msg=="exit":
        break
    conn.send(msg.encode("UTF-8"))

#关闭链接
conn.close()
socket_server.close()


