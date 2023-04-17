#-*-coding:utf-8-*-
from socket import *
import app

# 1 定义域名和端口号
HOST,PORT = '192.168.159.1',8080
# HOST,PORT = '127.0.0.1',6666
# 2 定义缓冲区 缓存
BUFFER_SIZE = 1024
ADDR = (HOST,PORT)

# 创建服务器套接字 AF_INET:IPv4 SCOK_STREAM :协议
tcpServerSocket = socket(AF_INET,SOCK_STREAM)

# 4 绑定域名和端口号
tcpServerSocket.bind(ADDR)

# 5 监听连接的最大连接数
tcpServerSocket.listen(5)
print("服务器启动...")
# 定义一个循环 目的：等待客户端的连接
while True:

    # 6.1 打开一个客户端对象，同意连接
    tcpClientSocket,addr = tcpServerSocket.accept()
    print('连接服务器的客户端对象',addr)

    # 6.2 循环的过程
    while True:
        # 6.3 从缓冲区读取指定长度的数据
        # decode()解吗 bytes -> str  encode()编码 str->bytes
        data = tcpClientSocket.recv(BUFFER_SIZE).decode()

        if not data:
            break
        print('data=',data)

        data = app.reply(data)
        print(data)
        tcpClientSocket.send(('%s'%(data)).encode())



    # 7 关闭资源
    tcpClientSocket.close()

tcpServerSocket.close()

