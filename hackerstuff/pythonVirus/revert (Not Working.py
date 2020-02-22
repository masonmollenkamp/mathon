import os
import KeyKript

path = "C:\\Users\\Mason Mollenkamp\\Desktop\\repo\\mathon\\hackerstuff\\pythonVirus\\Test\\" #file encript
directories = os.listdir(path)

for file in directories:
    with open(path + file, "r+") as f:
        Numbers = f.readlines()[0].strip(" ").split(" ")
        print(Numbers)
        f.write(KeyKript.ecdc(5, 91, "d", Numbers)) 