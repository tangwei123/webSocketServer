# webSocketServer
python3 webSocketServer

##### 环境要求：
    linux 使用webSocketServerUseEpollET.py或者webSocketServerUseLT.py文件，因为是用了select的epoll模式，不兼容windows、macos
    windows、macos、linux，都可以使用webSocketServerUseSelector.py。
##### socket运行方式：
    socket全程非阻塞方式。
    webSocketServerUseEpollET.py为边缘触发方式。
    webSocketServerUseLT.py为水平触发方式。
    ET和LT方式，是两种不同的触发方式，代码结构也不一致。
    
    webSocketServerUseSelector.py使用的是selectors的DefaultSelector的，水平触发方式。边缘触发方式我没去研究
#### 接收数据过程：
##### 握手阶段：
    遵从websocket的协议，
    浏览器发起websocket连接，首次（未握手）会发送一个http的头数据包，
    服务端解析头数据包，得到 Sec-WebSocket-Key 与 258EAFA5-E914-47DA-95CA-C5AB0DC85B11 字符串拼接 然后加密数据返回给浏览器，之后握手完成！
##### 数据交互阶段：
    解析数据遵从websocket的协议，每一帧数据！
    第一个字节（第一位FIN代表数据是否发送完毕，后四个位opCode数据类型，数据类型自行查找）
    第二个字节（第一位HasMASK后续数据是否使用了mask掩码加密数据，后七位代表后续数据长度，这儿参考websocket协议即可）
    后续字节按照协议处理。
    每接收一次数据，都需要严格做好处理，异常中途客户端中断（宕机、断电、关闭网页等等突发情况）
    接收每一帧的数据，有多少才接收多少，不能多接收一帧，否则非常容易产生粘包！
    
    发送数据，按照websocket协议即可（大数据也不需要分包！因为2的64次方个字节的数据已经非常非常大了）
##### 目前实现的功能：
    文本传输、大文件上传、网页端接收客户端发送的文件（目前只做了图片接收）、网页端闪断闪连、传输大文件中途关闭浏览器的异常
##### 后续可以实现的功能：
    文件断点续传（逻辑太烦不想写了）、后续很多功能的！
##### 使用方式：
    python webSocketServiceDaemon.py 
    双击index.html文件即可
