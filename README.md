## 说明
基于 python3.7 + django 2.2.3 实现的 django-webtelnet。有兴趣的同学可以在此基础上稍作修改集成到自己的堡垒机中。

### 所需技术: 
- websocket，django-channels 为 django 提供 websocket 支持
- xterm.js 前端模拟 shell 终端的一个库
- telnetlib，python 自带的一个 telnet 连接库

### 如何将所需技术整合起来？
1. xterm.js 在浏览器端模拟 shell 终端, 监听用户输入通过 websocket 将用户输入的内容上传到 django
2. django 接受到用户上传的内容, 将用户在前端页面输入的内容通过 telnetlib 建立的 telnet 通道上传到远程服务器执行
3. telnetlib 将远程服务器的处理结果返回给 django
4. django 将 telnetlib 返回的结果通过 websocket 返回给用户
5. xterm.js 接收 django 返回的数据并将其写入前端页面

###目前存在的问题
由于 telnetlib 库的原因，终端无法显示颜色已经动态改变大小

## 启动
```
pip3 install -r requirements.txt
cd django-webtelnet/webtelnet/
python3 manage.py runserver 0.0.0.0:8000
```	
访问：http://127.0.0.1:8000

## 预览
![](https://github.com/leffss/django-webtelnet/blob/master/screenshots/1.PNG?raw=true)
![](https://github.com/leffss/django-webtelnet/blob/master/screenshots/2.PNG?raw=true)
![](https://github.com/leffss/django-webtelnet/blob/master/screenshots/3.PNG?raw=true)
![](https://github.com/leffss/django-webtelnet/blob/master/screenshots/4.PNG?raw=true)
![](https://github.com/leffss/django-webtelnet/blob/master/screenshots/5.PNG?raw=true)
![](https://github.com/leffss/django-webtelnet/blob/master/screenshots/6.PNG?raw=true)
