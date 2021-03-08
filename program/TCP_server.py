#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/3/4 14:49
# 工具：PyCharm
# Python版本：3.7.0

# python 2
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

# python 3
# import sys
# import importlib
# importlib.reload(sys)

import socket
"""
1.创建 TCP 服务端的 socket
2.bing 绑定 ip 地址和端口号
3.listen 使套接字变为被动套接字
4.accept 取出一个客户端连接，用于服务
5.recv/send 接收和发送消息
6.关闭套接字
"""
# server
def main():
 # 1、创建 tcp 服务端的 socket
 server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

 # 2、绑定
 server_socket.bind(('', 8888))

 # 3、listen 使套接字变为被动套接字
 server_socket.listen(128)

 # 4、如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务
 # client_socket 用来为这个客户端服务
 # tcp_server_socket 就可以省下来专门等待其他新客户端的链接
 client_socket, client_addr = server_socket.accept()

 # 5、接收客户端发来的消息
 recv_data = client_socket.recv(1024)
 print("接收到客户端%s 的数据：%s" % (str(client_addr), recv_data.decode('gbk')))

 # 6、回复数据给客户端
 client_socket.send("收到消息".encode('gbk'))

 # 7、关闭套接字
 client_socket.close()
 server_socket.close()

if __name__ == '__main__':
 main()