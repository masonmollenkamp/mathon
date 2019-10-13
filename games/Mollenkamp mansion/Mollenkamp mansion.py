import sys
import random
import os

os.system('clear')
help = "List of commands:\n1.inspect or examine, type one and then the item name\n2.interact or use, type one and then the item name\n3.inspect or examine, type one and then the item name"
print(help)

invatory = ["Redroom key"]
currentRoom = "redroom"
gameIteration = 1
Quit = False

rooms = {"Redroom" :
         {
           "Locked"  :
            "locked", 
            "Bed" :
              ["it's a bed", {
                  "sleep " : "Sleeping...", "jhgdfsjf " : "hjrfgrjdfghrj f"}],
            "phone" :
              ["its a phone", {
                  "unlock" : "print('this concludes the test')\nprint('everything is awsome')"},
                   10,
                    {8 : "tiny crack", 7 : "pretty big crack", 6 : "crack across the screen", 5 : "multiple scrtches and one huge crack", 4 : "2 Huge Cracks", 3 : "Display broken", 2 : "Screen detached", 1 : "bits and pieces"}]
            },
         "redroom" :
         {
             "Locked" : "unlocked",
             "Mysterious SSD" :
             ["it's a table", {"unscrew" : """rooms[redroom] += {\"Badge\" : [\"it can go into one of the slots in the jacket.\", {\"Put pin in holes\" : \"\"\"if computerDone == 1 && input(\"which hole\") == 4:
	print(\"The right latch on the white door is open\")
	badge = True\"\"\""""]}],
             "chair" :
             ["it's a chair", "sit"]},
         "blueroom" :
         {
             "Locked" : "unlocked",
             "Saw" : ["it's just a saw", {"litraly nothing" : "print(\"seriosly\")"}, 2, {1 : "the saw won't snap"}]
             "computer" : ["no logo", {"use another item" : " Bannana = print(\"A load sound breaks the silence, you look at the white door and the left latch has opened. you get it, you had to add the logo to the Bannana(C) computer\") + \"*\" if (input(\"What item\").lower == \"saw\") else print(\"Nothing Happens\")", "play on computer" : "print(\"You get on the computer. A file called Mollenkamp mansion opens up, then you relize that the computer is your computer and an error message occurs on your computer. Hmm, you'll need a new app to open this error link... Aha! it means that the programers made a mistake!\")\nfor i in range(5):\n  os.system(\'start \\\"Mollenkamp mansion.py\\\"\\\necho Error: Virus detected.\')"},
             0, {1 : "its a computer do you think your going to smash it with your bare hand?"}],
             "bananas" : ["there are three of them", {"eat" : "print(\"Attack the bannanas to eat them.\")"}, 2, {1 : "There are 2 of them"}]}
    }


def doGameItaration():
    global gameIteration
    if gameIteration == 1:
        print("Player wakes up in their normal room, but it feels wobbly. They go and open their door and see a sign in a white room ‘Pick a door red or blue, there is a white door in front of them, to the left there is a red and a blue door.")
    elif gameIteration == 2:
        print("The room seems to be themed around bannana(C) the computer company")
        if computerDone == True  &&  Bannana == "*":
            gameIteration == 4
            doGameItaration
commandList = []

for room in rooms:
    for item in rooms[room]:
        for command in rooms[room][item][1]:
            commandList.append([command, item])

def Examine(item):
    global currentRoom

    examineItem = []

    for Command in commandList:
        if Command[1] == item:
            examineItem += Command[0]

    print(rooms[currentRoom][item][0])
    print("You can:")

    y = ""
    for i in range(len(examineItem)):

        y += examineItem[i]
    print(y)

    print("With this item.")

def moveRoom(x):        
    global currentRoom
    global rooms
    global gameIteration

    Error = []

    for room in rooms:
        if x == room:
            if rooms[x]["Locked"] == "unlocked":
                currentRoom = x
                print(x)
                if x == "blueroom":
                    gameIteration = 2
            else:
                Error.append("*")
        else:
            Error.append("")
    print("Locked") 
    print("You are now in {}".format(currentRoom))
    for item in rooms[currentRoom]:
        if "Locked" not in item:
            print(item)

def unlock(room):
    global invatory
    global rooms
    for item in invatory:
        if item.split(" ")[0] == room:
            rooms[room]["Locked"] = "unlocked"
            print("unlocked")
        else:
            print("no key")

def interact(item, command):
    try:
        exec(rooms
            [currentRoom]
            [item][1]
            [command])
    except Exception as e:
        print("Error, that is not an item or that is not a command {}".format(e))

def attack(item, type):
    for forLoopItem in rooms[currentRoom]:
        if item == forLoopItem:
            if type == True:
                Dammage = random.randint(2,8)
                if Dammage < rooms[currentRoom][item][2]:
                    rooms[currentRoom][item][2] = rooms[currentRoom][item][2] - Dammage
                    rooms[currentRoom][item][0] = rooms[currentRoom][item][3][rooms[currentRoom][item][2]]
                else:
                    rooms[currentRoom][item][2] = 1
                    rooms[currentRoom][item][0] = rooms[currentRoom][item][3][rooms[currentRoom][item][2]]
            else:
                if 5 < rooms[currentRoom][item][2]:
                    rooms[currentRoom][item][2] = rooms[currentRoom][item][2] - 5
                    rooms[currentRoom][item][0] = rooms[currentRoom][item][3][rooms[currentRoom][item][2]]
                else:
                    rooms[currentRoom][item][2] = 1
                    rooms[currentRoom][item][0] = rooms[currentRoom][item][3][rooms[currentRoom][item][2]]
    return rooms[currentRoom][item][0]

gameIteration = eval(input("Put in a password or just press enter."))
if gameIteration == "":
    gameIteration == 1

while Quit != True:
    doGameItaration()
    Command = ""
    Command = input()
    try:
        if Command.split(" ")[0] == "inspect" or Command.split(" ")[0] == "examine":
            Examine(Command.split(" ")[1])
        elif Command.split(" ")[0] == "interact" or Command.split(" ")[0] == "use":
            x = ""
            for item in Command.split(" ")[2:]:
                if len(Command.split(" ")[2:]) != (Command.split(" ")[2:].index(item) + 1):
                    x += item + " "  
                else:
                    x = x + item
            interact(Command.split(" ")[1], x)
        elif Command.split(" ")[0] == "unlock" or Command.split(" ")[0] == "open":
            unlock(Command.split(" ")[1])
        elif Command.split(" ")[0] == "goto" or Command.split(" ")[0] == "move":
            moveRoom(Command.split(" ")[1])
        elif Command.split(" ")[0] == "hit" or Command.split(" ")[0] == "attack":
            attack(Command.split(" ")[1], True) if Command.split(" ")[2] == True else attack(Command.split(" ")[1], False)
        else:
            print(help)
    except Exception as e:
        print("An error has occured. {}".format(e))

