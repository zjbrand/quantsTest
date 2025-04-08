import socket

# 建立与服务器端通信的客户端对象
client_socket=socket.socket()

# 连接到服务器端
client_socket.connect(("localhost", 8888))


while True:
    # 发送信息
    msg=input("请输入要给服务器发送的消息：")
    if msg=="exit":
        break
    client_socket.send(msg.encode("UTF-8"))
    # 接受返回消息
    recv_data=client_socket.recv(1024)
    print(f"服务器回复的消息：{recv_data.decode('UTF-8')}")

#关闭连接
client_socket.close()


