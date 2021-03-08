#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/3/4 14:44
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
1.创建客户端套接字
2.发送/接收数据
3.关闭套接字
"""
import socket
def main():
# 1、创建 udp 套接字
# socket.AF_INET 表示 IPv4 协议 AF_INET6 表示 IPv6 协议
# socket.SOCK_DGRAM 数据报套接字，只要用于 udp 协议
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 2、准备接收方的地址
# 元组类型 ip 是字符串类型 端口号是整型
    dest_addr = ('192.168.113.111', 8888)
# 要发送的数据
    send_data = "我是要发送的数据"
# 3、发送数据
    udp_socket.sendto(send_data.encode("utf-8"), dest_addr)
# 4、等待接收方发送的数据 如果没有收到数据则会阻塞等待，直到收到数据
# 接收到的数据是一个元组 (接收到的数据, 发送方的 ip 和端口)
# 1024 表示本次接收的最大字节数
    recv_data, addr = udp_socket.recvfrom(1024)
# 5、关闭套接字
    udp_socket.close()


if __name__ == '__main__':

    main()