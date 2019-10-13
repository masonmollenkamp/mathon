import sys
import random
import os

os.system('clear')
help = "List of commands:\n1.inspect or examine, type one and then the item name\n2.interact or use, type one and then the item name\n3.inspect or examine, type one and then the item name"
print(help)
input()

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
             ["it's a table", "sit down", "put feet up"],
             "chair" :
             ["it's a chair", "sit"]},
         "blueroom" :
         {
             "Locked" : "unlocked",
             "computer" : ["no logo", "sit down", "put feet up"],
             "bananas" : ["there are three of them", "eat", "trash"]}
    }


def doGameItaration(password):
    if password == True:
        gameIteration = password
        doGameItaration("")
    elif gameIteration == "1":
        print("Player wakes up in their normal room, but it feels wobbly. They go and open their door and see a sign in a white room ‘Pick a door red or blue, there is a white door in front of them, to the left there is a red and a blue door.")

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

    Error = []

    for room in rooms:
        if x == room:
            if rooms[x]["Locked"] == "unlocked":
                currentRoom = x
            else:
                Error.append("*")
        else:
            Error.append("")
    print("Locked") 
    print("You are now in {}".format(currentRoom))
    for item in rooms[currentRoom]:
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
    except:
        print("Error, that is not an item or that is not a command")
        print("Would you like to try this item on another item in the room in the invotory")
        Uinput = input()
        if Uinput == True:
            doGameItaration("Uinput")

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


while Quit != True:

    Command = ""
    Command = input()
    if Command.split(" ")[0] == "inspect" or Command.split(" ")[0] == "examine":
        Examine(Command.split(" ")[1])
    elif Command.split(" ")[0] == "interact" or Command.split(" ")[0] == "use":
        interact(Command.split(" ")[1], Command.split(" ")[2])
    elif Command.split(" ")[0] == "unlock" or Command.split(" ")[0] == "open":
        unlock(Command.split(" ")[1])
    elif Command.split(" ")[0] == "goto" or Command.split(" ")[0] == "move":
        moveRoom(Command.split(" ")[1])
    elif Command.split(" ")[0] == "hit" or Command.split(" ")[0] == "attack":
        attack(Command.split(" ")[1], True if Command.split(" ")[2] == True else False)
    else:
        print(help)
