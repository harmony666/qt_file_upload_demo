import tkinter as tk
from tkinter import filedialog
import socket
import os
import sys
import struct


def choose():
    root = tk.Tk()
    root.withdraw()
    # 获取文件夹路径 global为全局变量关键字
    global f_path
    f_path = filedialog.askopenfilename()  # 返回值为所选择文件的绝对路径
    print('\n获取的文件地址：', f_path)


def send():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 修改ip
        s.connect(('127.0.0.1', 5555))  # 此处ip必须为服务器端的ip

    except socket.error as msg:
        print(msg)
        sys.exit(1)

    while True:
        filepath = f_path  # 传输文件的路径
        if os.path.isfile(filepath):
            # 定义定义文件信息。128s表示文件名为128bytes长，l表示一个int或log文件类型，在此为文件大小
            # fileinfo_size = struct.calcsize('128sq')
            # 定义文件头信息，包含文件名和文件大小
            fhead = struct.pack('128sq', bytes(os.path.basename(filepath).encode('utf-8')), os.stat(filepath).st_size)
            s.send(fhead)

            print('client filepath: {0}'.format(filepath))
            with open(filepath, 'rb') as fp:
                while True:
                    data = fp.read(1024)
                    if not data:
                        print('{0} file send over...'.format(filepath))
                        break
                    s.send(data)
        s.close()
        break



