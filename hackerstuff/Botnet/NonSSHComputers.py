import socket
import os

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
while 1:
    s.listen(1)
    data = ""
    conn, addr = s.accept()
    print("New Connection")        
    jstring = ""
    while data != "\n":

        data = conn.recv(1).decode("utf-8")
        jstring += data
    print("Running", jstring)
    s.send(os.system(jstring).encode('utf-8'))