# 服务端
# -*- coding=utf-8 -*-
import socket
import threading
import sys
import os
import struct
from tkinter import filedialog
import tkinter as tk
import send_choose
import easygui


def deal_data(conn, addr):
    print('Accept new connection from {0}'.format(addr))  # 查看发送端的ip和端口
    while True:
        fileinfo_size = struct.calcsize('128sq')  # linux 和 windows 互传 128sl 改为 128sq  机器位数不一样，一个32位一个64位
        buf = conn.recv(fileinfo_size)  # 接收的文件名字
        print('收到的字节流：', buf, type(buf))
        if buf:
            print(buf, type(buf))
            filename, filesize = struct.unpack('128sq', buf)
            fn = filename.strip(str.encode('\00'))
            if not os.path.exists('./like1'):
                os.mkdir('./like1')
            sPath = easygui.diropenbox()
            #easygui.msgbox(sPath)

            print('\n存储的文件地址：', sPath)
            new_filename = os.path.join(str.encode(sPath), str.encode('new_') + fn)
            print('file new name is {0}, filesize if {1}'.format(new_filename, filesize))
            recvd_size = 0  # 定义已接收文件的大小
            with open(new_filename, 'wb') as fp:
                print("start receiving...")
                while not recvd_size == filesize:
                    if filesize - recvd_size > 1024:
                        data = conn.recv(1024)
                        recvd_size += len(data)
                    else:
                        data = conn.recv(filesize - recvd_size)
                        recvd_size = filesize

                    fp.write(data)
            print("end receive...")
        conn.close()
        break


def socket_service():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 修改ip,此处ip必须为服务器端的ip ,linux做服务器输入ifconfig得到ip
        s.bind(('127.0.0.1', 5555))
        s.listen(10)

    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print("Waiting...")
    while True:
        conn, addr = s.accept()
        t = threading.Thread(target=deal_data, args=(conn, addr))
        t.start()


if __name__ == '__main__':
    socket_service()

