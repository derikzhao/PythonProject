# encoding:UTF-8
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 定义socket类型，网络通信，TCP

host = socket.gethostname()  # ip
port = 9084

s.bind((host, port))
s.listen(5)

while True:
    conn, addr = s.accept()
    print"conneced："
    print addr
    while True:
        data = conn.recv(1024)
        print data
        conn.send("server:successful")

    ''' cmd_status, cmd_result = commands.getstatusoutput(
         data)  # commands.getstatusoutput执行系统命令（即shell命令），返回两个结果，第一个是状态，成功则为0，第二个是执行成功或失败的输出信息
     if len(cmd_result.strip()) == 0:  # 如果输出结果长度为0，则告诉客户端完成。此用法针对于创建文件或目录，创建成功不会有输出信息
         conn.sendall('Done.')
     else:
         conn.sendall(cmd_result)  # 否则就把结果发给对端（即客户端）'''

conn.close()
