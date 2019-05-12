#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
#! -*- coding:utf-8 -*-

from websocketServer.webSocketServer import webSocketServer

class webSocketServiceDaemon(webSocketServer):
    def __init__(self):
        super().__init__()

    #通讯格式为：{"status":"ok", "message":"xxxx"}。
    def accordActionToSend(self, sock, message):
        print(message)
        if "action" in message and "info" in message:
            if message["action"] == "getRoomInfo":  # websocket连接（握手）完成，客户端会直接发送这个数据到这儿
                self.dictSocketHandleSendContent[sock] = '{"status":"ok", "message":' + str(self.dictRoom) + '}'
            else:
                self.dictSocketHandleSendContent[sock] = '{"status":"ok", "message":"未知操作类型"}'
        else:
            self.dictSocketHandleSendContent[sock] = '{"status":"error", "message":"通讯数据格式错误"}'

if __name__ == "__main__":
    webSocketServiceDaemon()