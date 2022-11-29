demo完成的功能

![img](https://cdn.nlark.com/yuque/0/2022/png/29622176/1669690992313-045892a2-aea4-4b24-aaf3-492a41b8b4fc.png)

在选择分析报告中选择本地一个文件，然后点击上传到指定文件夹，在本地windows机器模拟与服务器的文件上传下载。



# 环境需求

python版本：3.9

pyqt版本：pyqt6

安装命令

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyqt6
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple PySide6
```

# 报错信息解决方法

![img](https://cdn.nlark.com/yuque/0/2022/png/29622176/1669691015420-1ae1d5e8-3405-4fd2-a622-6ba7b1dd0ee6.png)



添加环境变量即可

![img](https://cdn.nlark.com/yuque/0/2022/png/29622176/1669691018511-3d40e7fa-11fa-4df2-a139-1e4fcede252e.png)

```
QT_QPA_PLATFORM_PLUGIN_PATH
D:\developer_tools\Anaconda3\Lib\site-packages\PySide6\plugins\platforms
```

# 学习参考链接

https://blog.csdn.net/qq_37193537/article/details/91043580

https://www.jb51.net/article/215587.htm
