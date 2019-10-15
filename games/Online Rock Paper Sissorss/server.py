import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
connectionNumber = 0
while connectionNumber != 2:
    s.listen(1)
    exec("conn{}, addr{} = s.accept()".format(connectionNumber, connectionNumber))
    exec("data = conn{}.recv(16)".format(connectionNumber))
    if (data=="Rock"):
        exec("connection{} = \"Rock\"".format(connectionNumber))
    if (data=="Jared"):
        jared = jared + 1
    if (data=="quit"):
        break  
        exec("conn{}.send('E')".format(connectionNumber))
    connectionNumber += 1
if (connection1 == "paper"):
    if connection2 == "sisors":
        conn1.send('0')
        conn2.send('1')
    elif (com == "rock"):
        conn1.send('1')
        conn2.send('0')
    else:
        print("tie")
if (player == "sisors"):
    if com == "rock":
        conn1.send('0')
        conn2.send('1')
    elif (com == "paper"):
        conn1.send('1')
        conn2.send('0')
    else:
        print("tie")
if (player == "rock"):
    if com == "paper":
        conn1.send('0')
        conn2.send('1')
    elif (com == "sisors"):
        conn1.send('1')
        conn2.send('0')
    else:
        print("tie")
print ("Mason: " + str(mason))
print ("Jared: " + str(jared))