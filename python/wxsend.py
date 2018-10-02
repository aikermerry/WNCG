import itchat
#微型传输文件举例
import time
itchat.auto_login(hotReload=True)

itchat.send('Hellofileheldper', toUserName='filehelper')
itchat.send_file(r"C:/Users/11395/Desktop/Python.txt",toUserName='filehelper')