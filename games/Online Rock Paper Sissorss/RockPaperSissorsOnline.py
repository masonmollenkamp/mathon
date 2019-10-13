#Client-side Rock paper sissors

import socket
import os

while 1:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.1.11", 50007))
    print("Connected to server.\nWaiting for matches")
    jstring = s.recv(16).decode("utf-8")
    if jstring.split(" ")[0] == 1:
        print("Match found.")
    else:
        print("No match found")
        quit()
    if input("Press enter to ready or quit to quit").lower() != "quit":
        s.send("*".encode('utf-8'))
    else:
        quit()
    s.send(bytes(input("Rock, Paper, Sissors, Shoot!")))
    jstring = s.recv(16).decode("utf-8")
    if jstring[0] == "1":
        print("You Win!")
    elif jstring[0] == "1":
        print("you lost")
    else:
        print("An error has occured. Error code {}".format(jstring[0]))
    
                
    