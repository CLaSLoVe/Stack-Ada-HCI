import socket

HOST = 'localhost'  # 监听所有可用的网络接口
PORT = 8002  # 监听的端口号

# 创建一个UDP套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定套接字到指定的主机和端口号
server_socket.bind((HOST, PORT))

print('Listening on {}:{}'.format(HOST, PORT))

# 循环接收数据并输出
while True:
    data, addr = server_socket.recvfrom(1024)
    print('Received {} bytes from {}:{}'.format(len(data), addr[0], addr[1]))
    print('Data:', data)