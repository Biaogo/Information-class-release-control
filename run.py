#!/usr/bin/python3
import os
import re
import signal
print("0.输出默认路径软件列表 1.杀死指定名称的控制软件 2.杀死指定pid 3.打个响指 4.未开发区域")
print("一般电脑室的电脑都会恢复C盘(系统盘),故软件装在系统盘")
cz = int(input("请选择数字:"))
if cz == 1:
    name = input("请输入名称:")
    os.popen("taskkill /f /im:"+str(name))
    print("已执行")
elif cz == 2:
    pid = int(input("输入PID:"))
    os.popen("taskkill /pid:"+str(pid))
    print("已执行")

elif cz == 3:
    code = 'taskkill /f /t /fi "pid ne 1"'
    os.popen(code)
    print("已执行")
else:
    print("come soon...")