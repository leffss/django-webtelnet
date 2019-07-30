from channels.generic.websocket import WebsocketConsumer
from django_webtelnet.tools.telnet import Telnet
from django.http.request import QueryDict
from django.utils.six import StringIO
import os
import json
import base64
import re


class WebTelnet(WebsocketConsumer):
    message = {'status': 0, 'message': None}
    """
    status:
        0: telnet 连接正常, websocket 正常
        1: 发生未知错误, 关闭 telnet 和 websocket 连接

    message:
        status 为 1 时, message 为具体的错误信息
        status 为 0 时, message 为 telnet 返回的数据, 前端页面将获取 telnet 返回的数据并写入终端页面
    """

    def connect(self):
        """
        打开 websocket 连接, 通过前端传入的参数尝试连接 telnet 主机
        :return:
        """
        self.accept()
        query_string = self.scope.get('query_string')
        telnet_args = QueryDict(query_string=query_string, encoding='utf-8')

        port = telnet_args.get('port')
        port = int(port)

        ssh_key_name = telnet_args.get('ssh_key')
        passwd = telnet_args.get('password')

        host = telnet_args.get('host')
        user = telnet_args.get('user')

        if passwd:
            passwd = base64.b64decode(passwd).decode('utf-8')
        else:
            passwd = None

        self.telnet = Telnet(websocker=self, message=self.message)

        telnet_connect_dict = {
            'host': host,
            'user': user,
            'port': port,
            'password': passwd,
            'timeout': 30,
        }

        self.telnet.connect(**telnet_connect_dict)

    def disconnect(self, close_code):
        try:
            if close_code == 3001:
                pass
            else:
                self.telnet.close()
        except:
            pass
        finally:
            print('命令: ')
            print(self.telnet.cmd)
            print('结果: ')
            print(self.telnet.res)

    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        if type(data) == dict:
            status = data['status']
            if status == 0:
                data = data['data']
                self.telnet.shell(data)
            else:
                pass

