import sys
import os

def usage():
    print("Usage:\nSSH-sub.py Target_host Target_port\n-l = Listen Mode\n")

def main():
    if not len(sys.argv[1:]):
        usage()
    
    try:
        opt, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu:", ["help", "listen", "execute", "target", "port", "command", "upload"])
    except getopt.GetopteError as e:
        usage()
    
    
