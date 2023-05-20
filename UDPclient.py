import socket


# 客户端
# 指定服务器地址
# UDP不用连接
HOST = "本机IP地址"
PORT = 10086


udp_client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
      sendData = input("输入要发送的数据:")
      udp_client.sendto(sendData.encode(encoding="utf-8"),(HOST,PORT))
      if sendData == "exit":
            print("退出")
            break
      info = udp_client.recv(1024).decode(encoding="utf-8")
      print("收到数据:",info)
udp_client.close()