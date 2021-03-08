#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/3/4 14:47
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
""""""

"""

1.创建 TCP 的 socket 套接字
2.连接服务器
3.发送数据给服务器端
4.接收服务器端发送来的消息
5.关闭套接字

"""

# client
import socket
def main():
 # 1、创建客户端的 socket
 # socket.AF_INET 表示 IPv4 协议 AF_INET6 表示 IPv6 协议
 # socket.SOCK_STREAM 流式套接字，只要用于 TCP 协议
 client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 # 2、构建目标地址
 server_ip = input("请输入服务器端的 IP 地址：")
 server_port = int(input("请输入服务器端的端口号："))
 # 3、连接服务器
 # 参数：元组类型 ip 是字符串类型 端口号是整型
 client_socket.connect((server_ip, server_port))
 # 要发送给服务器端的数据
 send_data = "我是要发送给服务器端的数据"
# 4、发送数据
 client_socket.send(send_data.encode("gbk"))
 # 5、接收服务器端恢复的消息， 没有消息会阻塞
 # 1024 表示接收的最大字节数
 recv_date= client_socket.recv(1024)
 print("接收到的数据是：", recv_date.decode('gbk'))
 # 6、关闭套接字
 client_socket.close()
if __name__ == '__main__':
 main()