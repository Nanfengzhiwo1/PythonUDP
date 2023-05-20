
import socket  # 导入socket模块


# server 服务端
# 设置服务器默认端口号
# UDP不用连接
HOST = "本机IP地址"
PORT = 10086
# 创建一个套接字socket对象，用于进行通讯
# socket.AF_INET 指明使用INET地址集，进行网间通讯
# socket.SOCK_DGRAM 指明使用数据协议，即使用传输层的udp协议
udp_server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 绑定地址
udp_server.bind((HOST,PORT))
print("开始监听...")
while True:
    data,addr = udp_server.recvfrom(1024)
    # addr[0]:代表ip，addr[1]：代表端口,这是个元组
    print("Recieved {} from {}:{}".format(data,addr[0],addr[1]))
    if data == b"exit":
        print("服务器退出")
        break
    udp_server.sendto(data,addr)
udp_server.close()
